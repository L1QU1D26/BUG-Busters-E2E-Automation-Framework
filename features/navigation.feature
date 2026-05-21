Feature: Navigation Functionality


  @navigation
  Scenario: Navigate to Mens Wear section

    Given user is logged into the application
    When user clicks Mens Wear from Shop menu
    Then Mens Wear page should be displayed


  @navigation
  Scenario: Open cart page

    Given user is logged into the application
    When user clicks cart icon
    Then cart page should be displayed


  @navigation
  Scenario: Navigate back to shop page

    Given user is on mens wear page
    When user clicks Go To Back button
    Then shop page should be displayed