import unittest
from utils.helpers import validate_position_limit

class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

class TestPositionLimit(unittest.TestCase):
    def test_valid_team(self):
        players = [
            Player("F1", "Forward"),
            Player("F2", "Forward"),
            Player("F3", "Forward"),
            Player("M1", "Midfield"),
            Player("M2", "Midfield"),
            Player("M3", "Midfield"),
            Player("M4", "Midfield"),
            Player("D1", "Defender"),
            Player("D2", "Defender"),
            Player("D3", "Defender"),
            Player("D4", "Defender"),
            Player("D5", "Defender"),
            Player("G1", "Goalkeeper"),
            Player("G2", "Goalkeeper")
        ]
        team = Team("Valid FC", players)
        self.assertTrue(validate_position_limit(team))

    def test_exceeds_forward_limit(self):
        players = [
            Player("F1", "Forward"),
            Player("F2", "Forward"),
            Player("F3", "Forward"),
            Player("F4", "Forward"),  # Exceeds limit
            Player("M1", "Midfield"),
            Player("G1", "Goalkeeper")
        ]
        team = Team("Overload FC", players)
        self.assertFalse(validate_position_limit(team))

if __name__ == "__main__":
    unittest.main()
