Feature: Login Functionality

@login
Scenario: Successful login
Given user open login page
When user enters valid username and password
Then user should navigate to inventory page

@invalidlogin
Scenario: Invalid login
Given user open login page
When user enters invalid credentials
Then login error should display

@emptyuser
Scenario: Login with empty username
Given user open login page
When user enters empty username and valid password
Then empty email error should display


@emptypass
Scenario: Login with empty password
Given user open login page
When user enters valid username and empty password
Then empty password error should display

@logout
Scenario: Successful logout

Given user open login page
When user enters valid username and password
And user clicks logout button
Then user should navigate to login page

