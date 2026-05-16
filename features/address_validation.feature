Feature: Address Validation during Checkout

  As a user
  I want validation on address fields
  So that incorrect data is not accepted

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

  Scenario: Invalid zip code validation
    When user enters checkout details
      | first_name | Ganesh |
      | last_name  | Kumar |
      | address    | Mumbai Street |
      | city       | Mumbai |
      | zip_code   | ABC123 |
    And user clicks on continue button
    Then error message "Invalid Zip Code" should be displayed

  Scenario: Missing mandatory fields validation
    When user leaves all mandatory fields empty
    And user clicks on continue button
    Then validation errors should be displayed for all required fields