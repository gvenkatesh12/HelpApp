Feature: Whatsapp Order placement in the తెలుగు language
  Scenario: Whatsapp Order placement in the తెలుగు language
    Given I send "Hi"
    Then Show "Servcrust కి స్వాగతం దయచేసి భాషను ఎంచుకోండి" Click to Select
    And Select "తెలుగు"
    When show దయచేసి GPS స్థానాన్ని పంపండి
    And add "latitude" and "longitude"
    Then show కంకర రకాన్ని ఎంచుకోండి
    When select product
    Then show కావాల్సిన పరిమాణాన్ని ఎంచుకోండి(CFT)
    When select quantity
    Then show  చెల్లించాల్సిన మొత్తం
    When show discount claimed
    And Show payment options
    And select payment option
    When Payment option is pay on delivery
    Then Show Order placed message with order id