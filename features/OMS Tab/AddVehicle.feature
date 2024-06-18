Feature: Searching for a Vehicle by Number
  As a user,
  I want to be able to log in to the application as a partner
  So that I can add vehicles

  Scenario: User logs in successfully
    Given i launch the application
    When I am on the main page of the application
    Then I enter my username and password
    When I enter "<username>" and "<password>"
    Then click on sign-in button
    And I should redirect to home screen of the application

  Scenario: User searches for a vehicle by its number
    Given Navigate to Vehicles tab
    When click on add vehicle button
    And "Add Vehicle" pop up should be displayed
    When add the vehicle number, owner name, Driver Phone number, Vehicle type, CFT, Status
    Then I click on confirm
    And verify the message "Vehicle added"
    And check the vehicle is added by searching the added vehicle number in search bar
    And close the application
