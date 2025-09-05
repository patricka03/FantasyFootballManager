from models.team import Team
from models.player import Player

class League:

    def __init__(self, league_name):
        self.league_name = league_name
        self.league_teams = []

    def add_team(self, team):
        self.league_teams.append(team)
        print(f"{team.team_name} has been added to {self.league_name} league")

    def remove_team(self, team):
        if team in self.league_teams:
            self.league_teams.remove(team)
            print(f"{team.team_name} has been removed from {self.league_name}")

    def rank_teams(self):
        ranked = sorted(self.league_teams, key=lambda team: team.calculate_team_score(), reverse=True)
        print(f"\n🏆 {self.league_name} Standings:")
        for position, team in enumerate(ranked, start=1):
            print(f"{position}. {team.team_name} — {team.calculate_team_score()} pts")


# fantasy_league = League('Fantasy League')
# print(fantasy_league.league_name)#---> This works
#
# Chelsea = Team('Chelsea', 'Enzo Marisca')
# Fantasy = Team('Fantasy', 'Pat Marlo')
#
# fantasy_league.add_team(Chelsea)
# fantasy_league.add_team(Fantasy)
# fantasy_league.remove_team(Fantasy)

Chelsea = Team('Chelsea', 'Enzo Marisca')

palmer = Player('Cole Palmer', 'Midfielder', 'Chelsea')
palmer._goals = 5
palmer._assists = 2
palmer._clean_sheets = 1

jackson = Player('Nico Jackson', 'Forward', 'Chelsea')
jackson._goals = 3
jackson._assists = 1
jackson._clean_sheets = 0

Chelsea.add_player(palmer)
Chelsea.add_player(jackson)
Chelsea.remove_player(jackson)

print(Chelsea.players)
print(Chelsea.calculate_team_score())



fantasy_league = League('Fantasy League')
print(fantasy_league.league_name)#---> This works

Chelsea = Team('Chelsea', 'Enzo Marisca')
Fantasy = Team('Fantasy', 'Pat Marlo')

fantasy_league.add_team(Chelsea)
fantasy_league.add_team(Fantasy)
fantasy_league.rank_teams()