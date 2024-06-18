Feature: User loginAs a user,I want to be able to log in to the application as a partner So that I can access partner-specific features

  Scenario Outline: User fails to log in with invalid credentials
    Given I launch the application
    And I am on the main page of the application
    When I enter "<username>" and "<password>"
    And I click on the sign-in button
    Then I should see an error message indicating that the login failed
    And close the application


    Examples:
      | username       | password            |
      | john_doe       | JohnDoe@!           |
      | jane.doe       | JaneDoe#$%^         |
      | user123        | User123!@#          |
      | partner_xyz    | PartnerXYZ&*        |
      | test_user      | TestUser123$        |
      | invalid_user   | InvalidPass!@#      |
      | wrong_user     | WrongPassword*&     |
      | special_user   | SpecialPass$%^&     |
      | temp_partner   | TempPartner12!@     |
      | new_user       | NewUser123#         |
#      | demo_user      | DemoPass!@#123      |
#      | example_user   | ExamplePass%^&123   |
#      | invalid_partner| InvalidPartner@!4567|
#      | incorrect_user | IncorrectPass123!   |
#      | random_user    | RandomPassword$%^&  |
#      | temp_user      | TempPass!@#567      |
#      | trial_partner  | TrialPartner123$    |
#      | sample_user    | SamplePass*&789     |
#      | fake_partner   | FakePartner!@#890   |
#      | dummy_user     | DummyPass123$%^     |
#      | test_partner   | TestPartner&*123    |
#      | example_partner| Example123!@#Partner|
#      | invalid_demo   | InvalidDemo$%^&123  |
#      | incorrect_demo | IncorrectDemo&*456  |
#      | random_demo    | RandomDemo123!@#    |
#      | temp_demo      | TempDemo$%^&567     |
#      | trial_demo     | TrialDemo789!@#     |
#
