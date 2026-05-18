Feature: Logout Functionality

Scenario: Successful logout
  Given user is logged in
  When user clicks logout button
  Then user should be redirected to login page