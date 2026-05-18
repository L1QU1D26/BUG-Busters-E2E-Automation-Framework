Feature: Cart Management

  Scenario: Verify user can add product to cart
    Given user navigates to the "Mens Wear" category
    When user adds a product to the cart
    Then cart count should be updated successfully

  Scenario: Verify added product is displayed in cart
    Given user has added a product to the cart
    When user opens the cart page
    Then added product should be displayed in cart summary

  Scenario: Verify user can update product quantity in cart
    Given user has product in the cart
    When user updates the product quantity
    Then updated quantity should be displayed correctly

  Scenario: Verify user can remove product from cart
    Given user has product in the cart
    When user removes the product from the cart
    Then product should be removed successfully

  Scenario: Verify cart total amount is calculated correctly
    Given user has multiple products in the cart
    When user opens the cart page
    Then total amount should be displayed correctly