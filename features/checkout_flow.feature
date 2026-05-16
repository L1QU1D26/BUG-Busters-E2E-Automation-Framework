Feature: Checkout Flow

  As a registered user
  I want to complete the checkout process
  So that I can place an order successfully

  Background:
    Given user launches the application "https://shop.qaautomationlabs.com/"
    And user logs in with valid credentials
    And user adds a product to the cart
    And user navigates to the cart page

  Scenario: Successful checkout with valid details
    When user clicks on checkout button
    And user enters valid shipping details
      | first_name | Ganesh |
      | last_name  | Kumar  |
      | address    | Mumbai Street |
      | city       | Mumbai |
      | zip_code   | 400001 |
    And user clicks on continue button
    And user places the order
    Then order confirmation page should be displayed
    And order number should be generated