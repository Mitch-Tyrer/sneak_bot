# import libraries/dependences

from os import stat
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait

# import credentials from external text file and convert to a dictionary [include all form elements from a shopify checkout]
user_info = {}
#url = input("What shopify store do you want to search? ")
#search = input("What are you searching for? ")



f = open('user_info.txt', 'r')
for line in f:
    (key, val) = line.strip().split(' : ')
    user_info[key] = val

# Function that searches for key terms in a json product list

print(user_info)

def search_products():
    usr_query = input("What type of product are you looking for? ")
    r = requests.get(f"{url}products.json")
    products = json.loads((r.text))['products']

    found_products = {}
    k = 1
    for product in products:
        if usr_query in product['title']:
            found_products[k] = product['title']
            k += 1

    for choices in found_products:
        print(choices, found_products[choices])

    choice = input("Enter the number of the product you're looking for? ")
    while True:
        try:
            choice = int(choice)
            search = found_products[choice]
            break
        except:
            choice = input("Selection needs to be a number: ")

    return search


# Function to Check if item is available by searching throught the products json (shopname.com/products.json)
# Do this by comparing the desired user input against the 'title' in the json
# append the 'handle' to the url (shopname.com/products)
url = "https://www.allbirds.com/"
search = "Women's Tree Breezers - Everest (Dark Green Sole)"

def check_availability(url, search):
    r = requests.get(f"{url}products.json")
    products = json.loads((r.text))['products']
    for product in products:
        print(product['title'])
        product_name = product['title']

        if product_name == search:
            print(product_name)
            product_url = f"{url}products/{product['handle']}"            
            return product_url
    else:
        return False


# If available open the site select size (may need to add a way to search for inputs for buttons and selects as well as a name/label for size)
# Click add to cart
# Click checkout
# fill in form with information from dictionary


test_url = check_availability(url, search)
driver = webdriver.Chrome(executable_path=r'C:\Users\necro\Documents\Coding\Selenium_BrowserDrivers\chromedriver.exe')
driver.get(test_url)


driver.find_element_by_xpath('//button[@aria-label="Add Size 10"]').click()
driver.find_element_by_xpath('//button[@id="add-to-cart"]').click()
time.sleep(5)
driver.find_element_by_xpath('//a[@href="/checkout?locale=en-US"]').click()
time.sleep(5)
driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(user_info['email'])
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys(user_info['first_name'])
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys(user_info['last_name'])
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys(user_info['address'])
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys(user_info['city'])
time.sleep(1)
select = Select(driver.find_element_by_xpath('//select[@placeholder="State"]'))
select.select_by_value(user_info['state'])
time.sleep(1)
driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys(user_info['zip'])
time.sleep(1)
driver.find_element_by_xpath('//button[@id="continue_button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//button[@id="continue_button"]').click()
time.sleep(10)

#billing informations
driver.find_element_by_xpath('//iframe[@class="card-fields-iframe"]').send_keys(user_info['card_num'])
time.sleep(1)
driver.find_element_by_xpath('//input[@id="name"]').send_keys(f"{user_info['first_name']} {user_info['last_name']}")
time.sleep(1)
driver.find_element_by_xpath('//input[@id="expiry"]').send_keys(user_info['exp_date'])
time.sleep(1)
driver.find_element_by_xpath('//input[@id="verification_value"]').send_keys(user_info['sec_code'])
time.sleep(1)
driver.find_element_by_xpath('//button[@id="continue_button"]').click()



# way to interate over and find the value tags in a html select
# select = driver.find_element_by_xpath('//select[@placeholder="State"]')
# states = select.find_elements_by_tag_name("option")
# stateList = []
# for state in states:
#     stateList.append(state.get_attribute("value"))