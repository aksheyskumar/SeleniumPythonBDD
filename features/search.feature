Feature: Search functionality

  @search1
  Scenario: Search valid product
    Given Navigate to the application URL
    When Enter Valid product in the search box
    And Click search button
    Then Searched product should be available as results

  @search1
  Scenario: Search invalid product
    Given Navigate to the application URL
    When Enter invalid product in the search box
    And Click search button
    Then Proper search message should be shown in search results


