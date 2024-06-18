import time
from behave import *
from appium import webdriver as appiumwebdriver
from typing import Any, Dict
from selenium import webdriver as seleniumwebdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import json
import logging


def find_element(context, xpath):
    return WebDriverWait(context.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, xpath)))


def find_elements(context, xpath):
    return WebDriverWait(context.driver,20).until(EC.presence_of_all_elements_located((AppiumBy.XPATH, xpath)))


def find_element_web(context, xpath):
    return WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))


class locators:

    #LOGIN AND HOME PAGE

    welcome_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"
    user_name_xpath = ("//android.widget.EditText")
                       # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
    pasword_xpath ='(//android.widget.EditText)[2]'
                     # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    sign_in_xpath ='//android.view.ViewGroup[@content-desc="Sign in"]'
    invalid_username_or_password_text_xpath = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[5]")
    # logout_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
    logout_button_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]"

    profile_Button_xpath ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView"
    # COMPANY DETAIL
    company_navigation_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]"
    company_name_xpath = "//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView"
    orders_xpath ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
    # WEB XPATH
    Hamburger_path = "//button[@id='topnav-hamburger-icon']"
    on_boarding_menu_xpath = "//*[@id='navbar-nav']/li[6]/a"
    add_company_menu_xpath = '//*[@id="navbar-nav"]/li[6]/mat-nav-list/a[1]/span/i'
    search_input_xpath = "/html/body/app-root/app-companydetails/div/div/div/div/div[3]/div[1]/div/section/mat-form-field/div/div[1]/div[3]/input"

    #profile_details
    company_xpath = ("//android.widget.TextView[4]")
                     # "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]")
    Name_xpath = "//android.widget.TextView[6]"
    Role_xpath = "//android.widget.TextView[8]"
    Status_xpath = "//android.widget.TextView[10]"
    Email_xpath = "//android.widget.TextView[12]"
    Mobile_xpath = "//android.widget.TextView[14]"
    Notifications_xpath = "//android.widget.TextView[16]"
    Created_On_xpath = "//android.widget.TextView[18]"

    # company_Header_xpath = "/android.widget.TextView[3]"
    # Name_Header_xpath = "//android.widget.TextView[5]"
    # Role_Header_xpath = "//android.widget.TextView[7]"
    # Status_Header_xpath = "//android.widget.TextView[9]"
    # Email_Header_xpath = "//android.widget.TextView[11]"
    # Mobile_Header_xpath = "//android.widget.TextView[13]"
    # Notifications_Header_xpath = "//android.widget.TextView[15]"
    # Created_On_Header_xpath = "//android.widget.TextView[17]"

    #chrome details xpaths

import json
import os

import logging


class Locators:
    # # To download the invoice pdf
    # current_dir = os.getcwd()
    # print(f"Current working directory is: {current_dir}")
    # logging.info(f"Current working directory is: {current_dir}")
    # new_dir_name = "automation_pdf"
    # new_dir_path = os.path.join(current_dir, new_dir_name)
    # if not os.path.exists(new_dir_path):
    #     os.mkdir(new_dir_path)
    #     print(f"Directory '{new_dir_name}' created successfully.")
    #     logging.info(f"Directory '{new_dir_name}' created successfully.")
    # else:
    #     print(f"Directory '{new_dir_name}' already exists.")
    #     logging.info(f"Directory '{new_dir_name}' already exists.")

    # Get the user's home directory
    home_dir = os.path.expanduser('~')
    pdf_dir = os.path.join(home_dir, 'common_pdfs')
    if not os.path.exists(pdf_dir):  # Create the directory if it doesn't exist
        os.makedirs(pdf_dir)

    # Get the data, user details and the order id detail from Json file
    file_name = "omsuserdata.json"
    dir = os.getcwd()
    # Loop through all files in the directory and its subdirectories to find omsuserdata.json file
    for root, dirs, files in os.walk(dir):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            f = open(file_path, "r")

    # WHATSAPP AUTOMATION RESPONSE SCREENS TEXT TELUGU
    welcome_screen_response_telugu = "Servcrust కి స్వాగతం"
    location_screen_response_telugu = "show దయచేసి GPS స్థానాన్ని పంపండి"
    product_type_response_telugu = "కంకర రకాన్ని ఎంచుకోండి"
    quantity_type_response_telugu = "కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT)"

    # WHATSAPP AUTOMATION RESPONSE SCREENS TEXT ENGLISH
    welcome_screen_response_english = "Servcrust కి స్వాగతం"
    location_screen_response_english = "Please share the Delivery Location (GPS)"
    product_type_response_english = "Select Aggregate Type"
    quantity_type_response_english = "Select Quantity (CFT)"
    payment_response_english = 'Pay On Delivery'
    click_to_select = "Click to select"



    jsontext = f.read()
    data = json.loads(jsontext)
    url = data['url']
    super_admin_username = data['super_admin_username']
    super_admin_password = data['super_admin_password']
    admin_username = data['admin_username']
    admin_password = data['admin_password']
    executive_username = data['executive_username']
    executive_password = data['executive_password']
    onboarding_username = data['onboarding_username']
    onboarding_password = data['onboarding_password']
    accountant_username = data['accountant_username']
    accountant_password = data['accountant_password']
    operations_head_username = data['operationshead_username']
    operations_head_password = data['operationshead_password']
    support_manager_username = data['supportmanager_username']
    support_manager_password = data['supportmanager_password']
    support_executive_username = data['supportexecutive_username']
    support_executive_password = data['supportexecutive_password']
    finance_head_username = data['financehead_username']
    finance_head_password = data['financehead_password']
    orderid = data['order_id']
    product_search = data['product_search']
    quantity_search = data['quantity_search']
    miscellaneous_search = data['miscellaneous_search']
    add_stock = data['add_stock']
    database = 'mydatabase.db'

    # login page objects
    privacy_policy_link_xpath = "/html/body/app-root/app-home/div/footer/div/div/div[2]/a[1]"
    privacy_policy_page_xpath = '//*[@id="services"]/div/div/div/div/h1'
    privacy_policy_page_text_xpath = '//*[@id="services"]/div/div/div'
    terms_n_conditions = "/html/body/app-root/app-home/div/footer/div/div/div[2]/a[2]"
    terms_text_xpath = '//*[@id="page5R_mcid0"]/span[1]'
    refund_policy_link_xpath = "//a[.='Refund Policy']"
    refund_policy_page_xpath = "//a[.='Refund Policy']"
    refund_policy_page_text_xpath = "//div[@class='col-lg-12']"
    login_username_textbox_xpath = "//input[@id='email']"
    login_password_textbox_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@type='submit']"
    home_login_button_xpath = "//a[normalize-space()='Login']"                                                   #'//*[@id="mainNavigation"]/ul/li[6]/a'
    Hamburger_path = "//span[contains(@class,'hamburger-icon')]"

    success_msg = "/html/body/app-root/ng-toast/div/div/div[2]/p[2]"
    frgt_username_text_xpath = "//*[@id='email']"
    invalidcred_msg = '/html/body/app-root/lib-ng-toast/div/div[2]/p[2]'

    # common objects for the Web application after login
    profile_button = '//*[id="layout-wrapper"]/app-header/div/div/div[2]/div[3]/div/a[1]'
    logout_button = "//a[@class='dropdown-item'][2]"
    navbar = "//*[@id='layout-wrapper']/app-topnavbar/div/div[1]/div[1]/a[2]/span[1]/img"

    # Dashboard
    dashboard_text_xpath = "//h4[contains(text(),'Dashboard')]"
    dashboard_order_status_text = "//div[@class='card-body p-0']/div[1]/div/div/div/div/h2/span"
    dashboard_orders = "//div[@class='card-body p-0']/div[1]/div[{}]/div/div/div/h2/span"
    dashboard_sales_graph = "(//*[local-name()='g' and @class= 'apexcharts-datalabels'])[3]//*[local-name()='g']//*[name()='rect']"
    sales_graph_loop = "(//*[local-name()='g' and @class= 'apexcharts-datalabels'])[3]//*[local-name()='g'][{}]//*[name()='rect']"
    graph_data = "//div[@class='apexcharts-tooltip apexcharts-theme-light apexcharts-active']"
    graph_order_date = "//*[@class='apexcharts-tooltip apexcharts-theme-light']/div[@class='apexcharts-tooltip-title']"
    graph_orders_value = "//*[contains(@class,'apexcharts-tooltip apexcharts-theme-light apexcharts-active')]/div[{}]/div/div[1]/span[2]"
    graph_orders_text = "//*[contains(@class,'apexcharts-tooltip apexcharts-theme-light apexcharts-active')]/div[{}]/div/div[1]/span[1]"
    user_name_text_xpath = "//*[@id='page-header-user-dropdown']/span/span/span[1]"
    user_text_xpath = "//*[@id='page-header-user-dropdown']/span/span/span[2]"
    dashboard_Placed_text_xpath = "//div/div/div/div[2]/div/div/div/div/div[1]/div/h5"
    dashboard_Placed_orders_count = "//div/div/div/div[2]/div/div/div/div/div[1]/div/div/div[2]/h2/span"
    dashboard_Confirmed_text_xpath = "//div/div/div/div[2]/div/div/div/div/div[2]/div/h5"
    dashboard_Confirmed_orders_count = "//div/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/h2/span"
    dashboard_Dipatched_text_xpath = "//div/div/div/div[2]/div/div/div/div/div[3]/div/h5"
    dashboard_Dipatched_orders_count = "//div/div/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/h2/span"
    dashboard_Delivered_text_xpath = "//div/div/div/div[2]/div/div/div/div/div[4]/div/h5"
    dashboard_Delivered_orders_count = "//div/div/div/div[2]/div/div/div/div/div[4]/div/div/div[2]/h2/span"
    dashboard_Quantity_sold_in_tons_text_xpath = "//div/div/div/div[3]/div[1]/div/div/div[1]/div/div/div/div[1]/p"
    dashboard_Quantity_sold_in_tons_value = "//div/div/div/div[3]/div[1]/div/div/div[1]/div/div/div/div[1]/h2/span"
    dashboard_Companies_onBoard_text_xpath = "//div/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/p"
    dashboard_Companies_onBoard_value = "//div/div/div/div[3]/div[1]/div/div/div[2]/div/div/div/div[1]/h2/span"
    dashboard_Others_text_xpath = "//div/div/div/div[3]/div[1]/div/div/div[3]/div/div/div/div[1]/p"
    dashboard_Others_value = "//div/div/div/div[3]/div[1]/div/div/div[3]/div/div/div/div[1]/h2/span"
    dashboard_UPI_text_xpath = "//div/div/div/div[3]/div[1]/div/div/div[4]/div/div/div/div[1]/p"
    dashboard_UPI_value = "//div/div/div/div[3]/div[1]/div/div/div[4]/div/div/div/div[1]/h2/span"
    dashboard_POD_text_xpath = "//div/div/div/div[3]/div[1]/div/div/div[6]/div/div/div/div[1]/p"
    dashboard_POD_value = "//div/div/div/div[3]/div[1]/div/div/div[6]/div/div/div/div[1]/h2/span"
    dashboard_Cancelled_by_admin_text_xpath = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[1]"
    dashboard_Cancelled_by_admin_value = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[1]/b"
    dashboard_Cancelled_by_customer_text_xpath = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[2]"
    dashboard_Cancelled_by_customer_value = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[2]/b"
    dashboard_Cancelled_by_system_text_xpath = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[3]"
    dashboard_Cancelled_by_system_value = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[3]/b"
    dashboard_Total_value = "//div/div/div/div[3]/div[4]/div[3]/div/div/div/h6[4]/b"

    ### Table attributes
    dropdown = "//mat-select"
    master_dropdown = "//*[@class='page-title-right']//mat-select"
    dropdown_arrow = "//mat-select/div/div[2]"
    dropdown_options = "//mat-option"
    dropdown_options_loop = "//mat-option[{}]"
    table_rows = "//mat-table//mat-row"
    table_columns = "//mat-table/mat-header-row/mat-header-cell"
    table_row_loop = '//mat-row[{}]'
    table_cell_loop = '//mat-row[{}]/mat-cell[{}]'
    form_cell_loop = '//tbody/tr[{}]/td[{}]'
    form_row_loop = '//tbody/tr[{}]/td[1]'
    form_row_loop_2column = '//tbody/tr[{}]/td[2]'

    # Menu objects
    dashboard_menu_path = '//*[@id="navbar-nav"]/li[2]/a'
    oms_menu_path = '//*[@id="navbar-nav"]/li[3]/a'
    oms_online_sales_tab_xpath = '//a[@routerlink="/orders"]'
    stock_menu_path = '//*[@id="navbar-nav"]/li[5]/a'
    add_user_menu_xpath = "//div/ul/li[@class='nav-item ng-star-inserted'][1]/a"
    on_boarding_menu_xpath = "//*[@id='navbar-nav']/li[4]/a"
    registration_menu_xpath = '//*[@id="navbar-nav"]/li[4]/mat-nav-list/a[3]/span/span'
    accounts_menu_xpath = "//*[@id='navbar-nav']/li[7]/a"
    accountant_account_menu_xpath = "/html/body/app-root/app-order/div/app-topnavbar/div/div[1]/div[2]/div/ul/li[6]/a"
    request_for_settle_page = '//*[@id="navbar-nav"]/li[7]/mat-nav-list/a[3]'
    pay_in_page = "//*[.=' Pay In']"
    support_menu_xpath = "//*[@id='navbar-nav']/li[8]/a"
    service_ticket_menu_xpath = '//*[@id="navbar-nav"]/li[8]/mat-nav-list'
    rewards_menu_path = "//a[@routerlink='/rewards']"
    cost_master_menu = "//*[@id='navbar-nav']/li[7]/mat-nav-list/a[1]"
    accountant_cost_master_menu = "/html/body/app-root/app-order/div/app-topnavbar/div/div[1]/div[2]/div/ul/li[6]/mat-nav-list/a[1]"
    stock_page_but_Xpath = "//a[@routerlink='/stock']"
    company_page_menu = "//span[contains(text(),'New Company')]"
    vehicales_admin_page = "//a[@routerlink='/vehicles']"
    registration_partners_tab ='//*[@id="mat-tab-label-3-1"]'
    registration_servcrust_tab= '//*[@id="mat-tab-label-3-0"]'
    # table
    partner_Name ='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[1]'
    partner_status ='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[2]'#mobile notification
    partner_Role ='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[3]'
    partner_email='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[4]'
    partner_phone='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[5]'
    partner_company='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[6]'
    partner_notifyneworders='//*[@id="mat-tab-content-1-1"]/div/div/div/div/mat-table/mat-row[1]/mat-cell[7]'

    partner_Enabled='//*[@id="mat-mdc-slide-toggle-17-button"]/div[2]/div/div[3]/svg[1]'





    orderstatus_text_path = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[10]/span'
    confirm_button = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[12]/button[1]/img'
    oms_button = '//*[@id="layout-wrapper"]/app-header/div/div/div[2]/div[2]/button'

    # oms page objects
    oms_search_pane = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/section/mat-form-field/div/div[1]'
    order_id_search = "//input[@formcontrolname='id']"
    oms_nav_pane = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/section/mat-paginator/div/div/div[2]'
    oms_number_pages = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/section/mat-paginator/div/div/div[1]/div[1]'
    oms_pages = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/section/mat-paginator/div/div/div[1]/div[2]'
    oms_ranges = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/section/mat-paginator/div/div/div[2]/div'
    oms_search_button = "//mat-card-content/div/button[1]"
    oms_clear_button = "//mat-card-content/div/button[2]"
    oms_columns = "//div/table/thead/tr/th"
    oms_rows = "//div/table/tbody/tr"
    order_status = "//table/tbody/tr[1]/td[9]"
    order_created_on = "//table/tbody/tr[1]/td[8]"
    order_status_tab = "//mat-label[contains(.,'Order Status')]"
    payment_status_tab = "/html/body/app-root/app-order/div/div/div/div/div[1]/div/div/div/form/mat-card/mat-card-content/div/mat-form-field[5]/div[1]/div/div[1]/div[2]/label/mat-label"
    status_is_placed = "//mat-option[@value='PLACED']"
    status_is_paid = "//mat-option[@value='paid']"

    # company page
    scroll_down = "window.scrollTo(50,700);"
    scroll_up = "window.scrollTo(0, document.body.scrollTop);"
    scroll_middle = "window.scrollTo(0, document.body.scrollHeight / 5);"
    company_name_text_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[3]/div[1]/div/div[2]/mat-table/mat-row[1]/mat-cell[2]'
    company_prefix_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[3]/div[1]/div/div[2]/mat-table/mat-row[1]/mat-cell[5]'
    quantity_operational_text_xpath = "//div/div/div/div/div[2]/div/div/div[2]/form/mat-horizontal-stepper/div/div[2]/div[1]/div[1]/div/mat-form-field[6]/div[1]/div/div[2]/mat-select/div/div[1]/span/span"
    company_details_xpath = "//div/table/tbody/tr"
    company_name_xpath = "//input[@placeholder='Company Name']"
    company_status_xpath = "//*[@id='mat-select-value-3']"
    company_active_button_xpath = "//mat-option[1]"
    company_license_no_xpath = "//input[@placeholder='License No']"
    company_GSTIn_xpath = "//input[@placeholder='GSTIn']"
    company_PAN_no_xpath = "//input[@placeholder='Pan Number']"
    company_QuantityOperational_xpath = '//mat-select[@formcontrolname="operationalQty"]'
    company_list_row = '//*[@id="layout-wrapper"]/div/div/div/div[3]/div[1]/div/div[2]/mat-table/mat-row[1]'
    company_details_table = '//*[@id="layout-wrapper"]/div/div/div/div[3]/div[2]/div/div[2]/div/table'
    company_details_rows = 'tr'
    company_details_data = 'td'
    company_Ton_xpath = '//mat-option[@value="TON"]'
    company_email_xpath = "//input[@placeholder='E-mail']"
    company_mobile_no_xpath = "//input[@placeholder='Contact']"
    company_details_next_button1_xpath = "//div[@id='cdk-step-content-0-0']//button[@type='button'][normalize-space()='Next']"
    company_state_button_xpath = "//mat-select[@formcontrolname='state']"
    company_state_selection_xpath = "//mat-option[2]"
    company_district_button_xpath = "//mat-select[@formcontrolname='district']"
    company_district_selection_xpath = "//mat-option[4]"
    company_city_button_xpath = "//input[@formcontrolname='city']"
    company_building_no_xpath = "//input[@formcontrolname='addressLine1']"
    company_street_no_xpath = "//input[@formcontrolname='addressLine2']"
    company_PINCODE_xpath = "//input[@formcontrolname='pinCode']"
    company_latitude_xpath = "//input[@formcontrolname='compAddressCoordinatesLat']"
    company_longitude_xpath = "//input[@formcontrolname='compAddressCoordinatesLng']"
    company_details_next_button2_xpath = "//*[@id='cdk-step-content-0-1']/div[3]/button[2]/i"
    company_details_next_button3_xpath = "//*[@id='cdk-step-content-0-2']/div/div/button[2]/i"
    company_details_next_button4_xpath = "//*[@id='cdk-step-content-0-3']/div[3]/button[2]/i"
    company_details_submit_button_xpath = "//div[2]/div[4]/div/button[2]"
    company_search_button_xpath = "//div[3]/div[1]/div/section/mat-form-field/div[1]/div/div[2]/input"
    company_mobile_verification = "//tbody/tr[6]/td"
    toggle_button = "//div[@class='mdc-switch__icons ng-star-inserted']"
    next_button = "//button[@aria-label='Next page']"
    first_page_button = "//mat-paginator/div/div/div[2]/button[1]"
    server_side_pagination_last = '//*[@id="radioBtn"]/button[4]'
    server_side_pagination_next = '//*[@id="radioBtn"]/button[3]'
    total_count = "//mat-paginator/div/div/div[2]/div"

    # confirming an order
    search_box_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/div/form/mat-card/mat-card-content/div/mat-form-field[3]/div/div[1]'
    search_placed_order_xpath = '//*[@id="mat-option-4"]/span'
    search_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/div/form/mat-card/mat-card-content/div/button[1]'
    placed_orderid = 'APWG8-20230216-1'
    confirm_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[12]/button[1]'

    # ----------------dispatch date---------------------------------------
    dispatch_xpath = '//*[@id="mat-dialog-0"]/app-confirm-dialog/div/div/div[1]/div/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button'
    dispatch_year = '//*[@id="mat-datepicker-2"]/mat-calendar-header/div/div/button[1]'
    dispatch_year1 = '//*[@id="mat-datepicker-2"]/div/mat-multi-year-view/table/tbody/tr[1]/td[2]/button'
    dispatch_month = '//*[@id="mat-datepicker-2"]/div/mat-year-view/table/tbody/tr[2]/td[1]/button'
    dispatch_day = '//*[@id="mat-datepicker-2"]/div/mat-month-view/table/tbody/tr[2]/td[5]/button'

    # stock_page web elements
    stock_text_xpath = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/h4'
    pagination_button_locator = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div/div/mat-paginator/div/div/div[2]/button[3]'
    verify_admin_page = '//*[@id="page-header-user-dropdown"]/span/span/span[2]'
    select_company_box_xpath = "//mat-select/div"
    stock_page_search = "//div/div/div/mat-form-field/div[1]/div/div[2]/input"
    pagenator_element_xpath = 'div.mat-paginator-range-label'
    last_page_but_xpath = "//button[@aria-label='Last page']"
    company_listbox_xpath = "//mat-option"
    product_search_textfield_xpath = '//*[@id="mat-input-2"]'
    header_row_xpath = "//mat-table//mat-header-row"
    header_cells_xpath = "mat-header-cell"
    server_side_pagination_first = "//*[@id='radioBtn']/button[1]"
    add_stock_button = "//button[normalize-space()='Add Stock']"
    select_a_product_button = '//mat-select[@formcontrolname="productId"]'
    quantity_in_tons = "//input[@placeholder='Quantity']"
    add_stock_save_button = "//app-add-manual/div[2]/button[2]"
    add_stock_close_button = "//app-add-manual/div[2]/button[1]"
    total_items_per_page = "//mat-paginator/div/div/div[2]/div"
    items_per_page_click = "/html/body/app-root/app-sign-up/div/div/div/div/div[2]/mat-tab-group/div/mat-tab-body[2]/div/div/div/section/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select"
    item_15_xpath = "/html/body/div[3]/div[2]/div/div/div/mat-option[3]"

    first_page_button_xpath_admin = "/html/body/app-root/app-manual-stock/div/div/div/div/div[2]/div/div/div/mat-paginator/div/div/div[2]/button[1]"
    first_page_button_xpath_superadmin = "//div[@class = 'mat-paginator-container']/div/button[1]"

    next_page_button_xpath_superadmin = "/html/body/app-root/app-stock/div/div/div/div/div[2]/div/div/div/div/mat-paginator/div/div/div[2]/button[3]"

    next_page_button_xpath_admin = "//*[@id='layout-wrapper']/div/div/div/div[2]/div/div/div/mat-paginator/div/div/div[2]/button[3]"
    text_cft_ton_xpath = "//mat-table//mat-header-row//mat-header-cell[2]"

    # logout objects
    logout_xpath = "//button[@class='btn shadow-none']"
    logout_button_xpath = "//span[normalize-space()='Sign Out']"

    # Costmaster
    cost_master_company = "//mat-select[@formcontrolname='selectedCompany']"
    cost_master_calender = "//button[@aria-label='Open calendar']"
    cost_master_months = "//mat-calendar-header/div/div/button[1]/span[2]"
    cost_master_dates_year = "//mat-multi-year-view/table/tbody/tr/td"
    cost_master_dates_month = "//mat-year-view/table/tbody/tr/td"
    cost_master_dates_day = "//mat-month-view/table/tbody/tr/td"
    cost_master_order_pane_search = '//div/div/div[3]/input[@placeholder="Search..."]'
    cost_master_search = "//div/div/div/form/mat-card/mat-card-content/div/button[1]/span[2]"
    cost_master_calculation = "//tbody[@role='rowgroup']/tr[{}]//table"
    cal_row_tables = "//tbody[@role='rowgroup']/tr[{}]//div/table"
    calculation_values = "//tbody[@role='rowgroup']/tr[{}]//div[{}]/table/tr[2]/td"

    # Request for settle
    request_for_settle_aggregate = "//a[@href='#developers']"
    request_for_settle_logistics = "//a[@href='#designers']"
    request_for_settle_search = "//button[@class='btn btn-primary shadow']"
    request_for_settle_select_status = "//mat-select[@formcontrolname='payStatus']"
    request_for_settle_select_company = "//mat-select[@formcontrolname = 'selectedCompany']"
    request_for_settle_payout = "//mat-option[@value='payOut']"
    request_for_settle_values = "//div[@role='tabpanel']//h5"
    request_for_settle_text_value = "//div[@role='tabpanel']/div/div[{}]/div/h5"
    request_for_settle_value = "//div[@role='tabpanel']/div/div[{}]/div/div/div/h2/span"
    ready_for_payout_count = '//*[@id="developers"]/div/div[2]/div/div/div[2]/h2/span'
    indian_mines_company = "//span[text()='Indian Mines - TS15_12']"

    # Pay In
    pay_in_order_type = "//mat-select[@formcontrolname='orderType']"
    pay_in_settled_orders = "//mat-option[@value='settledOrders']"

    # on-boarding page objects
    servcrust_tab = "//span[contains(text(),'ServCrust')]"
    all_user_search = "//mat-form-field/div[1]/div/div[2]/input"
    email_verification = "//mat-table/mat-row[1]/mat-cell[4]"
    mobile_verification = "//mat-table/mat-row[1]/mat-cell[5]"
    admin_tab_xpath = "/html/body/app-root/app-sign-up/div/div/div/div/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[2]"
    others_tab_xpath = "/html/body/app-root/app-sign-up/div/div/div/div/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[3]"

    # all-user details page
    all_user_details_text_xpath = "//*[@id='layout-wrapper']/div/div/div/div[1]/div/div/h4"
    add_user_button_xpath = "/html/body/app-root/app-sign-up/div/div/div/div/div[1]/div/div/button"
    add_new_user_button_xpath = "/html/body/app-root/app-dashboard-new/div/app-topnavbar/div/div[1]/div[3]/div/ul/li[7]/a"
    add_user_text_xpath = "/html/body/div[3]/div[2]/div/mat-dialog-container/app-add-signup/h2"
    add_user_select_company = "//mat-select[@id='companyId']"
    email_xpath = "//*[@id='email']"
    email_error_msg_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-add-signup[1]/div[1]/form[1]/mat-form-field[2]/div[2]/div[1]"
    mobile_xpath = "//*[@id='mobile']"
    mobile_error_msg_xpath = "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/div[1]/div[1]/app-add-signup[1]/div[1]/form[1]/mat-form-field[3]/div[2]/div[1]"
    add_user_username_xpath = "//input[@placeholder='User Name']"
    add_user_name_xpath = "//input[@formcontrolname='name']"
    add_user_admin_role_select_xpath = '/html/body/div[3]/div[2]/div/mat-dialog-container/app-add-signup/div[1]/form/mat-form-field[6]/div/div[1]/div[3]/mat-select'
    add_user_role = "/html/body/div[3]/div[4]/div/div/mat-option"
    add_user_close_button = "//div/div/app-add-signup/div[2]/button[1]"
    add_user_admin_success_msg = "/html/body/app-root/ng-toast/div/div/div[2]/p[1]"
    add_user_admin_search_box = "//div/div[2]/input[@placeholder='Search...']"

    superadmin_role_select_xpath = "/html/body/div[3]/div[4]/div/div/div/mat-option"
    admin_role_select_xpath = "//mat-option"
    admin_button_select = "//div/div/div/div/div[2]/mat-tab-group/mat-tab-header/div/div/div/div[2]/span[2]/span"
    select_role_in_adduser = "//*[@placeholder='Role']"
    superadmin_save_button = "//div/div/app-add-signup/div[2]/button[2]"
    error_msg_xpath = "/html/body/app-root/ng-toast/div/div/div[2]/p[1]"
    admin_save_button = "//span[contains(.,'Save')]"
    superadmin_search_name_xpath = '/html/body/app-root/app-sign-up/div/div/div/div/div[2]/mat-tab-group/div/mat-tab-body[2]/div/div/div/section/mat-form-field/div/div[1]/div[3]/input'
    admin_search_name_xpath = "/html/body/app-root/app-sign-up/div/div/div/div/div[2]/div/div/section/mat-form-field/div/div[1]/div[3]/input"
    superadmin_verify_added_user_xpath = "//mat-row[1]//mat-cell[1]"
    admin_verify_added_user_xpath = "//mat-row[1]//mat-cell[1]"
    verify_search = "//mat-row[1]//mat-cell[1]"
    Registration_partner_search_box_xpath ='//*[@id="mat-input-19"]'
    Registration_partner_search_box_logo_xpath="//mat-icon[normalize-space()='search']"

    # Master Page
    success_msg_xpath = "/html/body/app-root/lib-ng-toast/div/div[2]/p[1]"
    master_logo_xpath = "//a[@routerlink='/master']"
    master_page_path = "//span[normalize-space()='Master']"
    master_page_text = "//*[@id='layout-wrapper']/div/div/div/div[1]/div/div/h4"
    product_tab = "/html/body/app-root/app-master/div/div/div/div/div[2]/div/div/div/ul/li[1]/a"
    master_search_input = "//mat-form-field/div/div/div[1]/input"
    master_quantity_tab = "//li[2]/a[@class='nav-link']"
    master_miscellaneous_tab = "//*[@id='layout-wrapper']/div/div/div/div[2]/div/div/div/ul/li[5]"
    master_logistic_tab = "//*[@id='layout-wrapper']/div/div/div/div[2]/div/div/div/ul/li[3]"
    master_charges_tab = "//div[@class='card-body']/ul/li[4]"
    master_experimental_tab = "//a[normalize-space()='Experimental']"
    search_result = "//mat-table/mat-row[1]/mat-cell[1]"
    search_result_row = "//mat-table/mat-row[1]/mat-cell[{}]"
    logistics_max_dist = "//div[@class='card-body']/div[1]/h4/b"
    master_select_company = "//div[@class='page-title-right']/div/mat-select"
    master_status = "//mat-row/mat-cell[2]"
    last_modified = "//mat-row/mat-cell[3]"
    logistics_edit_button = '//mat-row[{}]//mat-cell[9]/span/button'
    logistics_name = "//mat-row[{}]/mat-cell[{}]"
    logistics_values = '//mat-table/mat-row[{}]/mat-cell[{}]/span/mat-form-field/div/div[1]/div/input'
    logistics_save = '//mat-table/mat-row[{}]/mat-cell[9]/span/button'
    logistics_roundtrip = '//mat-row[{}]/mat-cell[8]'
    master_add_product = "//div[@class='card-body']/div/button"
    master_add_distance = "//*[@class='col-sm']/button"
    master_add_new_dist_pre = "//mat-dialog-container/app-add-distance/h1"
    add_dist_company = "//mat-select[@formcontrolname='company']"
    add_dist_company_selected = "//mat-option[@tabindex='0']"
    add_dist_veh_type = "//mat-select[@formcontrolname='selectvehicleType']"
    add_dist_base_km = "//*[@data-placeholder='BaseKms Ex(05)']"
    add_dist_base_charge = "//*[@data-placeholder='baseCharge']"
    add_dist_slab1_kms = "//*[@data-placeholder='slab1kms']"
    add_dist_slab1_charge = "//*[@data-placeholder='slab1Charge']"
    add_dist_slab2_km = "//*[@data-placeholder='slab2kms']"
    add_dist_slab2_charge = "//*[@data-placeholder='slab2Charge']"
    add_dist_save = "//*[@align='end']/button[2]"
    add_dist_cancel = "//*[@align='end']/button[1]"
    round_trip = "//*[@data-placeholder='roundTrip']"
    base_km_error = "//div[@class='alert alert-danger ng-star-inserted']"
    slab_km_error = "//div[@class='ng-star-inserted'][1]"
    master_experimental_card_header = "//div[@class='card-header']/h3"
    experimental_rows = "//app-geo-based-discounts[@id='geodiscounttab']/div/div/div/div[2]/div/mat-table/mat-row"
    experimental_columns = "//app-geo-based-discounts[@id='geodiscounttab']/div/div/div/div[2]/div/mat-table/mat-header-row/mat-header-cell"
    experimental_cell = "//app-geo-based-discounts[@id='geodiscounttab']/div/div/div/div[2]/div/mat-table/mat-row[{}]/mat-cell[{}]"
    edit_button = '//*[@id="geodiscounttab"]/div/div/div/div[2]/div/mat-table/mat-row[1]/mat-cell[7]/span/button'
    radius_input = "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-edit-geo-based-discounts/div[1]/form/mat-form-field[2]/div/div[1]/div[3]/input"
    discount_input = "/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-edit-geo-based-discounts/div[1]/form/mat-form-field[3]/div/div[1]/div[3]/input"
    save_button = '/html/body/div[3]/div[2]/div/mat-dialog-container/div/div/app-edit-geo-based-discounts/div[2]/button[2]'


    # privacy policy
    privacy_policy = '/html/body/app-root/app-sign-in/div/div[3]/div/div[2]/a[1]'
    privacy_policy_text = '/html/body/app-root/app-privacyandpolicy/div/section/div/div/div/pdf-viewer/div/div[2]/div[1]/div[1]/span[1]/span'
    privacy_policy_total_text = '/html/body/app-root/app-privacyandpolicy/div/section/div/div/div/pdf-viewer/div'

    # terms and condition
    termsandcondition_button = '/html/body/app-root/app-sign-in/div/div[3]/div/div[2]/a[2]'
    termsandcondition_text = '//*[@id="p5R_mc1"]/span'
    termsandcondition_total_text = '/html/body/app-root/app-termsandconditions/div/section/div/div/div/div/pdf-viewer/div/div[2]'

    # refund and policy
    refundandpolicy_button = '/html/body/app-root/app-sign-in/div/div[3]/div/div[2]/a[3]'
    refundandpolicy_text = '//*[@id="services"]/div/div/div/div/h1[1]'
    refundandpolicy_total_text = '//*[@id="services"]/div/div'

    # Service Ticket page
    generic_tab = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/div/ul/li[1]/a'
    business_tab = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/div/ul/li[2]/a'
    technical_tab = '//*[@id="layout-wrapper"]/div/div/div/div[1]/div/div/div/ul/li[3]/a'
    ticket_id_box = "//input[@placeholder='Ticket ID']"
    service_ticket_search = "//*[@id='layout-wrapper']/div/div/div/div[2]/div/div/div[1]/form/mat-card/mat-card-content/div/button[1]"
    service_ticket_clear = '//*[@id="layout-wrapper"]/div/div/div/div[2]/div/div/div[1]/form/mat-card/mat-card-content/div/button[2]'
    result_ticket_id = '//mat-table/mat-row/mat-cell[1]'
    add_ticket_button = "//button[@mattooltip='Ticket']"
    requested_by = "//mat-select[@formcontrolname='requestedBy']"
    customer_name = '//input[@formcontrolname="requestedByName"]'
    customer_number = '//input[@formcontrolname="mobileNo"]'
    ticket_description = '//textarea[@formcontrolname="ticketDesc"]'
    ticket_priority = '//mat-select[@formcontrolname="priority"]'
    ticket_status = '//mat-select[@formcontrolname="ticketStatus"]'
    ticket_type = '//mat-select[@formcontrolname="ticketType"]'
    ticket_save_button = "//button[.='Save']"
    success_msg_ticket_ID = "//app-root/lib-ng-toast/div/div[2]/p[2]"

    # Rewards Page
    rewards_page_order_id_search = "//div/div/div/div/section/mat-form-field/div[1]/div/div[2]/input"
    rewards_page_search_button = "//mat-card-content/div/button[1]"
    rewards_page_total_points_awarded = "//table/tbody/tr[1]/td[6]"
    rewards_page_total_points_monitised = "//table/tbody/tr[1]/td[7]"
    rewards_page_amount = "//table/tbody/tr[1]/td[7]"

    # Add Accountant User
    add_user_company_xpath = "//*[@id='companyId']"
    companies_list_xpath = "//*[@id='companyId-panel']"
    name_xpath = '//input[@class="mat-input-element mat-form-field-autofill-control ng-tns-c119-45 ng-untouched ng-pristine ng-invalid cdk-text-field-autofill-monitored"]'
    role_xpath = '//span[@class="mat-select-placeholder mat-select-min-line ng-tns-c122-47 ng-star-inserted"]'
    role_admin_xpath = '//span[@class="mat-option-text"]'
    save_button_xpath = '//button[@class="mat-focus-indicator btn btn-primary mat-flat-button mat-button-base"]'

    accountant_xpath = '//*[@id="page-header-user-dropdown"]/span/span/span[2]'
    accountant_order_id = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/span'
    accountant_product = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[2]/span'
    accountant_quantity = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]/span'
    accountant_unit = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[4]/span'
    accountant_bill = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/span'
    accountant_paymode = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[6]/span'
    accountant_paystatus = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[7]/span'
    accountant_orderstatus = '/html/body/app-root/app-order/div/div/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[9]/span'

    # Cost Master page
    len1 = "//table/tbody/tr[{}]/td/div/div/div/div[{}]/table/tr"
    len2 = "//table/tbody/tr[{}]/td/div/div/div/div[{}]/table/tr[{}]/td[{}]"

    # Admin Vehicles page
    add_vehicle_button = "//div/div/div/div/div/div/button[@type='button']"
    vehicle_no_box = "//input[@formcontrolname='vehicleNo']"
    vehicle_owner_name_box = "//input[@formcontrolname='ownerName']"
    vehicle_owner_phone_number_box = "//input[@formcontrolname='phoneNo']"
    vehicle_type_dropdown = "//mat-select[@formcontrolname='vehicleType']"
    vehicle_cft_dropdown = "//mat-select[@placeholder='CFT']"
    vehicle_category_dropdown = "//mat-select[@placeholder='Vehicle Category']"
    vehicle_category_shipping = "//mat-option[@value='Shipping']"
    vehicle_status_dropdown = "//mat-select[@placeholder='Status']"
    vehicle_status_active = "//mat-option[@value='Active']"
    vehicle_status_inactive = "//mat-option[@value='Inactive']"
    vehicle_page_search_bar = "//mat-form-field/div/div/div/input[@placeholder='Search...']"
    add_vehicle_close = "//div/div/app-add-vehicle/div[2]/button[1]"
    add_vehicle_save = "//div/div/app-add-vehicle/div[2]/button[2]"
    add_vehicle_items_per_page_count = "//div/div/div/div/div[2]/div/div/div/mat-paginator/div/div/div[2]/div"

    # directsales
    user_Admin = "//span[@class='d-none d-xl-block ms-1 fs-12 text-muted user-name-sub-text']"
    oms_direct_sales_tab_xpath = '//*[@id="navbar-nav"]/li[3]/mat-nav-list/a[2]'
    add_sale_xpath = "//button[normalize-space()='Add Sale']"
    add_name_xpath = "//input[@placeholder='Name']"
    add_phno_xpath = "//input[@placeholder='Phone Number']"
    payment_xpath = "//span[contains(text(),'Select Payment Mode')]"
    payment_method_xpath = "//*[contains(text(),'POD')]"
    aggregate_xpath = "//*[contains(text(),'Select Aggregate')]"
    quantity_xpath = "//*[contains(text(),'Select Quantity')]"
    vehicle_xpath = "//input[@placeholder='Vehicle Number']"
    ds_save_button = '//app-adddirectsales/div[2]/button[2]/span[2]'
    clear_button = "//button[@style='margin-top: -12px;']"
    order_id_xpath = '//body//app-root//mat-row[1]/mat-cell[1]'
    order_phno_xpath = '//body//app-root//mat-row[1]/mat-cell[8]'
    order_aggregate_xpath = '//body//app-root//mat-row[1]/mat-cell[3]'
    order_quantity_xpath = "//body//app-root//mat-row[1]/mat-cell[4]"
    dc_xpath = "//mat-row[1]//mat-cell[9]//button[1]"
    payment_method1_xpath = "//*[contains(text(),'Credit')]"
    payment_method2_xpath = "//*[starts-with(text(),'UPI')]"
    error_message_xpath = '//app-adddirectsales/div[1]/form/mat-form-field[1]/div[2]/div'
    error_message1_xpath = '//app-adddirectsales/div[1]/form/mat-form-field[2]/div[2]/div'
    error_message2_xpath = '//app-adddirectsales/div[1]/form/mat-form-field[6]/div[2]'
    bill_amount_xpath = "//input[@placeholder='Bill Amount']"
    close_button_xpath = "//span[normalize-space()='Close']"

