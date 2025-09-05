from models.team import Team
from models.player import Player

class Match:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.score = {'home_team': 0, 'away_team': 0}
        self.player_performances = [1,2,3,4,5]

    def match_result(self, home_goal, away_goal):
        print(f"{self.home_team}: {home_goal} - {away_goal} : {self.away_team}")

    def assign_points(self):
        points = 0



# chel_vs_united = Match('Chelsea FC', 'Manchester United')
# print(chel_vs_united.away_team)
#
# chel_vs_united.match_result(2,1)