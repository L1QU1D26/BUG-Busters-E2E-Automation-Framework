Feature: Website Navigation

Scenario: Navigate to products page
    Given the user is on the homepage
    When the user clicks on Products menu
    Then the products page should be displayed

Scenario: Navigate to cart page
    Given the user is logged in
    When the user clicks on Cart icon
    Then the cart page should open