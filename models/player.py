from itertools import count

class Player:
    def __init__(self, name, position, club):
        self.name = name
        self.position = position
        self.club = club
        self._goals = 0
        self._assists = 0
        self._clean_sheets = 0
        self._points = None

    def calculate_points(self, goals, assists,clean_sheets):
        self._goals = goals
        self._assists = assists
        self._clean_sheets = clean_sheets
        points = 0

        if self.position == "Forward":
            points += self._goals * 4
            points += self._assists * 3
            return points
        elif self.position == "Midfielder":
            points += self._goals * 5
            points += self._assists * 3
            points += self._clean_sheets * 1
            return points
        elif self.position == "Defender":
            points += self._goals * 6
            points += self._assists * 3
            points += self._clean_sheets * 4
            return points
        else:
            points += self._goals * 10
            points += self._assists * 3
            points += self._clean_sheets * 4
            return points

    def update_goals_stats(self, value):
        self._goals += value
        print(f"{self.name} has scored {self._goals} goals")

    def update_assists_stats(self, value):
        self._assists += value
        print(f"{self.name} has a total of {self._goals} assist")


# palmer = Player('Palmer', 'Goalkeeper', 'Chelsea')
# print(palmer.calculate_points(5,2,0))
# palmer.update_goals_stats(10)
# palmer.update_assists_stats(10)
