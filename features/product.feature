Feature: Product Functionality


  @product
  Scenario: View product details

    Given the user is on the mens products page
    When the user clicks on a product
    Then product details should be displayed


  @product
  Scenario: Add mens product to cart

    Given the user is viewing a mens product
    When the user clicks Add to Cart
    Then the product should be added to the cart


  @product
  Scenario: Validate mens products are displayed

    Given the user is on the mens products page
    Then products should be visible


  @product
  Scenario: Validate womens products page

    Given the user is on the womens products page
    Then products should be visible


  @product
  Scenario: Validate kids products page

    Given the user is on the kids products page
    Then products should be visible


  @product
  Scenario: Validate electronics products page

    Given the user is on the electronics products page
    Then products should be visible


  @product
  Scenario: Validate cart badge updates

    Given the user is viewing a mens product
    When the user clicks Add to Cart
    Then cart count badge should update