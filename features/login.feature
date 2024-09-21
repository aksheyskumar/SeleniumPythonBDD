Feature:

  @completed
  Scenario: Login as valid Community User
    Given Navigate to the login URL
    When Enter the Phonenumber
    And Click the Continue button
    And Enter the Password
    And Click the login button
    Then User should be logged in Successfully

  @completed
  Scenario: Login as invalid Community User
    Given Navigate to the login URL
    When Enter the invalid Phonenumber
    And Click the Continue button
    Then Warning message should popup - We cannot find an account with that mobile number

  @completed
  Scenario: Login without phone number
    Given Navigate to the login URL
    When Leave the phone number field empty
    And Click the Continue button
    Then Warning message should popup - Enter your e-mail address or mobile phone number


  