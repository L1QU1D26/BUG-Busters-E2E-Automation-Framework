Feature: Address Validation during Checkout

  Background:
    Given user launches the application "https://shop.qaautomationlabs.com/"
    And user logs in with valid credentials
    And user adds a product to cart
    And user navigates to checkout page

  Scenario: Empty address validation
    When user clicks on checkout button
    And user leaves address field empty
    And user clicks on continue button
    Then error message "Address is required" should be displayed

  Scenario: Missing mandatory fields validation
    When user leaves any mandatory fields empty
    And user clicks on continue button
    Then validation errors should be displayed for all required fields