class Team:
    def __init__(self, name="Name", origin="Origin"):
        self.team_name = name
        self.team_origin = origin

    def define_team_name(self, name):
        self.team_name = name

    def define_team_origin(self, origin):
        self.team_origin = origin


class Player(Team):
    def __init__(self, player_name, player_point, team_name, team_origin):
        Team.__init__(self, team_name, team_origin)
        self.player_name = player_name
        self.player_points = player_point

    def scored_points(self):
        self.player_points += 1

    def __set_name__(self, name):
        self.player_name = name

    def __str__(self):
        return self.player_name + " has scored: " + str(self.player_points) + " points"


Player1 = Player("Ronney", 256, "Man Utd", "England")

print(Player1.player_name)
print(Player1.player_points)
print(Player1.team_name)
print(Player1.team_origin)
Player1.scored_points()
print(Player1.player_points)
print(Player1)

# Team1 = Team("Manchester United", "England")
#
# Team2 = Team("Golden State Worriors", "San Franscisco"
#
# Team3 = Team()
#
# print(Team1.team_name)
# Team1.define_team_name("Real Madrid")
# print(Team1.team_name)
#
# print(Team1.team_origin)
# Team1.define_team_origin("Newton Heats")
#
# print(Team2.team_name)
# print(Team2.team_origin)
#
# print(Team3.team_name)
# print(Team3.team_origin)
