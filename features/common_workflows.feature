Feature: Common Application Workflows

  Scenario: Verify application launches successfully
    Given user launches the application
    Then homepage should load successfully

  Scenario: Verify homepage navigation menu
    Given user opens the application
    Then navigation menu should be visible

  Scenario: Verify homepage title
    Given user launches the application
    Then homepage title should match expected value