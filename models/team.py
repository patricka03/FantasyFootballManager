from models.player import Player

class Team:
    def __init__(self, team_name, manager_name):
        self.team_name = team_name
        self.manager_name = manager_name
        self._players = []

    @property
    def players(self):
        return [player.name for player in self._players]

    def add_player(self, player):
            self._players.append(player)
            print(f"{player.name} has been added to {self.team_name} players list")

    def remove_player(self, player):
        if player in self._players:
            self._players.remove(player)
            print(f"{player.name} has been removed from {self.team_name} players list")
        else:
            print(f"{player.name} is not a player of {self.team_name}")

    def calculate_team_score(self):
        return sum(player.calculate_points(player._goals, player._assists, player._clean_sheets) for player in self._players)

# Chelsea = Team('Chelsea', 'Enzo Marisca')
#
# palmer = Player('Cole Palmer', 'Midfielder', 'Chelsea')
# palmer._goals = 5
# palmer._assists = 2
# palmer._clean_sheets = 1
#
# jackson = Player('Nico Jackson', 'Forward', 'Chelsea')
# jackson._goals = 3
# jackson._assists = 1
# jackson._clean_sheets = 0
#
# Chelsea.add_player(palmer)
# Chelsea.add_player(jackson)
# Chelsea.remove_player(jackson)
#
# print(Chelsea.players)
# print(Chelsea.calculate_team_score())

