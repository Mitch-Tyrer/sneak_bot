# sneak_bot

# Description

This is code for automated online shopping for shoes with the ability to search for products based on key terms, find the correct link to that product and then automatically purchase it.

Currently this code only works for online webstores utilizing the Shopify API.  Built using the Selenium-Python library and the chromium webdriver for automation of form entry.

Is capable of inputing data currently until it reaches the billing information.  Currently working out how to use selenium to reach the proper inputs as they are in an iframe

# Note
This is currently built around a random shopify site I was using to test.  If you want to customize this code you will have to manually modify the xpaths to the html inputs for the shopify site you are using.

# Getting Started

## Downloading python


This needs to be Python version `3.7` or up

MacOS
   * From Python's official website [here](https://www.python.org/downloads/mac-osx/)
   * If you have [brew](https://brew.sh) installed, you can just run the coommand `brew install python3`

Linux
   * From Python's official website [here](https://www.python.org/downloads/source/)
   * Using the package manager for your system. With Ubuntu, this command is `sudo apt install python3-dev`

Windows
   * From Python's official website [here](https://www.python.org/downloads/windows/)
   * If you have the [Chocolatey package manager](https://chocolatey.org/) installed, you can run `choco install python`


# Current Dependencies

At the moment this code only requires the following dependencies to run:

```
pip install requests
pip install selenium

```

#Using Selenium.
Please visit `https://selenium-python.readthedocs.io/index.html` for more information about this python plugin.

In order to run this script you will need to install one of the following drivers related to the version of your preferred web browser.

```
Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/
```

# How to use.
Before anything else modify the `user_info.txt` file with your preferred credentials.  The formatting is very strict so only change the information, leave the keys the same and the spacing around the colons is intentionally.

   * Your modified file values should look like this:
         ```
         email : example@example.com
         ```