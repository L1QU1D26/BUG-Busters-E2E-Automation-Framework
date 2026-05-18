Feature: Product Functionality

Scenario: View product details
    Given the user is on the products page
    When the user clicks on a product
    Then product details should be displayed

Scenario: Add product to cart
    Given the user is viewing a product
    When the user clicks Add to Cart
    Then the product should be added to the cart