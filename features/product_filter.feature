Feature: Product Filtering Functionality

  Background:
    Given the user is logged into the application and on shop page
    And the user navigates to the Men's Wear category page

  @filter @positive
  Scenario: Apply single category filter
    Given the user notes the initial product count
    When the user selects the "Formal" filter checkbox
    Then the product count should be updated and be less than the initial count
    And the products displayed should be updated

  @filter @positive
  Scenario: Apply multiple category filters
    Given the user selects the "Formal" filter checkbox
    And the user selects the "Footwear" filter checkbox
    And the user notes the initial product count
    When the user selects the "$0 - $100" filter checkbox
    Then the product count should change accordingly

  @filter @negative
  Scenario: Apply incompatible filters yielding no products
    When the user selects the "Footwear" filter checkbox
    And the user selects the "Red" filter checkbox
    Then no products should be displayed in the list
