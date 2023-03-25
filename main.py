from battle import fight
from setup import *

print("BATTLE sim by SB")
file = 'players.pickle'
# creating 2 players with this func
load_or_new_players = input("Do you want to load old players or create new ones? type load or new: ")
if "new" in load_or_new_players:
    p1, p2 = setting_up_players("2")
else:
    amount_of_loads = str(input("do you want to load 1 or 2 players: "))
    if "1" in amount_of_loads:
        p1 = loading_players_dialogue(file)
        x, p2 = setting_up_players(amount_of_loads)
    else:
        p1 = loading_players_dialogue(file)
        p2 = loading_players_dialogue(file)



def main(p1, p2):
    stat_checking(p1, p2)
    print("")
    fight(p1, p2)
    saving_players_dialogue(p1, p2, file)


main(p1, p2)
