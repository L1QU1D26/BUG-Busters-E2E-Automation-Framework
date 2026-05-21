Feature: Navigation Functionality


  @navigation
  Scenario: Navigate to all category sections slowly

    Given user is logged into the application
    When user slowly visits all Shop categories
    Then Electronics page should be displayed
    When user clicks cart icon
    Then cart page should be displayed
    When user clicks Go To Back button
    Then shop page should be displayed
