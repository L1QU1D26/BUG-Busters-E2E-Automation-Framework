Feature: Authentication API Workflows

  Scenario: Verify successful login with valid credentials
    Given user sends login request with valid credentials
    Then login response status code should be 200
    And authentication token should be generated

  Scenario: Verify login with invalid password
    Given user sends login request with invalid password
    Then login response status code should be 401
    And error message should be displayed

  Scenario: Verify login with empty email field
    Given user sends login request without email
    Then login response status code should be 400
    And validation message for email should be displayed

  Scenario: Verify login with empty password field
    Given user sends login request without password
    Then login response status code should be 400
    And validation message for password should be displayed

  Scenario: Verify login with invalid email format
    Given user sends login request with invalid email format
    Then login response status code should be 400
    And invalid email format message should be displayed

Feature: Product API Workflows

  Scenario: Verify all products are fetched successfully
    Given user sends request to fetch all products
    Then products response status code should be 200
    And product list should be returned

  Scenario: Verify product details by valid product ID
    Given user sends request with valid product ID
    Then product details response status code should be 200
    And product details should be displayed

  Scenario: Verify product details with invalid product ID
    Given user sends request with invalid product ID
    Then product response status code should be 404
    And product not found message should be displayed