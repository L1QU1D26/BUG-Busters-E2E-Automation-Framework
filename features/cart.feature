Feature: Cart Management

  Scenario Outline: Verify user can add product to cart from different categories

    Given user navigates to the <category> category
    When user adds <product_number> to the cart
    Then cart count should be updated successfully

    Examples:
      | category    | product_number |
      | Mens Wear   | 4              |
      | Electronics | 6              |
      | Kids Wear   | 3              |
  

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