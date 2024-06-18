Feature: User logout As a user,
  I want to be able to logout of the application as a partner

  Scenario: User logout successfully
    Given I launch the application
    And I am on the main page of the application
    When I enter my username and password
    And I click on the sign-in button
    Then I should redirect to home screen of the application
    And I click on logout button
    And I should redirect to the login page
