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
cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "sdk_gphone_x86",
    "app": r"C:\Users\Manik\Downloads\base (3).apk",
    "automationName": "UiAutomator2",
    "resetKeyboard": True

}
# cap = {
#     "platformName": "Android",
#     "platformVersion": "14",
#     "appium:automationName": "UiAutomator2",
#     "deviceName": "motorola edge 50 pro",
#     "app": r"C:\Users\Manik\Downloads\base (3).apk",
#     "automationName": "UiAutomator2",
#     "resetKeyboard": True
# }

@given(u'i launch the application')
def step_impl(context):
    try:
        configurator.before_all(context)
        sys.path.append(os.getcwd())
        context.driver = appiumwebdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(cap))
        time.sleep(2)
        logging.info('Application launched successfully!')
    except Exception as e:
        logging.warning(f"Error occurred while launching the application: {e}")


@when(u'I am on the main page of the application')
def step_impl(context):
    try:
        welcome_text = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, locators.welcome_text_xpath)))
        text1 = welcome_text.text
        logging.info(f"Clicked on {text1}")
    except Exception as e:
        logging.error(f'Error while navigating to the main page: {e}')

@then(u'I enter my username and password')
def step_impl(context):
    try:
        # username = find_element(context, Locators.user_name_xpath)
        username = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, locators.user_name_xpath)))
        logging.info('clicked on user input field')
        username.clear()
        logging.info(f"Username entered: Venkatesh")
        username.send_keys("venkatesh")
        logging.info(f'Entered username: venkatesh')
        #

        # Wait for the password field to be visible
        password = find_element(context, locators.pasword_xpath)
        # password = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.password_xpath)))
        password.clear()
        logging.info('clicked on password field')
        password.send_keys("Test@12345")
        logging.info(f"Password entered: Test@12345")


    except Exception as e:
        logging.error(f'Error clicking entering username and password: {e}')


@when(u'I enter "{username}" and "{password}"')
def step_impl(context, username, password):
    try:
        # USERNAME INPUT FIELD
        user_name = find_element(context, locators.user_name_xpath)
        user_name.clear()
        logging.info("Clicked on username input field.")
        user_name.send_keys(username)
        logging.info(f"Username entered: {username}")

        # PASSWORD INPUT FIELD
        pass_word = find_element(context, locators.pasword_xpath)
        pass_word.clear()
        logging.info("Clicked on password input field.")
        pass_word.send_keys(password)
        logging.info(f"Password entered: {password}")
    except Exception as e:
        logging.error(f'Error to click entering username and password: {e}')


@then(u'click on sign-in button')
def step_impl(context):
    try:
        sign_in_button = find_element(context, locators.sign_in_xpath)
        sign_in_button.is_selected()
        logging.info("Clicked on Sign-in button")
        sign_in_button.click()
    except Exception as e:
        logging.error(f'Error clicking Sign-in button: {e}')

@then(u'I should redirect to home screen of the application')
def step_impl(context):
    try:
        orders_page = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, locators.orders_xpath)))
        location1 = orders_page.text
        logging.info(f"Welcome to: {location1}")
    except Exception as e:
        logging.error(f'Error navigating to home screen: {e}')


