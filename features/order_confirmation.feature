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
      | zip_code   | 503108    |

  Scenario: Verify successful order placement and order number generation
    When user clicks on place order button
    Then the order confirmation page should load successfully
    And a success message "Thank you. Your order has been received." should be displayed
    And a valid order number should be generated
    And the order summary including date and total should be visible