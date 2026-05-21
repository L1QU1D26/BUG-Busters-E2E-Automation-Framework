Feature: Product Functionality

Scenario: Browse all product categories slowly
    Given the user is logged in for product testing
    When the user slowly checks products in all categories
    Then the product should be added to the cart
