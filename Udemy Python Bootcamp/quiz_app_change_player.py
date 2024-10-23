"""Function to swap the current player from P1 to P2"""


def change_player(player_one_name, player_two_name, current_player):
    """Swaps current player"""
    if current_player == player_one_name:
        return player_two_name
    return player_one_name
