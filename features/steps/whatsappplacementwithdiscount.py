import re
from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from log import LogConfigurator
from whatsapp_automation import *
from whatsapporderplacementintelugu import *
import logging
import random
from urllib.parse import parse_qs

configurator = LogConfigurator()


@given(u'I send "Hi"')
def step_impl(context):
    configurator.before_all(context)
    try:
        hi = "Hi"
        res_hi = autooms.send_hi(hi)
        logging.info(f"Hi message response is : {res_hi}")
        if res_hi.find("Sorry! Your Order request cannot be processed") >= 0 or res_hi.find(
                "సరైన జవాబు ఇవ్వకపోవటం వలన మీ ఆర్డర్ రద్దు చేయబడినది"):
            context.res_hi = res_hi
            logging.info(f"Hi message response is : {res_hi}")
        else:
            context.res_hi = res_hi
        logging.info("Hi message sent")
    except Exception as e:
        logging.error(f"Error occurred at sending hi:{str(e)}")


@given(u'I send "Hi" from "{Mobile_number}"')
def step_impl(context, Mobile_number):
    configurator.before_all(context)
    try:
        print("Please enter Hi ")
        hi = "Hi"
        number = Mobile_number
        res_hi = autooms.send_hi_number(hi, number)
        if res_hi.find("Sorry! Your Order request cannot be processed") >= 0 or res_hi.find(
                "సరైన జవాబు ఇవ్వకపోవటం వలన మీ ఆర్డర్ రద్దు చేయబడినది"):
            context.res_hi = res_hi
            logging.info(f"Hi message response is : {res_hi}")
        else:
            context.res_hi = res_hi
        logging.info("Hi message sent")
    except Exception as e:
        logging.error(f"Error occurred at sending hi:{str(e)}")


@given(u'Choose Language')
def step_impl(context):
    try:
        global existing_number
        lan = context.res_hi
        existing_number = 1
        if lan.find("Welcome to Servcrust.") >= 0 and lan.find("Click to select") >= 0:
            logging.info("Please choose language(English/Telugu)")
            existing_number = 0
            logging.info("Order from New number")
        if lan.find("Select Order Type") >= 0 or lan.find("కంకర రకాన్ని ఎంచుకోండి") >= 0:
            logging.info("Order from Existing number")
            existing_number = 1
    except Exception as e:
        logging.error(f"Error occurred at Choose language:{str(e)}")


@given(u'Select Language')
def step_impl(context):
    if existing_number == 0:
        try:
            sel_lan = context.res_hi
            assert sel_lan.find("Welcome to Servcrust.") >= 0 and sel_lan.find("Click to select") >= 0
            send = 'English'
            logging.info(f"{send} language selected")
            res_lan = autooms.send_json2(send)
            context.res_lan = res_lan
            logging.info(f"Response after language selection :{res_lan}")
        except Exception as e:
            logging.error(f"Error occurred at Select language:{str(e)}")
    else:
        pass


@given(u'verify the messages in Language')
def step_impl(context):
    if existing_number == 0:
        try:
            if context.res_lan is not None:
                ver_lan = context.res_lan
                if ver_lan.find("Please share the Delivery Location (GPS)"):
                    logging.info("Got response in the selected language")
            else:
                res_lan = None
                pass
        except Exception as e:
            logging.error(f"Error occurred at verify language: {str(e)}")
    else:
        pass


@when(u'show Orders Type')
def step_impl(context):
    if existing_number == 1:
        try:
            order = context.res_hi
            if order.find("Select Order Type") >= 0 or order.find("కంకర రకాన్ని ఎంచుకోండి") >= 0:
                json_start = order.find('&message=') + len('&message=')
                json_string = order[json_start:]
                response_data = json.loads(json_string)
                value_of_body = response_data["body"]
                logging.info(value_of_body)
            else:
                pass
        except Exception as e:
            logging.info("Error occurred at show order type")
    else:
        pass


@when(u'Select "New Order"')
def step_impl(context):
    try:
        order_type = context.res_hi
        if order_type.find("Select Order Type") >= 0 or order_type.find("కంకర రకాన్ని ఎంచుకోండి") >= 0:
            send = 'New'
            # # send = input("Please select order type:")
            res_order = autooms.send_json8(send)
            logging.info("request sent json8")
            context.res_order = res_order
            logging.info(f"New order response : {res_order}")
        else:
            context.res_order = None
            pass
    except Exception as e:
        logging.error(f"Error occurred at select new order: {str(e)}")


@when(u'show "Please share the Delivery Location (GPS)"')
def step_impl(context):
    try:
        if context.res_order is not None:
            if context.res_order.find("Please share the Delivery Location (GPS)") >= 0 or context.res_order.find(
                    "show దయచేసి GPS స్థానాన్ని పంపండి") >= 0:
                json_start = context.res_order.rfind('&message=') + len('&message=')
                json_string = context.res_order[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["text"]
                logging.info(value_of_title)
        elif context.res_lan is not None:
            if context.res_lan.find("Please share the Delivery Location (GPS)") >= 0 or context.res_lan.find(
                    "show దయచేసి GPS స్థానాన్ని పంపండి") >= 0:
                json_start = context.res_lan.rfind('&message=') + len('&message=')
                json_string = context.res_lan[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["text"]
                logging.info(value_of_title)
    except Exception as e:
        logging.error(f"Error occurred at Please share the Delivery Location (GPS) {str(e)}")


@when(u'add "latitude" and "longitude"')
def step_impl(context):
    try:
        no_service = 1
        context.no_service = no_service

        # For random lat and lon
        # random_float_lat = random.uniform(15.50, 19.55)
        # random_float_lon = random.uniform(77.14, 81.19)
        # lat = f"{random_float_lat:.2f}"
        # lon = f"{random_float_lon:.2f}"

        # lat and lon for Indian mines Company
        # lat = 17.445391
        # lon = 78.386556

        # lat and lon for Tirupati mines Company
        # lat = 13.679914
        # lon = 79.511421

        # lat and lon for Maruthi mines Company
        # lat = 13.305457
        # lon = 77.168461

        # lat and lon for Automation Company
        lat = 18.782832
        lon = 78.298908

        logging.info(f"Given location is = latitude:{lat} and longitude:{lon}")
        res_gps = autooms.send_json4(lat, lon)
        context.res_gps = res_gps
        # logging.info(f"Select gps response: {res_gps}")
    except Exception as e:
        logging.error(f"Error occurred at add 'latitude' and 'longitude': {str(e)}")


@Then(u'add "{latitude}" and "{longitude}"')
def step_impl(context, latitude, longitude):
    try:
        logging.info("adding location.")
        no_service = 1
        context.no_service = no_service
        logging.info(f"Given location is = latitude:{latitude} and longitude:{longitude}")
        res_gps = autooms.send_json4(latitude, longitude)
        context.res_gps = res_gps
        # logging.info(f"Select gps response: {res_gps}")
    except Exception as e:
        logging.error(f"Error occurred at add 'latitude' and 'longitude': {str(e)}")


@when(u'Show Place order for order types')
def step_impl(context):
    try:
        no_service = context.no_service
        if no_service == 0:
            pass
        else:
            show_pro = context.res_gps
            logging.info(show_pro)
            if show_pro.find("Select Aggregate Type") >= 0 and show_pro.find("Aggregate") >= 0:
                json_start = show_pro.find('&message=') + len('&message=')
                json_string = show_pro[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["title"]
                logging.info(value_of_title)
            if show_pro.find("Sorry! Our services are not deliverable to your chosen location") >= 0:
                logging.info("The services are not available in the given location")
                no_service = 0
                context.no_service = no_service
                raise Exception
    except Exception as e:
        logging.error(f"Error occurred at show place order: {str(e)}")
        raise Exception from e


@when(u'select product')
def step_product(context):
    try:
        global no_product
        no_service = context.no_service
        if no_service == 0:
            no_product = 1
            pass
        else:
            products = []
            sel_pro = context.res_gps
            json_start = sel_pro.find('&message=') + len('&message=')
            json_string = sel_pro[json_start:]
            response_data = json.loads(json_string)
            options = response_data['items'][0]['options']
            for option in options:
                products.append(option['postbackText'])
            logging.info(products)
            send = random.choice(products)
            # send = "20ఎమ్ఎమ్"
            logging.info(f"Product selected is : {send}")
            res_pro = autooms.send_json5(send)
            context.res_pro = res_pro
            no_product = 0
            # logging.info(f"Select product response: {res_pro}")
    except Exception as e:
        logging.error(f"Error occurred at select product: {str(e)}")


@when(u'select "{product}" from given list')
def step_impl(context, product):
    try:
        global no_product
        no_service = context.no_service
        if no_service == 0:
            no_product = 1
            pass
        else:
            products = []
            sel_pro = context.res_gps
            json_start = sel_pro.find('&message=') + len('&message=')
            json_string = sel_pro[json_start:]
            response_data = json.loads(json_string)
            options = response_data['items'][0]['options']
            for option in options:
                products.append(option['title'])
            logging.info(products)
            i = 0
            for p in products:
                if p == product:
                    logging.info(f"Product selected is : {str(product)}")
                    res_pro = autooms.send_json5(str(product))
                    context.res_pro = res_pro
                    no_product = 0
                    break
                else:
                    i = i + 1
            if i == len(products):
                logging.info("The given product is currently not available")
                no_product = 1
            # logging.info(f"Select product response: {res_pro}")
    except Exception as e:
        logging.error(f"Error occurred at select product: {str(e)}")


@when(u'show quantity in CFT')
def step_impl(context):
    if no_product == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                show_qty = context.res_pro
                logging.info(show_qty)
                assert show_qty.find("Select Quantity (CFT)") >= 0 or show_qty.find(
                    "కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT") >= 0
                json_start = show_qty.rfind('&message=') + len('&message=')
                json_string = show_qty[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["title"]
                value_of_body = response_data["body"]
                logging.info(f"{value_of_body} for {value_of_title}")
        except Exception as e:
            logging.error(f"Error occurred at show qty in CFT: {str(e)}")
    else:
        pass


@when(u'select quantity')
def step_quantity(context):
    if no_product == 0:
        try:
            global no_quantity
            no_service = context.no_service
            if no_service == 0:
                no_quantity = 1
                pass
            else:
                quantity = []
                sel_qty = context.res_pro
                json_start = sel_qty.find('&message=') + len('&message=')
                json_string = sel_qty[json_start:]
                response_data = json.loads(json_string)
                options = response_data['items'][0]['options']
                for option in options:
                    quantity.append(option['title'])
                logging.info(quantity)
                send = random.choice(quantity[:-1])  # excluding previous menu
                # send = "1000"
                no_quantity = 0
                logging.info(f"Quantity selected is : {send}")
                res_qty = autooms.send_json6(send)
                context.res_qty = res_qty
                if res_qty.find('Pay On Delivery') >= 0 or res_qty.find('చెల్లించాల్సిన మొత్తం') >= 0:
                    logging.info(f"Selected quantity or product is deliverable: {res_qty}")
                    assert True
                else:
                    logging.info(f"Selected quantity or product is not deliverable : {res_qty}")
                    assert False
        except Exception as e:
            logging.error(f"Error occurred at select qty: {str(e)}")
            raise Exception from e
    else:
        no_quantity = 1
        pass


@Then(u'select "{quantity}" from given list')
def step_impl(context, quantity):
    if no_product == 0:
        try:
            global no_quantity
            no_service = context.no_service
            if no_service == 0:
                no_quantity = 1
                pass
            else:
                quantities = []
                sel_qty = context.res_pro
                json_start = sel_qty.find('&message=') + len('&message=')
                json_string = sel_qty[json_start:]
                response_data = json.loads(json_string)
                options = response_data['items'][0]['options']
                for option in options:
                    quantities.append(option['title'])
                logging.info(quantities)
                i = 0
                for q in quantities:
                    if q == quantity:
                        logging.info(f"Quantity selected is : {str(quantity)}")
                        res_qty = autooms.send_json6(str(quantity))
                        context.res_qty = res_qty
                        if res_qty.find('Pay On Delivery') >= 0 or res_qty.find('చెల్లించాల్సిన మొత్తం') >= 0:
                            logging.info(f"Selected quantity or product is deliverable: {res_qty}")
                            assert True
                        else:
                            logging.info(f"Selected quantity or product is not deliverable : {res_qty}")
                            assert False
                        no_quantity = 0
                        break
                    else:
                        i = i + 1
                if i == len(quantities):
                    logging.info("The given Quantity is currently not available")
                    no_quantity = 1
        except Exception as e:
            logging.error(f"Error occurred at select qty: {str(e)}")
            raise Exception from e
    else:
        no_quantity = 1
        pass


@when(u'previous menu is selected')
def step_impl(context):
    pass


@when(u'show total amount to pay after discount')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                amt_json = context.res_qty
                json_start = amt_json.rfind('&message=') + len('&message=')
                json_string = amt_json[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["content"]["header"]
                total_amount = value_of_title.split('₹')[1]
                logging.info(f"Total amount : ₹{total_amount}")
        except Exception as e:
            logging.error(f"Error at show amount {str(e)}")
    else:
        pass


@when(u'show discount claimed')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                dis_json = context.res_qty
                json_start = dis_json.find('&message=') + len('&message=')
                json_string = dis_json[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["content"]["text"]
                if value_of_title.find("Reward Claimed") >= 0 or value_of_title.find("రివార్డు మొత్తం") >= 0:
                    reward_claimed = value_of_title.split('₹')[1]
                    logging.info(f"Reward Claimed : ₹{reward_claimed}")
                else:
                    logging.info('Reward Claimed is : ₹0.00')
        except Exception as e:
            logging.error(f"Error at show discount {str(e)}")
    else:
        pass


@when(u'Show payment options')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                show_pay = context.res_qty
                assert show_pay.find("Amount to Pay") >= 0 or show_pay.find("చెల్లించాల్సిన మొత్తం") >= 0
                json_start = show_pay.find('&message=') + len('&message=')
                json_string = show_pay[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data['options'][2]["postbackText"]
        except Exception as e:
            logging.error(f"Error occurred at select payment option: {str(e)}")
    else:
        pass


@when(u'select payment option')
def step_payment_option(context):
    if no_quantity == 0:
        try:
            global payment
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                payment = []
                pay_json = context.res_qty
                assert pay_json.find("Amount to Pay") >= 0 or pay_json.find("చెల్లించాల్సిన మొత్తం") >= 0
                json_start = pay_json.find('&message=') + len('&message=')
                json_string = pay_json[json_start:]
                response_data = json.loads(json_string)
                options = response_data['options']
                for option in options:
                    payment.append(option['postbackText'])
                logging.info(f"Payment methods : {payment}")
        except Exception as e:
            logging.error(f"Error occurred at select payment: {str(e)}")
    else:
        pass


@when(u'Payment option is pay on delivery')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                pay_json = context.res_qty
                assert pay_json.find("Amount to Pay") >= 0 or pay_json.find("చెల్లించాల్సిన మొత్తం") >= 0
                send = 2  # Pay on delivery
                res_pay = autooms.send_json7(send)
                context.res_pay = res_pay
                logging.info("Your payment option is pay on delivery")
        except Exception as e:
            logging.error(f"Error occurred at pay on delivery : {str(e)}")
    else:
        pass


@when(u'Payment option is Others')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                pay_json = context.res_qty
                assert pay_json.find("Amount to Pay") >= 0 or pay_json.find("చెల్లించాల్సిన మొత్తం") >= 0
                send = 1  # Others
                res_pay = autooms.send_json7(send)
                logging.info(res_pay)
                context.res_pay = res_pay
                logging.info("Your payment option is Others")
        except Exception as e:
            logging.error(f"Error occurred at Payment option is Others : {str(e)}")
    else:
        pass


@Then(u'Payment option is "{Payment_Option}" from given options')
def step_impl(context, Payment_Option):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                pass
            else:
                pay_json = context.res_qty
                assert pay_json.find("Amount to Pay") >= 0 or pay_json.find("చెల్లించాల్సిన మొత్తం") >= 0
                send = 2  # Pay on delivery
                res_pay = autooms.send_json7(send)
                context.res_pay = res_pay
                logging.info(f"Your payment option is {Payment_Option}")
        except Exception as e:
            logging.error(f"Error occurred at {Payment_Option} : {str(e)}")
    else:
        pass


@then(u'Show Order placed message with order id')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                configurator.after()
                pass
            else:
                order = context.res_pay
                # if order.find("Please use Order No.") >= 0:
                ord_json = order
                json_start = ord_json.find('&message=') + len('&message=')
                json_string = ord_json[json_start:]
                response_data = json.loads(json_string)
                value_of_title = response_data["text"]
                logging.info(ord_json)
                if ord_json.find("Order ID") >= 0:
                    order_number_match = re.search(r'\*([^*]+)\*', value_of_title)
                if ord_json.find("మీ ఆర్డర్ విజయవంతం చేయబడింది") >= 0:
                    order_number_match = re.search(r'\*([^*]+)\*', value_of_title)
                if order_number_match:
                    global Order_Id
                    Order_Id = order_number_match.group(1)
                    # print("Order Number:", order_number)
                    logging.info(f"Order Number: {Order_Id}")
                else:
                    logging.info("Order number not found in the API response.")
                logging.info(value_of_title)
                configurator.after()
        except TypeError:
            pass
        except Exception as e:
            logging.error(f"Error occurred at showing order placed:{str(e)}")
    else:
        pass


@then(u'Show Pay using Payment Link')
def step_impl(context):
    if no_quantity == 0:
        try:
            no_service = context.no_service
            if no_service == 0:
                configurator.after()
                pass
            else:
                order = context.res_pay
                # if order.find("Please use Order No.") >= 0:
                ord_json = order
                query_params = parse_qs(ord_json)
                text = query_params.get('message', [''])[0]
                if ord_json.find("Pay via Payment Link") >= 0:
                    pattern = r'https?://\S+'
                    match = re.search(pattern, text)
                    if match:
                        payment_link = match.group(0)
                        context.payment_link = payment_link
        except TypeError:
            pass
        except Exception as e:
            logging.error(f"Error occurred at Show Pay using Payment Link:{str(e)}")
    else:
        pass


@then(u'Complete the Payment using the given link')
def step_impl(context):
    if no_quantity == 0:
        try:
            global Order_Id
            no_service = context.no_service
            if no_service == 0:
                configurator.after()
                pass
            else:
                payment_link = context.payment_link
                start_index = payment_link.find('https')
                if start_index != -1:
                    # Find the end of the URL by looking for the first double quote after the URL starts
                    end_index = payment_link.find('"', start_index)
                    if end_index != -1:
                        # Extract the URL
                        payment_link = payment_link[start_index:end_index]
                    else:
                        logging.info("End of URL not found.")
                else:
                    logging.info("URL not found.")
                logging.info(f"Link is: {payment_link}")
                # options = webdriver.ChromeOptions()
                # from selenium.webdriver.chrome.options import Options
                # chrome_options = Options()
                # options.add_argument('--ignore-ssl-errors=yes')
                # options.add_argument('--ignore-certificate-errors')
                # # options.add_argument('--headless')  # Uncomment to run Chrome in headless mode

                # driver = webdriver.Remote(command_executor='http://43.204.211.229:4444/wd/hub', options=chrome_options)
                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.get(payment_link)
                time.sleep(5)
                global Order_Id
                if payment_link.find("easebuzz") <= 0:
                    Order_Id = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="app-container"]/div/div[1]/div/div[1]/div/div[1]/div[2]/div[2]/div'))).text
                    logging.info(f"Your Order_Id is: {Order_Id}")
                    driver.switch_to.frame(0)
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='contact']"))).send_keys("9849333333")
                    time.sleep(1)
                    proceed_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div[4]/form/div[4]/div")))
                    proceed_button.click()
                    time.sleep(1)

                    ############# Payment with Net banking ############
                    net_banking_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="form-common"]/div[1]/div[1]/div/div/div[2]/div/button[3]/div')))
                    net_banking_button.click()
                    select_any_bank = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                  "/html/body/div[2]/div[2]/div/div[3]/div[4]/form/div[2]/div[6]/div[1]/div[1]/div/div[1]/div[2]")))
                    select_any_bank.click()
                    pay_now_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@id='redesign-v15-cta']")))
                    pay_now_button.click()
                    driver.switch_to.window(driver.window_handles[1])
                    success_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@class='success']")))
                    success_button.click()
                    time.sleep(1)

                    ############# Payment with Card ############
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='card_number']"))).send_keys("5267 3181 8797 5449")
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='card_expiry']"))).send_keys("0228")
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='card_name']"))).send_keys("Automation")
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='card_cvv']"))).send_keys("444")
                    # time.sleep(1)
                    # WebDriverWait(driver, 10, 1).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='redesign-v15-cta']"))).click()
                    # time.sleep(2)
                    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="overlay"]/div/div/button[2]'))).click()
                    # time.sleep(3)
                    # driver.switch_to.window(driver.window_handles[1])
                    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="otpForm"]/input'))).send_keys("4444")
                    # time.sleep(1)
                    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-action"]'))).click()

                    logging.info(f"Payment Successful for the order_id: {Order_Id}")
                    time.sleep(10)
                    driver.quit()
                else:
                    time.sleep(1)
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@id='easycollect_submit_payment']"))).click()
                    time.sleep(2)
                    driver.switch_to.frame(0)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[4]/div/div[2]/div[2]'))).click()
                    time.sleep(3)
                    WebDriverWait(driver, 10, 1).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Card Number']"))).send_keys(
                        int(5553042241984105))
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='MM/YY']"))).send_keys("0728")
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//input[@placeholder='Card Holder Name']"))).send_keys("Test")
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='CVV']"))).send_keys(int(123))
                    time.sleep(1)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[4]/div/div/button'))).click()
                    time.sleep(10)
                    driver.switch_to.window(driver.window_handles[1])
                    otp = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//span[@id='random-number']"))).text
                    logging.info(f"OTP is {otp}")
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='digit1']"))).click()
                    time.sleep(1)
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='digit1']"))).send_keys(otp[0])
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='digit2']"))).send_keys(otp[1])
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='digit3']"))).send_keys(otp[2])
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='digit4']"))).send_keys(otp[3])
                    time.sleep(2)
                    WebDriverWait(driver, 10, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@onclick="validateOTP(\'success\')"]'))).click()
                    time.sleep(7)
                    driver.switch_to.window(driver.window_handles[0])
                    success_msg = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='easycollect_container']/div/div/div/div[2]/div/div/div[2]/p/small"))).text
                    logging.info(success_msg)
                    time.sleep(2)
                    Order_Id = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "//div/div/div/div[2]/div/div/div[2]/ul/li[3]/p"))).text
                    logging.info(f"Your Order_Id is: {Order_Id[:-4]}")
                    time.sleep(1)
                    driver.quit()
        except Exception as e:
            logging.error(f"Error occurred at Complete the Payment using the given link:{str(e)}")
    else:
        pass


def order_id_method(context):
    order_id = Order_Id
    logging.info(order_id)
    return order_id
