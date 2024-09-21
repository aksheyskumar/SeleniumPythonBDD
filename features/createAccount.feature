Feature: Create new account

  @pmm
  Scenario: Create new account with invalid phonenumber
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields
    And Click Continue
    Then User should be navigated to the Puzzle Page

  @pmm
  Scenario: Create new account with empty name field
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields except your name
    And Click Continue
    Then System should throw a warning "Enter your name"

  @pmm
  Scenario: Create new account with empty phonenumber field
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields except mobile number/email
    And Click Continue
    Then System should throw a warning "Enter your email address or mobile phone number"

  @pmm
  Scenario: Create new account with empty password field
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields except password
    And Click Continue
    Then System should throw a warning "Enter a password"

  @pmm
  Scenario: Create new account with empty reenter password field
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields except Re-enterpassword
    And Click Continue
    Then System should throw a warning "Type your password again"

  @pmm
  Scenario: Create new account with Mismatched passwords
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Fill all the required fields with different password values
    And Click Continue
    Then System should throw a warning "Passwords do not match"

  @pmm1
  Scenario: Create new account with all fields empty
    Given Navigate to the login URL
    When Click Create your Amazon Account button
    And Click Continue
    Then System should throw  warning in all fields