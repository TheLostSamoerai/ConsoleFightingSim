import pickle


def save_player(player, filename):
    try:
        with open(filename, 'ab') as file:
            pickle.dump(player, file, protocol=pickle.HIGHEST_PROTOCOL)
    except:
        print("something went wrong, rebooting game...")
        #full_game()

# this still needs improving loln now just overwriting everthing
def clear_file(player1, player2, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(player1, file, protocol=pickle.HIGHEST_PROTOCOL)
            pickle.dump(player2, file, protocol=pickle.HIGHEST_PROTOCOL)
    except:
        print("something went wrong, rebooting game...")
        #full_game()


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