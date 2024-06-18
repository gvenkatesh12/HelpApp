#############################################################################################################
#  Author :Cantellat
#  Script Name: Whatsapp Automation
# Version : V1
# This Script Execution 7-JSON till order creation and also validates JSON Response titles as expected
############################################################################################################
import concurrent
import json
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
from whatsappjsons import *
import requests
import logging

url = f'https://whatsapp-staging.servcrust.com/listen'
# url = f'https://31c1-2401-4900-4e0f-f69f-fcef-49c0-197b-9ac7.ngrok-free.app/Listen'

genrandomid = lambda: ''.join(
    random.choices(string.ascii_uppercase + string.digits, k=len("ABEGkZYYRUZwAgo-sCO6slixPL-1")))
genphonenumber = lambda: ''.join(random.choices(string.digits, k=9))
whatsapp_json = Whatsapp_Jsons()


class autooms:
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON HI $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON Hi $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def send_hi(hi):
        global phone
        phone = '919' + str(genphonenumber())
        # phone = '917799556633'
        print("Please enter hi to place an order"),
        EnterText = hi
        msg_json = whatsapp_json.hi_msg_json
        id = genrandomid()
        msg_json['payload']['id'] = id
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['text'] = str(EnterText)
        res = requests.post(url, json=msg_json)
        dataload = res.json()
        if res.status_code == 200:
            return dataload
        else:
            print("\n**************JSON-1 Hi Response failed***********************")

            exit()

    def send_hi_number(hi, number):
        global phone
        print("Please enter hi to place an order"),
        EnterText = hi
        phone = '91' + str(number)
        msg_json = whatsapp_json.hi_msg_json
        id = genrandomid()
        msg_json['payload']['id'] = id
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['text'] = str(EnterText)
        MAX_RETRIES = 3
        print("\n**********************Json-1 Hi Input Json****************************\n")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n*******Output Response Json**************")
                break
            except:
                print("\nTimeout Error in JSON 1")
                exit()
        else:
            print("\n********All Retries failed please check********")

        dataload = res.json()

        if res.status_code == 200:
            return dataload
        else:
            print("\n**************JSON-1 Hi Response failed***********************")
            exit()

    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for Language Selection $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for Language Selection $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def send_json2(send):
        list = ["English", "Telugu"]
        print("Please enter the language(English,Telugu)")
        language = send
        msg_json = whatsapp_json.language_selection_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['title'] = str(language)
        msg_json['payload']['payload']['postbackText'] = str(language)
        MAX_RETRIES = 2
        print("\n******************JSON-2 Input Json English************************")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n**********JSON-2 Output English Response Json************")
                print(res.json())
                break
            except:
                print("\nTimeout Error in JSON 2")
        else:
            print("\n********All Retries failed please check********")

        dataload = res.json()

        if res.status_code == 200:
            return dataload
        else:
            dataload = res.json()
            if res.status_code == 200:
                return dataload
            else:
                print(res.status_code)
                print("\n**************JSON-1 Hi Response failed***********************")
            exit()

    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for GPS location $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for GPS location $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def send_json4(lat, lon):
        # phone = '9876542301'
        count = 0
        while count < 3:
            try:
                print("Please give the latitude of your location")
                latitude = lat
                print("Please give the longitude of your location")
                longitude = lon
                if ((type(latitude) != float and type(longitude) != float) or (
                        type(latitude) != float and type(longitude) == float) or (
                        type(latitude) == float and type(longitude) != float)):
                    raise TypeError
                elif type(latitude) == float and type(longitude) == float:
                    print("The given locations are in a correct format")
                    break
            except TypeError:
                count += 1
                print("The locations are not in desired format")
                print("Attempt " + str(count + 1) + " is exhausted!\n You have more " + str(
                    3 - count - 1) + " attempts to go\n Please enter the correct format... ")
            except:
                count += 1

        if count == 3:
            print("Redirecting you to the welcome screen...")
            # autooms.send_json2(send)

        msg_json = whatsapp_json.gps_sharing_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['latitude'] = str(latitude)
        msg_json['payload']['payload']['longitude'] = str(longitude)
        # MAX_RETRIES = 2
        res = requests.post(url, json=msg_json)
        print("\n*******************Input Json-4 GPS location************************")
        print(msg_json)
        print(res.json())
        print("\n**** Output GPS location Response Json***\n")

        dataload = res.json()
        if res.status_code == 200:
            print("\n************GPS location  Response Validation Pass***************")
            return dataload
        else:
            print(
                "\n**************Json GPS location Selection Response failed***********************")

            exit()

    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON Product list reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON Product list reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def send_json5(send):
        product = send
        # product = '60MM'
        msg_json = whatsapp_json.product_selection_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['title'] = str(product)
        msg_json['payload']['payload']['reply'] = str(product)
        msg_json['payload']['payload']['postbackText'] = str(product)
        MAX_RETRIES = 2
        print("\n*************************Input JSON-5 Product Quantity select**********************")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n**** Output JSON Product Quantity CFT select Response Json***\n")
                print(res.json())
                break
            except:
                print("\nTimeout Error in JSON Product CFT Quantity")
        else:
            print("\n********All Retries failed please check********")

        dataload = res.json()
        if res.status_code == 200:
            print("\n************JSON Product Quantity select Validation Pass***************")
            return dataload
        else:
            print("\n**************JSON Product Quantity Response failed***********************")

            exit()

    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON-6 Quantity list reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON-6 Quantity list reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def send_json6(send):
        quantity = send
        # quantity = '100'
        msg_json = whatsapp_json.quantity_selection_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['title'] = str(quantity)
        MAX_RETRIES = 2
        print(
            "\n*************************Input JSON-6 Quantity select**********************")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n**** Output JSON-6 Quantity select Response Json***")
                print(res.json())
                break
            except:
                print("\nTimeout Error in JSON 6")
        else:
            print("\n********All Retries failed please check********")

        dataload = res.json()
        if res.status_code == 200:
            print("\n************JSON-6 Product Quantity select Validation Pass***************")
            return dataload
        else:
            print(
                "\n**************JSON Product Quantity select validation failed***********************")

            exit()

    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON-7 COD reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Below code is for JSON-7 COD reply Select $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def send_json7(send):
        Dict = {0: 'UPI', 1: 'Others', 2: 'Pay On Delivery', 3: 'Previous Menu'}
        payment_method = Dict[int(send)]
        msg_json = whatsapp_json.payment_method_selection_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['title'] = str(payment_method)
        msg_json['payload']['payload']['postbackText'] = str(payment_method)
        msg_json['payload']['payload']['reply'] = str(payment_method)
        MAX_RETRIES = 2
        print(
            "\n*************************Input JSON-7 Payment Method select**********************")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n**** Output JSON-7 Payment Method select Response Json***")
                dataload = res.json()
                if res.status_code == 200:
                    print("\n************JSON-7 Payment Method Order Validation Pass***************")
                    print("\nYour Order has been placed successfully. Please use Order No. " + str(
                        id) + " Thanks for shopping with us. Have a Good Day.. Ending the chat!")
                    return dataload
                elif (res.status_code == 200 and dataload.find("Stone Crusher")) >= 0:
                    print("\n************JSON-7 Quantity not deliverable Reinitiating the order pass***************")
                    print(phone)
                    msg_json.clear()
                else:
                    print(
                        "\n**************JSON Product Quantity select validation failed***********************")
            except:
                print("\nTimeout Error in JSON 7")
            else:
                print("\n********All Retries failed please check********")

        else:
            print("Select the correct choice!", end="\n")
            autooms.send_json2('self')

    def send_json8(send):
        order_type = send
        msg_json = whatsapp_json.order_type_selection_json
        msg_json['payload']['sender']['phone'] = str(phone)
        msg_json['payload']['payload']['title'] = str(order_type)
        msg_json['payload']['payload']['reply'] = str(order_type)
        msg_json['payload']['payload']['postbackText'] = str(order_type)
        MAX_RETRIES = 2
        print(
            "\n*************************Input JSON-8 New Order select**********************")
        print(msg_json)
        for i in range(MAX_RETRIES):
            try:
                res = requests.post(url, json=msg_json)
                print("\n**** Output JSON-8 New Order select Response Json***")
                print(res.json())
                break
            except:
                print("\nTimeout Error in JSON 6")
        else:
            print("\n********All Retries failed please check********")

        dataload = res.json()
        if res.status_code == 200:

            return dataload

        else:
            print(
                "\n**************JSON-8 New Order select validation failed***********************")

            exit()


def startautomation():
    autooms.send_hi(f"hi")
    # counter = 0
    #
    # while counter < int(iterations):
    #
    #     print("\n" + '#' * 10 + "Automation Set [" + str(counter) + "] " + str(iterations))
    #     print(
    #         "##################################################Automation Set [" + str(
    #             counter) + "] ##################################################")
    #     print(
    #         "##################################################Automation Set [" + str(
    #             counter) + "] ##################################################")
    #     autooms.send_hi("hi")
    #     counter = counter + 1
    # else:
    #     print(
    #         "\n################################################## Automation Completed ##################################################")
    #     print(
    #         "################################################## Automation Completed ##################################################")
    #     print(
    #         "################################################## Automation Completed ##################################################")
    #
    # logging.info("Status : Automation " + str(iterations) + " Successful!")


if __name__ == "__main__":
    startautomation()

    # executions = 2
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     futures = [executor.submit(startautomation) for i in range(executions)]
    #     concurrent.futures.wait(futures)
