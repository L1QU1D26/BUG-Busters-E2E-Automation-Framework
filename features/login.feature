Feature: User login
  As a registered user
  I want to log in to the ecommerce site
  So that I can access protected features and place orders

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid email and password
    And the user submits the login form
    Then the user should be redirected to the account dashboard
    And the user should see a welcome message

  Scenario: Login fails with invalid credentials
    Given the user is on the login page
    When the user enters an invalid email or password
    And the user submits the login form
    Then the user should see an authentication error message
