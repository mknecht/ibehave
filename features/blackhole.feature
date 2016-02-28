Feature: Detecting gravitational waves.

  Scenario: Two black holes generate a detectable wave.
    Given we have 2 black holes
     And a big L
     When the holes collide
     Then we detect shockwaves