import pickle

def save_player(player, filename):
    with open(filename, 'ab') as file:
        pickle.dump(player, file, protocol=pickle.HIGHEST_PROTOCOL)


def clear_file(player1, player2, filename):
    with open(filename, 'wb') as file:
        pickle.dump(player1, file, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(player2, file, protocol=pickle.HIGHEST_PROTOCOL)


def load_player(filename):
    loaded_players = []
    with open(filename, 'rb') as f:
        try:
            while True:
                player = pickle.load(f)
                loaded_players.append(player)
                print(f"Loaded player: {player.name}")
        except EOFError:
            pass
    return loaded_players