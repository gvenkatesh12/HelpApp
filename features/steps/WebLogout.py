import logging
import sys
import os
import time
from appium import webdriver as appiumwebdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions
from selenium import webdriver
from Locators import *
from log import *

cap = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "sdk_gphone_x86",
    "app": r"C:\Users\Manik\Downloads\SC Partner.apk",
    "automationName": "UiAutomator2",
    "resetKeyboard": True
}
configurator = LogConfigurator()

@given(u'I am on the main page of the application')
def step_impl(context):
    try:
        configurator.before_all(context)
        sys.path.append(os.getcwd())
        context.driver = appiumwebdriver.Remote("http://localhost:4723/wd/hub",
                                                options=AppiumOptions().load_capabilities(cap))
        # time.sleep(2)
        logging.info(f'application sucessfully!! opened')

    except Exception as e:
        logging.warning(f"Error: {e}")


@when(u'I enter my username and password')
def step_impl(context):
    username = find_element(context, Locators.user_name_xpath)
    # username = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.user_name_xpath)))
    username.click()
    logging.info('clicked on user input field')
    logging.info(f"Username entered: {username}")
    username.send_keys("venkatesh")
    logging.info(f'Entered username: venkatesh')

    # Wait for the password field to be visible
    password = find_element(context, Locators.pasword_xpath)
    # password = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.password_xpath)))
    password.click()
    logging.info('clicked on password field')
    logging.info(f"Password entered: {password}")
    password.send_keys("Test@12345")
    logging.info(f'Entered password: Test@12345')


@when(u'I click on the sign-in button')
def step_impl(context):
    try:
        sign_in_button = find_element(context, Locators.sign_in_xpath)
        # sign_in_button = WebDriverWait(context, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, Locators.sign_in_xpath)))
        sign_in_button.click()
        logging.info("Clicked on Sign-in button")

    except Exception as e:
        logging.error(f'Error clicking Sign-in button: {e}')


@then(u'I click on logout button')
def step_impl(context):
    try:
        # logout =find_element(context, Locators.logout_button_xpath)
        logout = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, Locators.logout_button_xpath)))
        logout.click()
        logging.info("Logged out successfully!")
    except Exception as e:
        logging.error(f'Error while logging out: {e}')


@then(u'I should redirect to the login page')
def step_impl(context):
    try:

        welcome_text = WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, Locators.welcome_text_xpath)))
        text1 = welcome_text.text
        logging.info(f"Clicked on {text1}")
    except Exception as e:
        logging.error(f'Error response in main page{e}')





















































































# Assuming proper logging configuration and imports are done.

# Define a WebDriverWait instance for reuse
#
# @given(u'I am on the main page of the application')
# def step_impl(context):
#     try:
#         context.driver = appiumwebdriver.Remote("http://localhost:4723/wd/hub",
#                                                 options=AppiumOptions().load_capabilities(cap))
#         logging.info(f'Application opened successfully!')
#
#     except Exception as e:
#         logging.error(f"Error opening application: {e}")
#
# @when(u'I enter my username and password')
# def step_impl(context):
#     try:
#         username = find_element(context, Locators.user_name_xpath)
#         # username = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.user_name_xpath)))
#         username.click()
#         logging.info('clicked on user input field')
#         username.send_keys("venkatesh")
#         logging.info(f'Entered username: venkatesh')
#
#         # Wait for the password field to be visible
#         password = find_element(context, Locators.pasword_xpath)
#         # password = WebDriverWait(context, 20).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.password_xpath)))
#         password.click()
#         logging.info('clicked on password field')
#         password.send_keys("Test@12345")
#         logging.info(f'Entered password: Test@12345')
#
#         # username = WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.user_name_xpath)))
#         # logging.info(f'clicked on username field')
#         # username.click()
#         # username.send_keys("venkatesh")
#         # logging.info(f'Entered username:{username}')
#         #
#         #
#         # password = WebDriverWait(context,10).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.password_xpath)))
#         # password.click()
#         # password.send_keys("Test@12345")
#         # logging.info(f'Entered password:{password}')
#
#     except Exception as e:
#         logging.error(f"Error entering credentials: {e}")
#
# @when(u'I click on the sign-in button')
# def step_impl(context):
#     try:
#         sign_in_button = find_element(context, Locators.sign_in_xpath)
#         # sign_in_button = WebDriverWait(context, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, Locators.sign_in_xpath)))
#         sign_in_button.click()
#         logging.info("Clicked on Sign-in button")
#
#     except Exception as e:
#         logging.error(f'Error clicking Sign-in button: {e}')
#
# @then(u'I click on logout button')
# def step_impl(context):
#     try:
#         profile_Button = WebDriverWait(context, 20).until(EC.element_to_be_clickable((AppiumBy.XPATH, Locators.profile_xpath)))
#         logging.info(f"clicked to profile button")
#         profile_Button.click()
#         time.sleep(2)
#
#
#         logout = WebDriverWait.until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.logout_button_xpath)))
#         logout.click()
#         logging.info(f'Logged out successfully!')
#
#     except Exception as e:
#         logging.error(f"Error logging out: {e}")
#
# @then(u'I should redirect to the login page')
# def step_impl(context):
#     try:
#         welcome_text = WebDriverWait(context, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, Locators.welcome_text_xpath)))
#         assert "Login" in welcome_text.text
#         logging.info(f"Redirected to login page")
#
#     except Exception as e:
#         logging.error(f'Error redirecting to login page: {e}')
