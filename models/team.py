from models.player import Player

DEFAULT_BUDGET = 50.0

class Team:

    def __init__(self, team_name):
        self.budget = DEFAULT_BUDGET
        self.team_name = team_name
        self.manager_name = ""
        self._players = []
        self._starting_eleven = []

    @property
    def players(self):
        return [player.name for player in self._players]

    def add_player(self, player):
            if not player in self._players and self.budget > 0:
                self._players.append(player)
                self.budget -= player.price
                print(f"{player.name} has been added to {self.team_name} players list and the new budget is {self.budget}")


    def remove_player(self, player):
        if player in self._players:
            self._players.remove(player)
            print(f"{player.name} has been removed from {self.team_name} players list")
        else:
            print(f"{player.name} is not a player of {self.team_name}")

    def calculate_team_score(self):
        return sum(player.calculate_points(player._goals, player._assists, player._clean_sheets) for player in self._players)


    def add_to_field(self, player):
        if not player in self._starting_eleven and len(self._starting_eleven) < 11:
            starting_team = self._starting_eleven.append(player)
            print(f"{player.name} has been added to your starting eleven")
        else:
            print("Error: There are too many players in your starting 11")


Chelsea = Team('Chelsea')
#
palmer = Player('Cole Palmer', 'Midfielder', 'Chelsea', 7.0)
# palmer._goals = 5
# palmer._assists = 2
# palmer._clean_sheets = 1
#
jackson = Player('Nico Jackson', 'Forward', 'Chelsea',  7.0)

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
