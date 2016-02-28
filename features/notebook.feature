Feature: User Profile
  Scenario: Email address is changed
     Given Tina is logged in
      When Tina changes her email to tina@example.com
      Then in her user profile Tina sees tina@example.com as her email