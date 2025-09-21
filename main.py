import json
from models.player import Player
from models.team import Team
import pandas as pd

def load_players_from_json(filepath: str):
    with open(filepath, 'r') as file:
        data = json.load(file)
        return [Player(p["name"], p["position"], p["club"], p["price"]) for p in data]

# Load all players
players = load_players_from_json("data/players.json")

# Welcome message
print("\n🎉 Welcome to Patrick's Fantasy Football Manager 🎉")
print("Build your dream Premier League team and compete for glory!\n")

# Create team
team_name = input("🏟️  Enter your Fantasy Team Name:  ")
team = Team(team_name)
print(f"\n✅ Team '{team_name}' created successfully!")
print(f"You have a starting budget of 💰 {team.budget} million")
print("Choose wisely — balance stars and value!\n")

# Show available players
print("📋 Available Players:")
print("Name".ljust(20), "Position".ljust(12), "Club".ljust(15), "Price")
print("-" * 60)
for player in players:
    print(player.name.ljust(20), player.position.ljust(12), player.club.ljust(15), f"£{player.price:.1f}m")

# Interactive selection loop
while True:
    selected_name = input("\n🔍 Enter the name of the player to add (or type 'exit' to finish): ").strip()

    if selected_name.lower() == "exit":
        break

    # Find player by name
    selected_player = next((p for p in players if p.name.lower() == selected_name.lower()), None)

    if not selected_player:
        print("❌ Player not found. Please check the spelling.")
        continue

    if selected_player.name in team.players:
        print("⚠️ Player already in your team.")
        continue

    # Add player to team
    team.add_player(selected_player)

# Final team summary
print(f"\n Final Team '{team.team_name}'")
print("Players:")
for name in team.players:
    print(f"- {name}")


# Build your starting 11
starting = input("Add a player from your team into your starting eleven")
team.add_to_field(starting)

# Print fixtures for user to view
url = 'https://www.football-data.co.uk/mmz4281/2526/E0.csv'

prem_fixture = pd.read_csv(url)
print('Premier League Fixtures')
essentails = ['Date','Time','HomeTeam','AwayTeam']

for index, row in prem_fixture[essentails].iterrows():
    print(f"{row['Date']} {row['Time']} - {row['HomeTeam']} vs {row['AwayTeam']}")
