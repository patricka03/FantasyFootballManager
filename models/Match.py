from models.team import Team
from models.player import Player

class Match:

    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.score = {'home_team': 0, 'away_team': 0}
        self.player_performances = [1,2,3,4,5]

    def match_result(self, home_goal, away_goal):
        print(f"{self.home_team} ({home_goal}) - ({away_goal}) {self.away_team}")

    def assign_points(self, player_performance, user_team):
        total_points = 0

        for performance in player_performance:
            player = performance["player"]
            goals = performance.get("goals", 0)
            assists = performance.get("assists", 0)
            clean_sheet = performance.get("clean_sheet", False)

            if player in user_team._players:
                # Update player stats
                player._goals = goals
                player._assists = assists
                player._clean_sheets = clean_sheet

                # Calculate and add points
                points = player.calculate_points(goals, assists, clean_sheet)
                total_points += points
                print(f"{player.name} earned {points} points")

        print(f"\nTotal points earned from this fixture: {total_points}")
        return total_points

palmer = Player('Cole Palmer', 'Midfielder', 'Chelsea')
jackson = Player('Nico Jackson', 'Forward', 'Chelsea')
chilwell = Player('Ben Chilwell', 'Defender', 'Chelsea')

user_team = Team('My Fantasy XI', 'Pat')
user_team.add_player(palmer)
user_team.add_player(jackson)
user_team.add_player(chilwell)

chel_vs_united = Match('Chelsea FC', 'Manchester United')
chel_vs_united.match_result(2, 1)

player_performance = [
    {"player": palmer, "goals": 1, "assists": 1, "clean_sheet": True},
    {"player": jackson, "goals": 0, "assists": 1, "clean_sheet": True},
    {"player": chilwell, "goals": 0, "assists": 0, "clean_sheet": True}
]

chel_vs_united.assign_points(player_performance, user_team)
