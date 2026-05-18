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