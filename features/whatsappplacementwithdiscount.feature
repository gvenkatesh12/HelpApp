Feature: Whatsapp Order placement using pay on Delivery with invoice calculation
  Scenario: Place an order using Pay on delivery option using Whatsapp and show discount
    Given I send "Hi"
    And Choose Language
    And Select Language
    And verify the messages in Language
    When show Orders Type
    And Select "New Order"
    And show "Please share the Delivery Location (GPS)"
    And add "latitude" and "longitude"
    And Show Place order for order types
    And select product
    And show quantity in CFT
    And select quantity
    When previous menu is selected
    And Show Place order for order types
    And show total amount to pay after discount
    And show discount claimed
    And Show payment options
    And select payment option
    When Payment option is pay on delivery
    Then Show Order placed message with order id
