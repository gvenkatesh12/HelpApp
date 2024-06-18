import random
import string


class Details:
    def details(self):
        # **************** user details *******************
        base_email = 'abc@gmail.com'
        s_email = base_email.split("@")[1]
        user_name = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            user_name = user_name + i
        name_int = str(random.randint(10, 999))
        user_email = user_name + name_int + '@' + s_email
        user_mobile = str(random.randint(9000000000, 9999999999))
        user_username = user_name + name_int
        return user_email, user_mobile, user_username, user_name

    user_invalid_email = "addfile.com"
    user_invalid_mobile = "2243242343"

    def reasondetails(self):
        valid_reason = ['product is not available', 'Quality issue', 'others']
        reason = random.choice(valid_reason)

        return reason

    def vehicle_details(self):
        # **************** Vehicle details *******************
        vehicle_number = ''
        vehicle_no_text = ''
        owner_name = ''
        phone_number = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            owner_name = owner_name + i
        name2 = random.choices(string.ascii_lowercase, k=2)
        for j in name2:
            vehicle_no_text = vehicle_no_text + j
        vehicle_number = vehicle_no_text.upper() + str(random.randint(10, 99)) + vehicle_no_text.upper() + str(random.randint(1000, 9999))
        phone_number = str(random.randint(9000000000, 9999999999))
        return vehicle_number, owner_name, phone_number

    def invalid_vehicle_details(self):
        # **************** Invalid_Vehicle details *******************
        invalid_vehicle_number = ''
        invalid_owner_name = ''
        invalid_phone_number = ''
        vehicle_no_text = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            invalid_owner_name = invalid_owner_name + i
        invalid_owner_name = invalid_owner_name + str(random.randint(10, 99))
        name2 = random.choices(string.ascii_lowercase, k=3)
        for j in name2:
            vehicle_no_text = vehicle_no_text + j
        invalid_vehicle_number = vehicle_no_text + str(random.randint(10, 99)) + vehicle_no_text + str(random.randint(1000, 9999))
        invalid_phone_number = str(random.randint(1000000000, 5999999999))
        return invalid_vehicle_number, invalid_owner_name, invalid_phone_number
    
    def trip_details(self):
        # **************** trip details *******************
        driver_name = ''
        manual_dc = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            driver_name = driver_name + i
        name2 = random.choices(string.ascii_lowercase, k=5)
        for i in name2:
            manual_dc = manual_dc + i
        added_tons = str(random.randint(1, 10))
        driver_mobile = str(random.randint(9000000000, 9999999999))
        return driver_mobile, driver_name, added_tons, manual_dc

    def editlogistics(self):
        ################# Edit Logistics ##################
        base_km = random.choice(['5', '6', '7', '8', '9', '10'])
        base_charge = random.choice(['150', '200', '250'])
        slab1_km = '20'
        charges = random.choice(['10', '15', '20', '25', '30'])
        slab2_km = '40'
        return base_km, base_charge, slab1_km, charges, slab2_km

    # *************** company details ******************
    def companydetails(self):
        letter = ''
        company_name = ''
        company_name1 = random.choices(string.ascii_uppercase, k=6)
        for company in company_name1:
            company_name = company_name + company

        new_number = str(random.randint(10001, 99999))
        license_no = company_name + new_number

        new_number = str(random.randint(1000, 9999))
        letters = random.choices(string.ascii_uppercase, k=5)
        for abc in letters:
            letter = letter + abc
        pan_number = letter + new_number + 'T'

        new_number = str(random.randint(10, 99))
        gstin_no = new_number + pan_number + '1' + 'Z'

        name_no = str(random.randint(10, 999))
        base_email = 'abc@gmail.com'
        s_email = base_email.split("@")[1]
        company_email = company_name + name_no + '@' + s_email

        company_mobile = str(random.randint(9000000000, 9999999999))
        return company_name, license_no, gstin_no, pan_number, company_email, company_mobile

    def companyaddressdetails(self):
        city_list = ['JubileeHills', 'Charminar', 'Khairatabad', 'Secunderabad']
        city = random.choice(city_list)

        building_number = str(random.randint(100, 999))
        new_number = str(random.randint(10, 99))
        street = 'Street' + new_number

        pin_code = str(random.randint(100001, 999999))

        random_float = random.uniform(8.00, 37.00)
        latitude = f"{random_float:.2f}"

        random_float = random.uniform(68.00, 97.00)
        longitude = f"{random_float:.2f}"
        return city, building_number, street, pin_code, latitude, longitude

    # company_account_no = str(random.randint(100000001, 999999999))
    #
    # bank_name = "PAYTMBANK"
    #
    # ifsc_code = "PYTM0123456"
    #
    # branch = "HYD"

    def companyadmindetails(self):
        # **************** user details *******************
        base_email = 'abc@gmail.com'
        s_email = base_email.split("@")[1]
        company_admin_name = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            company_admin_name = company_admin_name + i
        name_int = str(random.randint(10, 999))
        company_admin_email = company_admin_name + name_int + '@' + s_email

        company_admin_mobile = str(random.randint(9000000000, 9999999999))

        company_admin_username = company_admin_name + name_int
        return company_admin_name, company_admin_username, company_admin_mobile, company_admin_email

    def ticketdetaisl(self):
        customer_name = ''
        name1 = random.choices(string.ascii_lowercase, k=6)
        for i in name1:
            customer_name = customer_name + i

        alternate_number = str(random.randint(9000000000, 9999999999))

        description = ''
        name2 = random.choices(string.ascii_lowercase, k=6)
        for i in name2:
            description = description + i

        notes = ''
        name3 = random.choices(string.ascii_lowercase, k=6)
        for i in name3:
            notes = notes + i

        return customer_name, alternate_number, description, notes
