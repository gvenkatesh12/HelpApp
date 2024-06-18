from behave import *
from whatsapp_automation import *
from whatsappplacementwithdiscount import *
import logging
import random


@then(u'Show "Servcrust కి స్వాగతం దయచేసి భాషను ఎంచుకోండి" Click to Select')
def step_impl(context):
    try:
        lan = context.res_hi
        if lan.find("Welcome to Servcrust.") >= 0 and lan.find("Click to select") >= 0:
            logging.info("Please choose language(English/Telugu)")
        else:
            pass
    except Exception as e:
        logging.error(f"Error occurred at Show 'స్వాగతం Servcrust. దయచేసి భాషను ఎంచుకోండి' Click to Select:{str(e)}")


@then(u'Select "తెలుగు"')
def step_impl(context):
    try:
        sel_lan = context.res_hi
        if sel_lan.find("Welcome to Servcrust.") >= 0 and sel_lan.find("Click to select") >= 0:
            send = 'తెలుగు'
            # send = input("Please select language")
            res_lan = autooms.send_json2(send)
            context.res_lan = res_lan
            logging.info(f"Select language response:{res_lan}")
        else:
            res_lan = None
            pass
    except Exception as e:
        logging.error(f"Error occurred at Select language:{str(e)}")


@when(u'show దయచేసి GPS స్థానాన్ని పంపండి')
def step_impl(context):
    try:
        if context.res_lan is not None:
            ver_lan = context.res_lan
            if ver_lan.find("దయచేసి మీ డెలివరీ స్థానాన్ని షేర్ చేయండి."):
                logging.info("Verified language as it is asking to send gps")
        else:
            res_lan = None
            pass
    except Exception as e:
        logging.error(f"Error occurred at show దయచేసి మీ డెలివరీ స్థానాన్ని షేర్ చేయండి.: {str(e)}")


@then(u'show కంకర రకాన్ని ఎంచుకోండి')
def telugu_gps_response(context):
    try:
        res_gps = context.res_gps
        if res_gps.find("క్షమించండి మీరు ఎంచుకున్న ప్రాంతానికి మా సేవలు అందించబడవు") >= 0:
            logging.info("క్షమించండి మీరు ఎంచుకున్న ప్రాంతానికి మా సేవలు అందించబడవు is displayed")
            no_service = 0
            context.no_service = no_service
        else:
            logging.info(res_gps)
            if res_gps.find("కంకర రకాన్ని ఎంచుకోండి") >= 0:
                logging.info("కంకర రకాన్ని ఎంచుకోండి is displayed")
    except Exception as e:
        logging.error(f"Error occurred at show కంకర రకాన్ని ఎంచుకోండి: {str(e)}")


@then(u'show కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT)')
def step_impl(context):
    try:
        no_service = context.no_service
        if no_service == 0:
            pass
        else:
            res_pro = context.res_pro
            logging.info(res_pro)
            if res_pro.find("కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT)") >= 0:
                logging.info("కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT) is displayed")
    except Exception as e:
        logging.error(f"Error occurred at show కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT): {str(e)}")


@then(u'show  చెల్లించాల్సిన మొత్తం')
def step_impl(context):
    try:
        no_service = context.no_service
        if no_service == 0:
            pass
        else:
            res_qty = context.res_qty
            json_start = res_qty.rfind('&message=') + len('&message=')
            json_string = res_qty[json_start:]
            response_data = json.loads(json_string)
            value_of_title = response_data["content"]["header"]
            total_amount = value_of_title.split('₹')[1]
            logging.info(f"చెల్లించాల్సిన మొత్తం : ₹{total_amount}")
    except Exception as e:
        logging.error(f"Error occurred at show  చెల్లించాల్సిన మొత్తం: {str(e)}")
