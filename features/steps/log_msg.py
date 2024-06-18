class Info:
    ## Login_page
    chrome = "Successfully launched chrome browser"
    random_value = "Random value is: {}"
    open_oms_home_page = "Successfully accessed {}"
    click_login_button = "Successfully clicked on login button in home page"
    login_credentials = "Entered User_Name: {} and Entered Password: {}"
    click_signin_button = "Successfully clicked on Signin button"
    login_success_message_text = "Signed in successfully"
    login_success_message = "Successfully Logged in"
    superadmin_text_verify = "SUPERADMIN"
    admin_text_verify = "PARTNER"
    executive_text_verify = "EXECUTIVE"
    accountant_text_verify = "ACCOUNTANT"
    onboarding_text_verify = "ONBOARDING"
    operations_head_text_verify = "OPERATIONSHEAD"
    support_manager_text_verify = "SUPPORTMANAGER"
    support_executive_text_verify = "SUPPORTEXECUTIVE"
    finance_head_text_verify = "FINANCEHEAD"
    user_verification = "Successfully accessed the {} account"
    logout = "Logout Successful"
    close_the_browser = "Closed the browser"

    ## OMS Page
    all_order_status = ['Placed', 'Confirmed', 'Dispatched', 'Delivered', 'Cancelled By System', 'Cancelled By Admin',
                        'Cancelled By Customer']
    order_status = ['Placed', 'Confirmed', 'Dispatched', 'Delivered']
    cancelled_status = ['Cancelled By System', 'Cancelled By Admin', 'Cancelled By Customer']
    show_oms_page = "Successfully shown the OMS Page"

    ## findorder.py
    random_order = "Random order select: {}"
    random_order_status = "Order status is: {}"

    ## All Users
    servcrust_tab = "Successfully shown all user details for ServCrust_tab {}"
    admin_tab = "Successfully shown all user details for admin_tab: {}"
    others_tab = "Successfully shown all user details for others_tab: {}"
    add_user_page = "Successfully clicked on add user page"
    entered_username = "successfully entered a username"
    user_search = "Successfully searched for user"

    ##Stock Page
    show_stock = "Stock of {} : {}"
    enter_order_id = "Successfully entered order_id {} in search tab"
    selected = "Successfully selected {}"
    stock_list = "Stock list : {}"
    stock = "Successfully shown the list of products"
    tons_text = "Tons"
    stock_text = "STOCK"
    cft_text = "CFT"
    toggle_tons = "Successfully toggled to Tons"
    toggle_cft = "Successfully toggled the button to CFT"
    stock_cft = "Successfully shown the details of stock in CFT: {}"
    stock_tons = "Successfully shown the details of stock in TONS: {}"
    total_products = "Successfully shown the total count : {}"
    page_count = "Successfully shown page count : {}"
    add_stock_button = "add stock button clicked successfully"
    stock_page = "Successfully shown stock page"
    product_search = "Entered the product in search: {}"

    ## Service Ticket Page
    service_ticket_page = "Successfully shown service ticket page"
    business_tab = "Successfully clicked on business tab"
    technical_tab = "Successfully clicked on technical tab"
    ticket_details = "Successfully got ticket details : {}"
    search_ticket = "Search Ticket_ID is : {}"
    result_ticket = "Result Ticket_ID is : {}"

    ##Rewards Page
    no_rewards = "No Orders are available"
    rewards_page = "Successfully shown the rewards page"
    get_rewards = "Successfully got the rewards for given order_id {}"
    total_rewards = "Successfully show the total reward points"
    rewards_monetised = "Successfully show the total reward points monetised"
    total_amount = "Successfully shown the total amount"

    ## Database
    values_inserted = "Successfully inserted"
    verify_details = "Successfully verified the details: {}"
    record_from_db = "Records from database:{}"

    ##Details
    details = "Details of {} : {}"

    ## Products Tab
    master_page = "Successfully shown the Master Page"
    products_tab = 'Successfully clicked on Products Tab'
    products_list = "Products list: {}"
    count_match = "Page count matched with total count which is : {}"
    compare_product_db = "Compared product details with product table in database"

    ##Quantity Tab
    click_quantity_tab = "Clicked on Quantity tab"
    no_quantity_msg = "Given quantity is not available in the company"
    quantity_available = "Given quantity is available in the company: {}"
    status = "Status details: {}"
    last_modified = "Last Modified is : {}"
    given_quantity = "Given Quantity : {}"
    quantity_list = "Quantities list is :{}"
    quantity_tab = 'Successfully clicked on Quantity Tab'
    compare_quantity_db = "Compared quantity details with quantity table in database"

    ##Experimental tab
    experimental_tab = "Successfully clicked on Experimental tab."
    geo_based_text = ' Geo Based Discounts '
    geo_based_discount = "Successfully shown Geo Based discounts"

    ##Miscellaneous tab
    click_miscellaneous_tab = "Miscellaneous tab clicked"

    ##Logistics Tab
    click_logistics_tab = "Logistics tab clicked"
    select_company = "Company : {}"
    max_shipping_dist = "Maximum Shipping Distance: {}"
    logistics_detail = "Detail : {}"
    logistics_details = "Details : {}"
    add_distance_enabled = "Add Distance is enabled"
    add_distance_clicked = "Successfully clicked add distance "
    dist_preset = "Distance Presets :{}"
    company_verify = "Company is matching the company selected"
    veh_type = "Vehicle type selected as : {}"
    veh_details = "VehicleTypes and details : {}"
    details_entered = "Details entered : {}"
    base_km = 'Entered base kms : {}'
    base_tab = 'Clicked tab on base kms'
    base_km_text = "The Base Kms is required."
    base_km_error = "Successfully verified base kms error message "
    base_km_msg = "Successfully verified base kms error message "
    base_charge = "Entered base charges : {}"
    base_charges_tab = 'Clicked tab on base charges '
    base_charges_txt = "Error message : Base charge is required"
    base_less = 'Base KMs should be less than Slab1 kms and Slab2 Kms '
    slab1_greater = "Entered slab1 kms greater than base kms : {}"
    slab1_less = 'Entered slab1 value less than base kms'
    slab1_charges = "Entered slab1 charges : {}"
    slab1_error = "Successfully verified slab1 error message"
    slab2_kms = "Entered slab2 kms greater than slab1 and base kms : {}"
    slab2_less = 'Entered slab2 less than slab1 and greater than base kms'
    slab2_less_base = 'Entered slab2 less than base kms'
    slab2_greater = "Slab1 Kms should be less than Slab2 kms and more than Base kms"
    slab2_charges = "Entered slab2 charges : {}"
    round_trip = "Round trip : {}"
    verify_round_trip = "Verified Round trip"
    page_update = "Page is updated with new details"
    page_update_fail = 'Failed to update with the new vehicle type details'
    save = 'Clicked on save'
    close = "close button clicked successfully"

    ## Charges Tab
    charges_tab = "Successfully clicked on Charges tab"
    show_charges = "Charges : {}"


    ## AddAccountantUser.py
    show_all_servcrust_user_details = "Successfully showed all servcrust user details page"
    click_add_user_button = "Clicked on Add User Button"
    servcrust_ltd_company_text = 'ServCrust Ltd'
    accountant_role_text = 'accountant'
    finance_head_role_text = "financehead"
    Registration_text ="registration"
    added_all_user_details = "Entered all the required details"
    entered_input_in_search_box = "Given inputs in search box"
    expected_email = "Expected email: {}"
    search_result_email = "Search result email: {}"
    save_button = "Save button clicked successfully"

    ## AddOnboardingUser.py
    select_servcrust_ltd_company = "ServCrust Ltd selected from list of companies"
    onboarding_role_text = 'onboarding'
    operations_head_role_text = 'operationshead'
    support_executive_role_text = 'supportexecutive'
    support_manager_role_text = 'supportmanager'

    # AddUserAdmin.py
    added_company_details = "Company details added and clicked next"
    added_address_details = "Address details added and clicked next"
    add_basic_option = "Basic option added and clicked next"
    submit_button = "Submit button clicked"
    company_entered_in_search_box = "Company name entered in search box"
    company_search_result_displayed = "Search result displayed"
    company_search_result_empty = "Search result is empty"
    expected_mobile = "Expected mobile: {}"
    search_result_mobile = "Search result mobile: {}"
    company_selected = "Successfully selected the company: {}"
    select_new_company_created = "Company selected from list of companies"
    admin_role_text = 'Partner'
    success_message = "success Message"
    success_message_displayed = "Success Message displayed"
    invalid_email = "Entered the email which is not valid"
    error_message_for_invalid_email = "enter a valid email"
    displayed_error_message_for_invalid_email = "Error message: Enter a valid email is displayed"
    invalid_mobile = "Entered the mobile number which is incorrect"
    error_message_for_invalid_mobile = "enter a valid 10-digit mobile number"
    displayed_error_message_for_invalid_mobile = "Error message: Enter a valid 10-digit mobile number is displayed"
    error_creating_user = "Error Creating User"
    error_creating_user_message = "User Already Exists .. Please try with new user"

    ## superadminadduser.py
    user_added = "successfully created {} user"

    ## Company.py
    show_company_page = "Successfully opened the company page"
    toggle_all = "successfully clicked toggle button"
    company_details = "<----Company Details--->"

    ## AdminCheckCutoffStock.py
    cutoff_stock_in_tons_text = "Cutoff Stock In Tons"
    cutoff_stock_in_tons_value = "cutoff stock in tons is {}"
    cutoff_stock_list = "cutoff stock list is {}"
    stock_greater_than_cutoff_stock = "products stock greater than cutoff stock {}"
    no_new_active_products = "No new products to be added"
    product_stock_less_than_cutoff_stock = "products whose stock is less than cut off stock : {}"
    select_active_product_and_stock = "product and quantity in tons is selected in add stock page"
    add_product_to_products_list = "product added to the products list: {}"

    ## SuperadminCancelledbysystemverification.py
    cutoff_hours_text = "CutOff Hours For Auto Cancellation"
    cutoff_hours_value = "CutOff Hours For Auto Cancellation is : {}"
    placed_orders = "Orders whose status is placed : {}"

    ## vehiclespage
    show_vehicles_page = "successfully show the vehicles page"
    show_vehicles_details = "successfully show the vehicles details: {}"

    ## CheckCostMasterInvoiceAmount.py
    get_invoice_amount = "order_id: {}, bill_id: {}"
    get_invoice_amount_pass = "Successfully retrieved invoice amounts from the Cost Master Page"
    check_orderid_and_invoice_amount = "successfully checked order id and invoice amount in cost master page"

    ## Checkpolicies.py
    click_privacy_policy = "successfully clicked on privacy policy link"
    privacy_policy_text_verify = "Privacy Policy"
    privacy_policy_text = "successfully show the privacy policy page"
    privacy_policy_page = "successfully get the privacy policy page"
    click_terms_and_conditions = "successfully clicked on Terms and conditions"
    terms_and_conditions_text_verify = 'TERMS AND CONDITIONS'
    terms_and_conditions_text = "successfully show the text and condition page"
    terms_and_conditions_page = "successfully get the terms and condition"
    click_refund_policy = "successfully clicked on refund policy"
    refund_policy_text_verify = 'Cancellation and Refund Policy'
    refund_policy_text = "successfully shows the refund policy page"
    refund_policy_page = "successfully gets the refund policy page"

    ## CostMasterPage
    show_cost_master_page = "Cost Master Page is displayed"

    ## Request for settle
    logistics_tab_rfs = "Logistics tab clicked in Request for settle page"
    metal_value_verification = "Successfully verified Metal value in Request for settle with Cost master page"
    logistics_value_verification = "Successfully verified Logistics value in Request for settle with Cost master page"
    rfs_total_orders = "Total order detail displayed on page: {}"
    rfs_due_date = "Due date is : {}"

    #Superadminaddtoncompany.py
    quantity_operational_info = "quantity operational text is: "
    quantity_operational_default_value_info = "Quantity operational option is set to CFT by default and verified successfully."
    company_name_info = "Company name entered: "
    company_status_info = "Clicked on company status."
    company_status_to_active_info = "Changed the status to active."
    comapany_license_no_info = "License No entered: "
    company_gstin_no_info = "Gst in No entered: "
    company_pan_no_info = "Pan number entered: "
    company_quantity_operational_combobox_info = "Clicked on Quantity operational Combobx"
    select_qauntity_oprational_ton_info = "Selected the Ton option from quantity operational combobox"
    company_email_info = "Entered company email: "
    company_mobile_info = "Company mobile number: "
    quantity_operational_text_after_change_info = "Quantity operational text after changing is: "
    company_added_quantity_operational_text = f"Company is added succesfully and Quantity operational is selected as TON"
    quantity_operational_set_to_ton_info = "Quantity operational option set to ton and verified successfully."
    searching_company_info = "Searching comany: "
    company_list_row_info = "Clicked on company list row"
    company_details_data_info = "Company details data: "
    company_list_check_info = "is in company_details_list"
    company_details_verification_info = "Compnay Details verified."
    quantity_operational_text_verification_info = f"Succesfully verified quantity operational text"
    company_added_quantity_operational_ton_info = f"Succesfully Added Company which quantity operations in ton to Servcrust Company Page as Super admin user."


class Error:
    ## Login_page
    search_company_in_partners_tab = None
    chrome = "An error occurred while I launch chrome browser: {}"
    open_oms_home_page = "Error occurred at open oms home page: {}"
    click_login_button = "An error occurred while clicking on the login button: {}"
    login_credentials = "An error occurred while entering login credentials: {}"
    click_signin_button = "An error occurred while clicking on the signin button: {}"
    login_success_message = "An error occurred while showing the 'Login is success' message:  {}"
    assertion_error = "Assertion error: {}"
    user_verification = "An error while verifying user {}: {}"
    logout = "An error occurred during logout: {}"

    ## All Users
    servcrust_tab = "An error occurred while showing all user details for ServCrust_tab: {}"
    admin_tab = "An error occurred while showing all user details for admin_tab: {}"
    others_tab = "An error occurred while showing all user details for others_tab: {}"
    add_user_page = "Error occurred at add user page : {}"
    entered_username = "Failed to shown a username{}"
    user_search = "Failed to search for user{}"
    no_record = "No Records found"

    ###OMS Page
    show_oms_page = "Error occurred at Showing OMS page: {}"
    orderid_search = "Error occurred at enter Order Id in the below order pane search: {}"
    ##menu tab
    OnBoarding_tab ="Error occured at onBoarding page: {}"
    Registration_tab ="Error occured at Registration page:{]"

    # Dashboard
    get_order_data1 = 'Error occurred at Get Order data of "Placed", "Confirmed", "Dispatched", "Delivered": {}'
    get_order_data2 = 'Error occurred at Get Order data of "Companies onBoard", "Quantity Sold in Tons", "COD", "UPI": {}'
    get_order_data3 = 'Error occurred at Get Order data of "CANCELLED BY ADMIN", "CANCELLED BY CUSTOMER", "CANCELLED BY SYSTEM": {}'
    verify_order_data1 = 'Error occurred at verify Order details of "Placed", "Confirmed", "Dispatched", "Delivered": {}'
    verify_order_data2 = 'Error occurred at verify the total companies count: {}'
    verify_order_data3 = 'Error occurred at verify "Quantity Sold in Tons", "COD", "UPI": {}'
    verify_order_data4 = 'Error occurred at verify Order details of "CANCELLED BY ADMIN", "CANCELLED BY CUSTOMER", "CANCELLED BY SYSTEM": {}'

    ## findorder.py
    find_order = "Error occurred at find order: {}"
    random_order_status = "Error occurred at find order status: {}"

    ## Stock page
    class_error = "Error at class : {}"
    show_stock = "Error occurred at show stock : {}"
    enter_order_id = "Failed to send {} in search tab : {}"
    toggle_tons = "Failed to toggle to Tons: {}"
    toggle_cft = "Failed to toggle the button to CFT: {}"
    total_products = "Error occurred at showing total count: {}"
    page_count = "Error occurred at showing page count: {}"
    add_stock_button = "Error at, click on the AddStock Button: {}"
    stock_page = "Error occurred at stock page : {}"
    product_search = "An error occurred while entering the product in search: {}"

    ## Service Ticket Page
    service_ticket_page = "Error occurred at show service ticket page : {}"
    click_add_ticket = "Error occurred at clicking on Addticket button : {}"
    business_tab = "Error occurred at clicking on business tab : {}"
    technical_tab = "Error occurred at clicking on technical tab : {}"
    ticket_details = "Error occurred at getting ticket details : {}"
    entering_ticket_details = "Error occurred at entering ticket details : {}"
    select_ticket_type_as_business = "Error occurred at select ticket type as 'Business': {}"
    select_ticket_type_as_technical = "Error occurred at select ticket type as 'Technical': {}"
    click_save = "Error occurred at clicking on save button : {}"
    verify_ticket_creation = "Error occurred at verify the Ticket creation with the Ticket ID : {}"

    ## Rewards Page
    rewards_page = "Error while showing rewards page: {}"
    get_rewards = "Failed to get rewards for order_id {} : {}"
    total_rewards = "Failed to show the total reward points{}"
    rewards_monetised = "Failed to show the total reward points monetised{}"
    total_amount = "Failed to show the total amount{}"
    orders_points = "Failed to get order id and reward points for each customer : {}"

    ## Database
    verify_details = 'Error occurred at verifying the details : {}'
    values_inserted = "Error occurred while storing values in Sqlite OMS database: {}"
    get_details = "Error occurred while getting row details from database : {}"

    #Pagination
    pagination_error = "Error occurred at Select all types of 'Items per page' and verify the pagination: {}"

    ## Details
    details = "Error occurred at details: {}"
    search = "Error occurred while search : {}"
    select_company = "Error at select company : {}"

    ##Tables and Forms
    orderlist = "Error occurred at reading Order id : {}"
    tablevalues = 'Error occurred at table values : {}'
    formvalues = 'Error occurred at form values : {}'
    onepage = 'Error occurred at one page : {}'

    ## Products list
    master_page = "Error occurred at showing master page : {}"
    products_tab = 'Error clicking on Products Tab : {}'
    products_list = "Error occurred at getting products list : {}"
    count_match = "Error occurred at matching count: {}"
    compare_product_db = "Error occurred at compare product detail with products table in OMS database: {}"

    ##Quantity Tab
    click_quantity_tab = "Error occurred at click on quantities tab: {}"
    search_quantity = "Error occurred at search quantity : {}"
    quantity_tab = 'Error clicking on Quantity Tab : {}'
    mismatch = 'Search input and output result mismatch'
    quantity_list = "Error occurred at Quantities list :{}"
    status = "Error occurred at status details : {}"
    last_modified = "Error occurred at last modified : {}"
    compare_quantity_db = " Error occurred at compare quantity details with quantity table in database: {}"

    ##Experimental tab
    experimental_tab = "Error occurred while clicking experimental tab : {}"
    geo_based_discount = "Error occurred while showing Geo based discount : {}"

    ##Logistics Tab
    click_logistics_tab = "Error occurred at logistic tab: {}"
    add_distance_enabled = "Error occurred at add distance enabled : {}"
    add_distance = "Error occurred at add distance : {}"
    dist_presets = "Error occurred add distance presets : {}"
    company_verify = 'Error occurred at company verification : {}'
    veh_type = 'Error occurred at select vehicle type : {}'
    vehicle_details = "Error occurred at for company Get the VehicleTypes and details: {}"
    base_km = "Error occurred at base km : {}"
    base_km_error = "Error occurred at base kms error message : {}"
    base_charges = "Error occurred at base charge : {}"
    base_km_msg = "Error occurred at base kms is required error message : {}"
    slab1_greater = "Error occurred at slab1 km : {}"
    slab1_less = "Error occurred at enter slab1 kms less than base kms : {}"
    slab1_error = 'Error occurred at error msg for slab1 kms : {}'
    slab1_charges = "Error occurred at slab1 charges : {}"
    slab2_kms = "Error occurred at slab2 km : {}"
    slab2_charges = "Error occurred at slab2 charges : {}"
    round_trip = 'Error occurred at round trip : {}'
    save = 'Error occurred at save button : {}'
    close = "Error occurred at, click on close button: {}"
    cancel = 'Error occurred at click on Cancel : {}'
    click_tab = "Error occurred at click tab : {}"
    edit_logistics = 'Error occurred at edit logistics : {}'
    page_update = "Error occurred at verify if the page is updated with the new vehicle slab rates details: {}"
    max_shipping_dist = "Error occurred at Maximium Shipping Distance"
    select_company_master_page = "Error occurred when selecting the company in masters page: {}"
    flat_discount_add = "Error occurred while adding the radius, discount value, setting the status to active for flat geo based discounts in masterpage: {}"
    edit_button = "Error occured at click on geo based discounts flat discount edit button: {}"
    save_button = "Error occurred at click on save button: {}"

    ##Miscellaneous tab
    click_miscellaneous_tab = "Error at click on Miscellaneous Tab: {}"

    ## Charges Tab
    charges_tab = "Error occurred at Charges tab : {}"
    get_charges = "Error occurred at get the charges : {}"

    # AddAccountantUser.py
    show_all_servcrust_user_details = "An error occurred at show all servcrust user details page: {}"
    click_add_user_button = "An error occurred at click Add User Button: {}"
    add_accountant_user_details = "Error occurred at show AddUser Page and Add an accountant and submit: {}"
    verify_accountant_user_creation = "An error occurred at verify the user creation in Servcrust User details page: {}"

    # AddFinanceHeadUser.py
    add_finance_head_user_details = "Error occurred at show AddUser Page and Add FinanceHead as role and submit: {}"
    verify_finance_head_user_creation = "An error occurred at verify the user creation in Servcrust User details page for financehead: {}"

    # AddManager.py
    add_manager_user_details = "Error occurred at show AddUser Page and Add a manager and submit: {}"
    verify_manager_user_creation = "Error occurred at verify the user creation in User details page: {}"

    # AddOnboardingUser.py
    add_onboarding_user_details = "Error occurred at show AddUser Page and Add Onboarding as role and submit: {}"
    verify_onboarding_user_creation = "An error occurred at verify the user creation in Servcrust User details page for Onboarding: {}"
    select_servcrust_ltd_company = "Error Message at select Servcrust Ltd company: {}"

    # AddOperationsHeadUser.py
    add_operations_head_user_details = "Error occurred at show AddUser Page and Add OperationsHead as role and submit: {}"
    verify_operations_head_user_creation = "An error occurred at verify the user creation in Servcrust User details page for OperationsHead: {}"

    # AddSupportExecutiveUser.py
    add_support_executive_user_details = "Error occurred at show AddUser Page and Add SupportExecutive as role and submit: {}"
    verify_support_executive_user_creation = "An error occurred at verify the user creation in Servcrust User details page for SupportExecutive: {}"

    # AddSupportManagerUser.py
    add_support_manager_user_details = "Error occurred at show AddUser Page and Add SupportManager as role and submit: {}"
    verify_support_manager_user_creation = "An error occurred at verify the user creation in Servcrust User details page for SupportManager: {}"

    # AddUser.py
    add_admin_user_details = "Error occurred at show AddUser Page and Add an Admin and submit: {}"
    verify_admin_user_creation = "Error occurred at verify the user creation in Admin User details page: {}"

    ## AddUserAdmin.py
    added_company_details = "Error occurred at Add company details click next: {}"
    added_address_details = "Error occurred at Add Address details click next: {}"
    add_basic_option = "Error occurred at Add Basic option click next: {}"
    company_submit_button = "Error occurred at Submit and add company: {}"
    company_entered_in_search_box = "Error at verify company prefix of the company added: {}"
    verify_company_creation = "Error at verify company details by selecting company in company list: {}"
    select_new_company_created = "Error occurred at select the new company created: {}"
    company_admin_add_details = "Error occurred at add all user details: {}"
    select_admin_role = "Error occurred at select Admin as the role: {}"
    user_submit_button = "Error occurred at Submit and add user: {}"
    success_message_displayed = "Error occurred at Check Success Message: {}"
    verify_company_admin_user_creation = "Error occurred at verify user detail added in admin user details tab: {}"
    invalid_email = "Error occurred at add email which is not valid: {}"
    displayed_error_message_for_invalid_email = "Error occurred at verify the error message for invalid email: {}"
    invalid_mobile = "Error occurred at add incorrect mobile number: {}"
    displayed_error_message_for_invalid_mobile = "Error occurred at verify the error message for incorrect mobile number: {}"
    invalid_username_and_name = "Error occurred at add incorrect username and name: {}"
    if_enabled_show_error_else_show_success = "Error occurred at if enabled show error message else show success message: {}"
    error_creating_user_message = "Error occurred at Check Error message 'Error creating user': {}"


    ## superadminadduser.py
    add_user_details = "Error occurred at show AddUser Page and Add an {} and submit: {}"
    user_added = "Error occurred at verifying success message after submitting {} details: {}"
    verify_user_creation = "Error occurred at verify the user creation in Servcrust User details page for {}: {}"

    #Superadminaddtoncompany.py
    verify_company_details_qunatity_operational_error = "Error occurred while verifying the comapny details and Quantity Operational when selecting company in company list."
    verify_quantity_operational_error = "An error occured while verifying the quantity operational option: "

    ## Company.py
    show_company_page = "Error occurred at opening company page : {}"
    toggle_all = "Error occurred at Toggle the All button: {}"
    company_details = "Error occurred at show companies and company detail for each company: {}"
    company_count_on_page = "Error occurred at companies on page: {}"
    total_companies_count = "Error occurred at show Total number of companies: {}"
    company_prefix = "Error occurred at getting company name with prefix: {}"

    ## AdminCheckCutoffStock.py
    get_cutoff_stock = "Error at Get the Cutoff Stock in Tons: {}"
    select_company_and_show_stock = "Error occurred at select company {} and show stock detail for the company: {}"
    stock_greater_than_cutoff_stock = "Error at for each product stock is greater than cutoff stock: {}"
    get_stock_detail = "Error at, for each product stock get the stock detail: {}"
    product_stock_less_than_cutoff_stock = "Error at, Stock for the product is less than cut off stock: {}"
    select_active_product_and_stock = "Error occurred at, select the active product and stock in tons: {}"
    add_product_to_products_list = "Error occurred at, add the product to the products list: {}"

    ## SuperadminCancelledbysystemverification.py
    get_cutoff_hours = "Error occurred at, Get the Cutoff Hours: {}"
    order_status_placed = "Error occurred at, Get the orders with order status placed: {}"
    get_created_on_and_add_cutoff_hours = "Error occurred at, Get the created On and add 'CutOff Hours For Auto Cancellation' as Cancellation Time : {}"
    if_order_status_cancelled_by_system = "if order status is Cancelled by System : {}"
    success_message_order_cancelled = 'Error occurred at, show success message " Order is cancelled by the system" : {}'
    error_message_order_not_cancelled = 'Error message that "Orders are not cancelled by system after the CutOff Hours"'

    ## vehiclespage
    show_vehicles_page = "failed to show the vehicles page: {}"
    show_vehicles_details = "failed to show the vehicles details: {}"

    ## CheckCostMasterInvoiceAmount.py
    get_invoice_amount_fail = "Failed to get the invoice amount from the Cost Master Page: {}"
    check_orderid_and_invoice_amount = "failed to check order id and invoice amount in cost master page"

    ## Checkpolicies.py
    click_privacy_policy = "failed to click on privacy policy page {}"
    privacy_policy_text = "failed to show the privacy policy page: {}"
    privacy_policy_page = "failed to get the privacy policy page {}"
    click_terms_and_conditions = "failed to click on terms and policy {}"
    terms_and_conditions_text = "failed to show the terms and conditions {}"
    terms_and_conditions_page = "failed to the terms and condition {}"
    click_refund_policy = "failed to click on refund policy {}"
    refund_policy_text = "failed to shows the refund policy page {}"
    refund_policy_page = "failed to gets the refund policy page {}"

    ## CostMasterPage
    show_cost_master_page = "Error occurred at show cost master page : {}"
    cost_master_company = "Error occurred at selecting company in cost master page:{}"
    metal_invoice_amount = "Error occurred at getting Metal Invoice amount: {}"
    logistics_invoice_amount = "Error occurred at getting Logistics Invoice amount : {}"

    ## CheckPayInAmount.py
    get_all_orders_with_pay_status_paid = "Error occurred at Get all the order details with payment status paid and payment mode as UPI or Others: {}"
    show_Pay_In_page = "Error occurred at show the Payin Page: {}"
    order_type_as_settled_orders = "Error occurred at Orders Type as settled orders: {}"
    search_settled_orders_in_order_pane_search = "Error occurred at Search the settled order in below order pane search: {}"
    toggle_button_to_before_adjusted_values = "Error occurred at Toggle the button to 'Before Adjusted Values': {}"
    get_all_settlements = "Error occurred at Get all the settlements: {}"
    check_order_id_amount_settled_with_ref_no = "Error occurred at Check Order ID and amount settled with Transaction Ref No: {}"
    check_amount_settled_lessthan_invoice_amount = "Error occurred at check the amount settled is less than the invoice amount in oms page: {}"
    fees_deducted_by_payment_gateway = "Error occurred at caluclate the fees deducted by the payment gateway: {}"
    verify_payment_gateway_details = "Error occurred at verify the payment gateway details: {}"

    ## Request for settle
    logistics_tab_rfs = "Error occurred at select the logistics tab: {}"
    aggregate_tab_rfs = "Error occurred at select the Aggregate Tab: {}"
    rfs_payout = "Error occurred at selecting status as payout : {}"
    request_for_settle_page = "Error occurred at Opening request for settle page: {}"
    rfs_search_button = "Error occurred at click on search button: {}"
    get_all_the_Orders = "Error occurred at get all the Orders: {}"
    check_total_matches_with_orders_count = "Error occurred at check the total matches the Total number of orders retrieved: {}"
    metal_invoice_amount_verify = "Error occurred at verifying Metal Invoice amount: {}"
    get_order_details_from_oms_page = "Error occurred at get the order details with the 'order id' from OMS page : {}"
    rfs_values = "Error occurred at getting values in request for payout page: {}"
    logistics_invoice_amount_verify = "Error occurred at verifying Logistics Invoice amount : {}"
    rfs_total_orders = "Error occurred at total order details: {}"
    rfs_verify_count = "Error occurred while verifying total orders on page: {}"
    rfs_due_date = "Error occurred at get due date: {}"

    ## UpdateOrderStatusByPartner
    select_order_status_placed = "Error occurred at select the order status as Placed and click on search: {}"
    no_records_found = "Error occurred at No Records Check Message 'No Records Found': {}"
    when_order_status_placed = "Error occurred at the order status is Placed: {}"
    OrderStatus_Placed_and_PayMode_Others_and_PayStatus_Paid = "Error occurred at Verify if the Order Status is Placed and Pay Mode is Others and Pay Status Paid"
    OrderStatus_Placed_and_PayMode_Pay_on_Delivery = "Error occurred at Verify if the Order Status is Placed and Pay Mode is Pay on Delivery"
    click_confirm = "Error occurred at Click on Confirm Button: {}"
    when_order_status_confirmed = "Error occurred at the order status is confirmed: {}"
    click_on_add_trip = "Error occurred at Click on AddTrip Button: {}"
    Select_Vehicle_Type = "Error occurred at Select_Vehicle_Type: {}"
    Error_Message_No_Vehicles_available = "Error occurred at Error Message 'No Vehicles available': {}"
    Show_Message_No_Vehicles = "Error occurred at Show Message 'No Vehicles': {}"
    provide_trip_details = "Error occurred at Provide the Trip details: {}"
    click_on_dispatch = "Error occurred at Click on Dispatch Button: {}"
    Enter_ManualDC_No = "Error occurred at Enter ManualDC No: {}"
    Click_on_Yes = "Error occurred at Click on Yes: {}"
    Click_on_Delivered = "Error occurred at Click on Delivered: {}"
    Click_Yes_to_Confirm_Delivery = "Error occurred at Click Yes to Confirm Delivery: {}"
    Payment_Mode_is_POD = "Error occurred at Payment Mode is Pay on Delivery: {}"
    Click_Update_Payment_Status_Button = "Error occurred at Click Update Payment Status Button: {}"
    Click_Yes_to_Change_the_Payment_Status = "Error occurred at Click Yes to Change the Payment Status: {}"
    Check_Payment_status_Success_Message = "Error occurred at Check Payment status Success Message : {}"



class Tables:
    OMS_table = '''
                        CREATE TABLE IF NOT EXISTS OMS_cancelled_Orders (
                            ID TEXT,
                            Product TEXT,
                            Quantity TEXT,
                            Unit TEXT,
                            Bill TEXT,
                            Pay_Mode TEXT,
                            Pay_status TEXT,
                            Created_on TEXT,
                            Order_status TEXT,
                            Distance TEXT,
                            Phone_No TEXT
                        )
                        '''
    OMS_table1 = '''
                          CREATE TABLE IF NOT EXISTS OMS_cancelled_Orders_accountant (
                              ID TEXT,
                              Product TEXT,
                              Quantity TEXT,
                              Unit TEXT,
                              Bill TEXT,
                              Pay_Mode TEXT,
                              Pay_status TEXT,
                              Created_on TEXT,
                              Order_status TEXT,
                              Distance TEXT
                          )
                          '''

    ticket_details_table = '''
                            CREATE TABLE IF NOT EXISTS ticket_details (
                                Ticket_ID TEXT,
                                Ticket_Description TEXT,
                                Priority TEXT,
                                Company_name TEXT,
                                Customer_name TEXT,
                                Requested_By TEXT,                                
                                Phone_number TEXT,
                                Order_ID TEXT,
                                Ticket_Status TEXT,
                                Created_on TEXT
                            )
                            '''

    order_rewards = '''
                   CREATE TABLE IF NOT EXISTS order_rewards (
                       Order_ID TEXT,
                       Customer_Mobile TEXT,
                       Created_On TEXT,
                       CFT_to_Points TEXT,
                       KM_to_Points TEXT,
                       Total_Points_Awarded TEXT,
                       Total_Points_Monetised TEXT,
                       Amount TEXT
                   )
                   '''
    logistics_table = '''
                               CREATE TABLE IF NOT EXISTS master_logistics (
                                   Vehicle_Type TEXT,
                                   Base_km_upto TEXT,
                                   Base_charge TEXT,
                                   Slab1_km TEXT,
                                   Slab1_charge TEXT,
                                   Slab2_km TEXT,
                                   Slab2_Charge TEXT,
                                   Round_Trip TEXT,
                                   last_modified_date TEXT,
                                   modified_by TEXT
                               )
                               '''
    stock_table = '''
            CREATE TABLE IF NOT EXISTS company_products (
            product TEXT,
            manual_stock TEXT,
            machine_stock TEXT,
            total_stock TEXT
        )
        '''
    active_products_table = '''
                    CREATE TABLE IF NOT EXISTS Company_active_products (
                        Company_name TEXT,
                        Active_products TEXT
                    )
                    '''
    products_table = '''
        CREATE TABLE IF NOT EXISTS master_product (
            product TEXT,
            Status TEXT,
            Price_per_unit TEXT,
            last_modified_date TEXT,
            modified_by TEXT
        )
        '''
    quantity_table = '''
            CREATE TABLE IF NOT EXISTS master_quantities (
                Quantity TEXT,
                Status TEXT,
                last_modified_date TEXT,
                modified_by TEXT
            )
            '''
    companies_table = '''
            CREATE TABLE IF NOT EXISTS active_companies (
                No TEXT,
                Company TEXT,
                Status TEXT,
                License_No TEXT,
                Prefix TEXT
            )
            '''
    companies_prefix_table = '''
            CREATE TABLE IF NOT EXISTS companies_prefix_table (
                Company TEXT,
                Status TEXT,
                License_No TEXT,
                Prefix TEXT
            )
            '''

    experimental_table = '''
           CREATE TABLE IF NOT EXISTS geo_based (
               Discount_name TEXT,
               Radius TEXT,
               Discount_value TEXT,
               Status TEXT,
               last_modified_date TEXT,
               modified_by TEXT
           )
           '''
    charges_table = '''
                CREATE TABLE IF NOT EXISTS master_charges (
                    Name TEXT,
                    Preference_value TEXT,
                    created_date TEXT,
                    last_modified_date TEXT,
                    modified_by TEXT
                )
                '''
    preferences_table = '''
            CREATE TABLE IF NOT EXISTS preferences (
                name TEXT,
                value TEXT,
                created_date TEXT,
                last_modified_date TEXT,
                modified_by TEXT
            )
            '''

    cost_master_table = '''
                   CREATE TABLE IF NOT EXISTS cost_master (
                       Order_ID TEXT,
                       Date TEXT,
                       Metal_Value TEXT,
                       Logistics_value TEXT,
                       Total_invoice TEXT,
                       Platform_and_accounting_charges TEXT,
                       Platform_and_Service_gst_charges TEXT,
                       Tax_Deduction TEXT,
                       Net_payment TEXT
                   )
                   '''

    aggregate_payout_table = '''
                   CREATE TABLE IF NOT EXISTS aggregate_payout (
                       Order_ID TEXT,
                       Payment_mode TEXT,
                       Aggregate_amount TEXT,
                       Payment_status TEXT,
                       Net_payment TEXT,
                       Order_status TEXT,
                       Due_date_to_pay TEXT
                   )
                   '''

    logistics_payout_table = '''
                       CREATE TABLE IF NOT EXISTS logistics_payout (
                           Order_ID TEXT,
                           Payment_mode TEXT,
                           Aggregate_amount TEXT,
                           Payment_status TEXT,
                           Net_payment TEXT,
                           Order_status TEXT,
                           Due_date_to_pay TEXT
                       )
                       '''

# mobile profile table
profile_table_query = """
                CREATE TABLE IF NOT EXISTS profile_table (
                    Company TEXT,
                    Name TEXT,
                    Role TEXT,
                    Status TEXT,
                    Email TEXT,
                    Mobile TEXT,
                    Notifications TEXT,
                    Created_On TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """
class Insert:
    OMS_table = '''
                        INSERT INTO OMS_cancelled_Orders (ID,Product,Quantity,Unit,Bill,Pay_Mode,Pay_status,Created_on,Order_status,Distance,Phone_No) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?)
                        '''
    OMS_table1 = '''
                            INSERT INTO OMS_cancelled_Orders_accountant (ID,Product,Quantity,Unit,Bill,Pay_Mode,Pay_status,Created_on,Order_status,Distance) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?)
                            '''
    ticket_details_table = '''INSERT INTO ticket_details (Ticket_ID, Ticket_Description, Priority, Company_name, 
            Customer_name, Requested_By, Phone_number, Order_ID, Ticket_Status, Created_on) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '''

    order_rewards = '''INSERT INTO order_rewards (Order_ID, Customer_Mobile, Created_On, CFT_to_Points, KM_to_Points, 
        Total_Points_Awarded, Total_Points_Monetised, Amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

    logistics_table = '''
                               INSERT INTO master_logistics (Vehicle_Type,Base_Km_upto,Base_charge,Slab1_km,Slab1_charge,Slab2_km,Slab2_charge,Round_Trip,last_modified_date,modified_by) VALUES (?, ?, ?,?, ?, ?,?, ?, ?, ?)
                               '''
    stock_table = '''
           INSERT INTO company_products (product, manual_stock, machine_stock, total_stock) VALUES (?, ?, ?, ?)
           '''
    active_products_table = '''
                        INSERT INTO Company_active_products (Company_name, Active_products) 
                        VALUES (?, ?)
                        '''

    products_table = '''
    INSERT INTO master_product (product,Status,Price_per_unit,last_modified_date,modified_by) VALUES (?, ?, ?,?,?)
    '''
    query_products = '''SELECT * FROM master_product WHERE product = ?'''
    quantity_table = '''
                INSERT INTO master_quantities (Quantity,Status,last_modified_date,modified_by) VALUES (?, ?, ?,?)
                '''
    query_quantity = '''SELECT * FROM master_quantities WHERE Quantity = ?'''
    companies_table = '''
           INSERT INTO active_companies (No, Company, Status, License_No, Prefix) VALUES (?, ?, ?, ?, ?)
           '''
    company_prefix_table_insert_query = '''
            INSERT INTO companies_prefix_table (Company, Status, License_No, Prefix) VALUES (?, ?, ?, ?)
            '''

    experimental_table = '''
               INSERT INTO geo_based (Discount_name,Radius,Discount_value,Status,last_modified_date,modified_by) VALUES (?, ?, ?,?,?,?)
               '''
    charges_table = '''
                INSERT INTO master_charges (Name, Preference_value,created_date,last_modified_date,modified_by) VALUES (?, ?, ?,?,?)
                '''
    preferences_table = '''
            INSERT INTO preferences (name,value,created_date,last_modified_date,modified_by) VALUES (?, ?, ?, ?, ?)
            '''
    cost_master_table = '''INSERT INTO cost_master (Order_ID, Date, Metal_Value, Logistics_value, Total_invoice, 
            Platform_and_accounting_charges, Platform_and_Service_gst_charges, Tax_deduction, Net_payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    aggregate_payout_table = '''
        INSERT INTO aggregate_payout (Order_ID, Payment_mode, Aggregate_amount, Payment_status, Net_payment, Order_status, Due_date_to_pay) VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
    logistics_payout_table = '''
            INSERT INTO logistics_payout (Order_ID, Payment_mode, Aggregate_amount, Payment_status, Net_payment, Order_status, Due_date_to_pay) VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
#mobile profile table
    profile_insert_query = """
                    INSERT INTO profile_table (Company, Name, Role, Status, Email, Mobile, Notifications, Created_On)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """