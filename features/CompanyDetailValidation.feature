Feature: Company Detail Validation As a user,I want to be able to log in to the application as a partner
  So that I can validate the company details

  Scenario Outline: Compare the partner company details of mobile application with web.
    Given I launch the application
    When I am on the main page of the application
    Then I enter my username and password
    When I enter "<username>" and "<password>"
    Then click on sign-in button
    And I should redirect to home screen of the application
    When I click to profile button
    Then I Getting the company details
    And Logout
#    And close the driver of mobile application
Examples:
    |username||password|
    |venkatesh||Test@12345|
##    |         ||123          |
##
  Scenario Outline: Launch the browser and land on servcrust and search for company that retrived from mobile and compare with web company details
    Given I launch chrome browser
    When open oms home page
    And Click on Login Button
    And Enter username "<username>" and password "<password>" for "<user>" user
    And Click the Sign In button
    And show the success message
    Then Navigate to Onboarding tab  --> Registration tab --> Partners tabs
    And In partners tab search for the company that retrived from mobile application
    And get the company details from the web
    And the company details retrieved from the mobile application should match the company details with web
   Examples: Credentials
        | user        | | username | password ||username|
         | superadmin  || Rupendhra  | Test@1234 ||venkatesh|