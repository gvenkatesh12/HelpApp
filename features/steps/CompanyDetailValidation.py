import logging
import time
import os
import sys
from behave import *
from appium import webdriver as appiumwebdriver
from typing import Any, Dict
from selenium import webdriver
from selenium.common import TimeoutException
from details import *
# from tensorflow import tf

from log_msg import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as seleniumwebdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from log import *
from Locators import *
# from Locators import Locators
import json

import sqlite3


# Configure logging
configurator = LogConfigurator()
#
# def fetch_element_text(driver, xpath, element_name):
#     """Helper function to fetch and log the text of an element identified by its XPath."""
#     try:
#         element = WebDriverWait(driver, 20).until(
#             EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
#         )
#         text = element.text
#         logging.info(f"{element_name}: {text}")
#         return text
#     except Exception as e:
#         logging.error(f"Error while fetching {element_name}: {e}")
#         return None
#
# def profile_Details(context):
#     try:
#         context.details = {
#
# # --------------------------------------------------------------------------------------------------------------------------#
#             "Company": fetch_element_text(context.driver, locators.company_xpath, "Company"),
#             "Name": fetch_element_text(context.driver,  locators.Name_xpath, "Name"),
#             "Role": fetch_element_text(context.driver, locators.Role_xpath, "Role"),
#             "Status": fetch_element_text(context.driver, locators.Status_xpath, "Status"),
#             "Email": fetch_element_text(context.driver, locators.Email_xpath, "Email"),
#             "Mobile": fetch_element_text(context.driver, locators.Mobile_xpath, "Mobile"),
#             "Notifications": fetch_element_text(context.driver, locators.Notifications_xpath, "Notifications"),
#             "Created On": fetch_element_text(context.driver, locators.Created_On_xpath, "Created On")
#         }
#     except Exception as e:
#         logging.error(f"Error while retrieving profile details: {e}")
#
# @when(u'I click to profile button')
# def step_impl(context):
#     try:
#         profile_button_click = WebDriverWait(context.driver, 20).until(
#             EC.element_to_be_clickable((AppiumBy.XPATH, locators.profile_Button_xpath))
#         )
#         profile_button_click.click()
#         logging.info("Clicked profile button successfully!")
#     except Exception as e:
#         logging.error(f"Error while clicking profile button: {e}")
#
# @then(u'I Getting the company details')
# def step_impl(context):
#     try:
#         profile_Details(context)
#         details = context.details
#
#         # Check if any detail is None and log specific detail messages
#         for key, value in details.items():
#             if value is None:
#                 raise ValueError(f"Failed to fetch {key} details.")
#
#         # Database operations
#         with sqlite3.connect('company_details1.db') as conn:
#             cursor = conn.cursor()
#
#             cursor.execute(Tables.profile_table_query)
#             time.sleep(10)
#
#             values = (
#                 details['Company'],
#                 details['Name'],
#                 details['Role'],
#                 details['Status'],
#                 details['Email'],
#                 details['Mobile'],
#                 details['Notifications'],
#                 details['Created On']
#             )
#             time.sleep(5)
#             cursor.execute(Insert.profile_insert_query, values)
#             conn.commit()
#         back_button = find_element(context,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView")
#         back_button.click()
#         logging.info(f'clicked on back button')
#
#         logging.info("Company details stored in SQLite database successfully.")
#     except sqlite3.Error as e:
#         logging.error(f"SQLite error occurred: {e}")
#     except ValueError as e:
#         logging.error(f"Data error: {e}")
#     except Exception as e:
#         logging.error(f"An error occurred: {e}")
#

        #---------------------Chrome browser-----------------------------#


current_file_name = os.path.basename(__file__)
new_file_name = os.path.splitext(current_file_name)[0] + ".png"
configurator = LogConfigurator()
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": Locators.pdf_dir,  # Set download directory
    "download.prompt_for_download": False,   # Disable download prompt
    "plugins.always_open_pdf_externally": True  # Disable Chrome PDF viewer
})
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
obj = Details()
user_email, user_mobile, user_username, user_name = obj.details()
execution_count = 0


# firefox_options.add_argument("--headless")

def find_element(context, xpath):
    return WebDriverWait(context.driver, 10, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))



@given(u'I launch chrome browser')
def launchBrowser(context):
    try:
        configurator.before_all(context)
        sys.path.append(os.getcwd())
        context.driver = webdriver.Chrome(options=chrome_options)
        # # context.driver = webdriver.Remote(command_executor='http://43.204.211.229:4444/wd/hub', options=chrome_options)
        context.driver.implicitly_wait(10)
        logging.info(Info.chrome)
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.chrome.format(str(e)))
        context.driver.close()
        raise Exception from e

@when(u'open oms home page')
def loginPage(context):
    try:
        context.driver.maximize_window()
        context.driver.get(Locators.url)
        logging.info(Info.open_oms_home_page.format(Locators.url))
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.open_oms_home_page.format(str(e)))
        context.driver.close()
        raise Exception from e


@when(u'Click on Login Button')
def clicklogin(context):
    try:
        time.sleep(3)
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.home_login_button_xpath))).click()

        logging.info(Info.click_login_button)
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.click_login_button.format(str(e)))
        context.driver.close()
        raise Exception from e

@when(u'Enter username "{username}" and password "{password}" for "{user}" user')
def step_impl(context, username, password, user):
    try:
        context.driver.find_element(by=By.XPATH, value=Locators.login_username_textbox_xpath).send_keys(username)
        context.driver.find_element(by=By.XPATH, value=Locators.login_password_textbox_xpath).send_keys(password)
        logging.info(Info.login_credentials.format(username, password))
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.login_credentials.format(str(e)))
        context.driver.close()
        raise Exception from e



@when('Click the Sign In button')
def step_impl(context):
    try:
        if context.driver.find_element(by=By.XPATH, value='/html/body/app-root/app-sign-in/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div[3]/button').click():
            time.sleep(2)
            logging.info(Info.click_signin_button)
            time.sleep(5)
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.click_signin_button.format(str(e)))
        context.driver.close()
        raise Exception from e


@when(u'show the success message')
def step_impl (context):
    try:
        success = context.driver.find_element(By.XPATH, Locators.success_msg)
        mesg= success.text
        logging.info(f'sucess {mesg}')
        logging.info(Info.login_success_message)
        time.sleep(5)
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.login_success_message.format(str(e)))
        context.driver.close()
        raise Exception from e


@then(u'Navigate to Onboarding tab  --> Registration tab --> Partners tabs')
def step_impl(context):
    try:
        context.driver.find_element(by=By.XPATH, value=Locators.Hamburger_path).click()
        context.driver.find_element(by=By.XPATH, value='//*[@id="navbar-nav"]/li[4]/a/span/span/span').click()
        context.driver.find_element(by=By.XPATH, value="//span[contains(text(),'Registration')]").click()
        time.sleep(30)
        # Click on Partners tab
        element = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-tab-label-3-1"]/div')))
        element.click()
        logging.info('Clicked on Partners tab')

        # Perform search for company (example 'venkatesh')
        search_xpath = '//*[@id="mat-input-19"]'  # Replace with actual search input XPath
        search_element = context.driver.find_element(By.XPATH, search_xpath)
        search_element.click()
        search_element.send_keys('venkatesh')

        logging.info('Performed search in Partners tab')


        logging.info(f'waiting!!!!!!!!')


    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(f"Error navigating to Partners tab: {str(e)}")
        context.driver.close()
        raise Exception from e

@then(u'In partners tab search for the company that retrived from mobile application')
def step_impl(context):
    try:
        logging.info("waitong")
    except Exception as e:
        time.sleep(1)
        context.driver.save_screenshot(f"./{new_file_name}")
        logging.error(Error.search_company_in_partners_tab.format(str(e)))
        context.driver.close()
        raise Exception from e


@then(u'get the company details from the web')
def step_impl(context):

    raise NotImplementedError(u'STEP: Then get the company details from the web')


@then(u'the company details retrieved from the mobile application should match the company details with web')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the company details retrieved from the mobile application should match the company details with web')
