def validate_budget(current_budget: float, player_price: float) -> bool:
    "Check if the team has enough budget to buy the player."
    return current_budget >= player_price

def validate_team_size(current_size: int, max_size: int):
    "Ensure team isn't exceeding max allowed player"
    return current_size <= max_size

def log_transfer(direction: str, player, team):
    """Simple console log for transfers (can expand later)."""
    print(f"{direction}: {player.name} {'→' if direction == 'IN' else '←'} {team.name}")


def validate_position_limit(team):
    position_limit = {
        "Forward": 3,
        "Midfield": 4,
        "Defender": 5,
        "Goalkeeper": 2
    }

    position_counts = {}
    for player in team.players:
        pos = player.position
        position_counts[pos] = position_counts.get(pos, 0) + 1

    for position, limit in position_limit.items():
        if position_counts.get(position, 0) > limit:
            return False

    return True

