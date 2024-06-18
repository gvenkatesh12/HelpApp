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
# cap = {
#     "platformName": "Android",
#     "platformVersion": "11",
#     "deviceName": "sdk_gphone_x86",
#     "app": r"C:\Users\Manik\Downloads\base (3).apk",
#     "automationName": "UiAutomator2",
#     "resetKeyboard": True
#
# }
cap = {
    "platformName": "Android",
    "platformVersion": "14",
    "appium:automationName": "UiAutomator2",
    "deviceName": "motorola edge 50 pro",
    "app": r"C:\Users\Manik\Downloads\base (3).apk",
    "automationName": "UiAutomator2",
    "resetKeyboard": True
}
@given(u'Navigate to Vehicles tab')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Navigate to Vehicles tab')


@when(u'click on add vehicle button')
def step_impl(context):
    #ADD VEHICLE
    raise NotImplementedError(u'STEP: When click on add vehicle button')


@when(u'"Add Vehicle" pop up should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: When "Add Vehicle" pop up should be displayed')


@when(u'add the vehicle number, owner name, Driver Phone number, Vehicle type, CFT, Status')
def step_impl(context):
    raise NotImplementedError(u'STEP: When add the vehicle number, owner name, Driver Phone number, Vehicle type, CFT, Status')


@then(u'I click on confirm')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on confirm')


@then(u'verify the message "Vehicle added"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify the message "Vehicle added"')


@then(u'check the vehicle is added by searching the added vehicle number in search bar')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then check the vehicle is added by searching the added vehicle number in search bar')

