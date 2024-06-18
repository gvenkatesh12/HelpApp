import random
import time
import logging
from log_msg import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from details import Details
from Locators import Locators

def findelement(context, path):
    return WebDriverWait(context.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, path)))
def findelement2(context, path):
    return WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.XPATH, path)))
def findelement1(context, path):
    return WebDriverWait(context.driver, 20, 1).until(EC.element_to_be_clickable((By.XPATH, path)))

################################ Random Order Id From OMS Page ###########################
class Random_class:

    def orderlist(self, context):
        try:
            # counter = 0
            order_list = []
            while True:
                row = findelement2(context, "//div/table/tbody/tr[1]")
                rows = findelement(context, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                for i in range(1, row_count + 1, 2):
                    xpath = Locators.form_cell_loop.format(i, 1)
                    order_id = findelement1(context, xpath)
                    order_list.append(order_id.text)
                # time.sleep(1)
                if len(rows) < 10:
                        break
                next_page = findelement1(context, Locators.server_side_pagination_next)
                if next_page.is_displayed():
                    next_page.click()
                    time.sleep(2)
                    rows = findelement(context, Locators.oms_rows)
                else:
                    break
                # counter += 1
                # if counter == 9:
                #     break
            return order_list
        except StaleElementReferenceException:
            a = order_list(self, context)
            return a
        except ElementClickInterceptedException:
            return order_list
            pass
        except TimeoutException:
            logging.info("Reached to the last page/ No records found")
            return order_list
        except Exception as e:
            logging.error(Error.orderlist.format(str(e)))
            context.driver.close()
            raise Exception from e

    ######################################################################################################
    def orderdetails(self, context):
        try:
            order_details = []
            while True:
                row = findelement2(context, "//div/table/tbody/tr[1]")
                rows = findelement(context, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column = findelement(context, Locators.oms_columns)
                for i in range(1, row_count + 1, 2):
                    order_row = []
                    for j in range(1, len(column)):
                        xpath = Locators.form_cell_loop.format(i, j)
                        order_id = findelement2(context, xpath)
                        order_row.append(order_id.text)
                    order_details.append(order_row)
                # time.sleep(1)
                if row_count < 10:
                    break
                next_page = findelement1(context, Locators.server_side_pagination_next)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(3)
                    rows = findelement(context, Locators.oms_rows)
                else:
                    break
            return order_details
        except StaleElementReferenceException:
            a = order_details(self, context)
            return a
        except ElementClickInterceptedException:
            return order_details
            pass
        except TimeoutException:
            logging.info("No records Found/ reached the lat page")
            return order_details
        except Exception as e:
            logging.error(Error.orderlist.format(str(e)))
            context.driver.close()
            raise Exception from e

    ######################################################################################################
    def serversidepagenation(self, context):
        try:
            order_details = []
            while True:
                row = findelement2(context, "//div/table/tbody/tr[1]")
                rows = context.driver.find_element(context, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column = context.driver.find_elements(By.XPATH, Locators.oms_columns)
                for i in range(1, row_count + 1, 2):
                    order_row = []
                    for j in range(1, len(column)):
                        xpath = Locators.form_cell_loop.format(i, j)
                        order_id = context.driver.find_element(By.XPATH, xpath)
                        order_row.append(order_id.text)
                    order_details.append(order_row)
                # time.sleep(1)
                if row_count < 10:
                    break
                next_page = findelement1(context, Locators.server_side_pagination_next)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(2)
                else:
                    break
            time.sleep(0.5)
            return order_details
        except ElementClickInterceptedException:
            return order_details
            pass
        except TimeoutException:
            logging.info("Reached to the last page/No records found")
            return order_details
        except Exception as e:
            logging.error(Error.orderlist.format(str(e)))
            context.driver.close()
            raise Exception from e

    ############################################################################################
    def orderdetails1(self, context):
        try:
            order_details = []
            while True:
                row = findelement2(context, "//div/table/tbody/tr[1]")
                rows = context.driver.find_elements(By.XPATH, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column = context.driver.find_elements(By.XPATH, Locators.oms_columns)
                for i in range(1, row_count + 1, 2):
                    order_row = []
                    for j in range(1, len(column) + 1):
                        xpath = Locators.form_cell_loop.format(i, j)
                        order_id = context.driver.find_element(By.XPATH, xpath)
                        order_row.append(order_id.text)
                    order_details.append(order_row)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.server_side_pagination_next)
                first_page = context.driver.find_element(By.XPATH, Locators.server_side_pagination_first)
                last_page = context.driver.find_element(By.XPATH, Locators.server_side_pagination_last)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(2)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            time.sleep(0.5)
            return order_details
        except ElementClickInterceptedException:
            return order_details
            pass
        except TimeoutException:
            logging.info("Reached to the last page/No records found")
            return order_details
        except Exception as e:
            logging.error(Error.orderlist.format(str(e)))
            context.driver.close()
            raise Exception from e

    # ******************** for reading all table(mat-row/mat-cell) values  *********************
    def tablevalues(self, context):
        try:
            time.sleep(0.1)
            table_values = []
            while True:
                rows = context.driver.find_elements(By.XPATH, Locators.table_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                columns = context.driver.find_elements(By.XPATH, Locators.table_columns)
                for i in range(1, row_count + 1):  # Rows
                    temp = []
                    for j in range(1, len(columns) + 1):  # Columns
                        xpath = Locators.table_cell_loop.format(i, j)
                        value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                        temp.append(value.text)
                    table_values.append(temp)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.next_button)
                first_page = context.driver.find_element(By.XPATH, Locators.first_page_button)
                time.sleep(0.1)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(0.3)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            return table_values
        except Exception as e:
            logging.error(Error.tablevalues.format(str(e)))
            context.driver.close()
            raise Exception from e

    # ******************** for reading total table(mat-row/mat-cell) values without last column*********************
    def tablevalues1(self, context):
        try:
            table_values1 = []
            while True:
                # logging.info("Entered while loop")
                rows = context.driver.find_elements(By.XPATH, Locators.table_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                columns = context.driver.find_elements(By.XPATH, Locators.table_columns)
                for i in range(1, row_count + 1):  # Rows
                    temp = []
                    for j in range(1, len(columns)):  # Columns
                        xpath = Locators.table_cell_loop.format(i, j)
                        value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                        temp.append(value.text)
                    table_values1.append(temp)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.next_button)
                first_page = context.driver.find_element(By.XPATH, Locators.first_page_button)
                time.sleep(0.1)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(0.3)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            return table_values1
        except Exception as e:
            logging.error(Error.tablevalues.format(str(e)))
            context.driver.close()
            raise Exception from e

    # ******************** for reading total table(tr/td) values *********************
    def formvalues(self, context):
        try:
            form_values = []
            while True:
                rows = context.driver.find_elements(By.XPATH, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column_count = context.driver.find_elements(By.XPATH, Locators.oms_columns)
                for i in range(1, row_count + 1):  # Rows
                    temp = []
                    for j in range(1, len(column_count) + 1):  # Columns
                        xpath = Locators.form_cell_loop.format(i, j)
                        value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                        temp.append(value.text)
                    form_values.append(temp)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.next_button)
                first_page = context.driver.find_element(By.XPATH, Locators.first_page_button)
                time.sleep(0.1)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(0.3)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            return form_values
        except Exception as e:
            logging.error(Error.formvalues.format(str(e)))
            context.driver.close()
            raise Exception from e

    # ******************** for reading total table(tr/td) values without first column *********************
    def formvalues2(self, context):
        try:
            form_values = []
            while True:
                rows = context.driver.find_elements(By.XPATH, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column_count = context.driver.find_elements(By.XPATH, Locators.oms_columns)
                for i in range(1, row_count + 1):  # Rows
                    temp = []
                    for j in range(2, len(column_count) + 1):  # Columns
                        xpath = Locators.form_cell_loop.format(i, j)
                        value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                        temp.append(value.text)
                    form_values.append(temp)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.next_button)
                first_page = context.driver.find_element(By.XPATH, Locators.first_page_button)
                time.sleep(0.1)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(0.3)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            return form_values
        except Exception as e:
            logging.error(Error.formvalues.format(str(e)))
            context.driver.close()
            raise Exception from e

    # ******************** for reading table(tr/td) values without last column *********************
    def formvalues1(self, context):
        try:
            form_values1 = []
            while True:
                rows = context.driver.find_elements(By.XPATH, Locators.oms_rows)
                row_count = len(rows)
                if row_count == 0:
                    break
                column_count = context.driver.find_elements(By.XPATH, Locators.oms_columns)
                for i in range(1, row_count + 1):  # Rows
                    temp = []
                    for j in range(1, len(column_count)):  # Columns
                        xpath = Locators.form_cell_loop.format(i, j)
                        value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                        temp.append(value.text)
                    form_values1.append(temp)
                time.sleep(1)
                next_page = context.driver.find_element(By.XPATH, Locators.next_button)
                first_page = context.driver.find_element(By.XPATH, Locators.first_page_button)
                time.sleep(0.1)
                if next_page.is_enabled():
                    next_page.click()
                    time.sleep(0.3)
                elif first_page.is_enabled():
                    first_page.click()
                    break
                else:
                    break
            return form_values1
        except Exception as e:
            logging.error(Error.formvalues.format(str(e)))
            context.driver.close()
            raise Exception from e

    def onepage(self, context):
        try:
            table_values = []
            time.sleep(0.5)
            rows = context.driver.find_elements(By.XPATH, Locators.table_rows)
            row_count = len(rows)
            columns = context.driver.find_elements(By.XPATH, Locators.table_columns)
            for i in range(1, row_count + 1):  # Rows
                temp = []
                for j in range(1, len(columns)):  # Columns
                    xpath = Locators.table_cell_loop.format(i, j)
                    value = context.driver.find_element(By.XPATH, xpath)  # Cell value
                    temp.append(value.text)
                table_values.append(temp)
            return table_values
        except Exception as e:
            logging.error(Error.onepage.format(str(e)))
            context.driver.close()
            raise Exception from e

    def editlogistics(self, context):
        try:
            time.sleep(1)
            details_entered = []
            rows = context.driver.find_elements(By.XPATH, Locators.table_rows)
            row_count = len(rows)
            columns = context.driver.find_elements(By.XPATH, Locators.table_columns)
            for j in range(1, row_count + 1):
                obj = Details()
                base_km, base_charge, slab1_km, charges, slab2_km = obj.editlogistics()
                time.sleep(1)
                edit = context.driver.find_element(By.XPATH, Locators.logistics_edit_button.format(j))
                edit.click()
                time.sleep(1)
                temp = []
                name = context.driver.find_element(By.XPATH, Locators.logistics_name.format(j, 1)).text
                temp.append(name)
                for k in range(2, len(columns) - 1):
                    values = context.driver.find_element(By.XPATH, Locators.logistics_values.format(j, k))
                    values.clear()
                    time.sleep(0.2)
                    if k == 2:
                        send = base_km
                        values.send_keys(send)
                        temp.append(send)
                    elif k == 3:
                        send = base_charge
                        values.send_keys(send)
                        temp.append(send)
                    elif k == 4:
                        values.send_keys(slab1_km)
                        temp.append(slab1_km)
                    elif k == 6:
                        values.send_keys(slab2_km)
                        temp.append(slab2_km)
                    else:
                        send = charges
                        values.send_keys(send)
                        temp.append(send)
                save = context.driver.find_element(By.XPATH, Locators.logistics_save.format(j))
                save.click()
                roundtrip = context.driver.find_element(By.XPATH, Locators.logistics_roundtrip.format(j))
                temp.append(roundtrip.text)
                details_entered.append(temp)
                time.sleep(2)
            return details_entered
        except Exception as e:
            logging.error(Error.edit_logistics.format(str(e)))
            context.driver.close()
            raise Exception from e
