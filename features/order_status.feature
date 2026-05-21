Feature: Order Confirmation

  Background:
    Given user launches the application "https://shop.qaautomationlabs.com/"
    And user logs in with valid credentials
    And user adds a product to cart
    And user navigates to checkout page
    And user enters valid checkout details
      | first_name | Ganesh    |
      | last_name  | Jangam    |
      | address    | Lingampet |
      | city       | Kamareddy |
      | state      | Telangana |
      | zip_code   | 503108    |
    And clicks on the continue button
    Then user should see the order confirmation

    
  Scenario: Verify place order button is visible on confirm page
    Then the place order button should be visible

  Scenario: Verify successful order placement
    When user clicks on place order button
    Then the thank you page should load successfully
    And a thank you message "Thank You for Your Order!" should be displayed