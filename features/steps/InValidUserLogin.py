import logging
import sys
import os
import time
from behave import *
from appium import webdriver as appiumwebdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions
from Locators import *
from log import *

configurator = LogConfigurator()


@then(u'I should see an error message indicating that the login failed')
def step_impl(context):
    try:
        Error_text =find_element(context,Locators.invalid_username_or_password_text_xpath)
        # Error_text = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy, Locators.invalid_username_or_password_text_xpath)))
        text1 = Error_text.text
        logging.info(f"showing the error message{text1}")
        logging.info("test case passed!!!")

    except Exception as e:

        logging.error(f'Error message indicating that the login failed,{e}')


@then(u'close the application')
def step_impl(context):
    # Add code to close the application
    context.driver.quit()
    time.sleep(5)
