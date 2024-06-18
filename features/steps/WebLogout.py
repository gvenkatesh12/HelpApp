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


@then(u'I Logout')
def step_impl(context):
    try:
        # logout =find_element(context, Locators.logout_button_xpath)
        logout = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, locators.logout_button_xpath)))
        logout.click()
        logging.info("Logged out successfully!")
    except Exception as e:
        logging.error(f'Error while logging out: {e}')

