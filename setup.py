import random
from saving_data import save_player, load_player, clear_file
from player import Player


# function for letting user to check the stats of each player
def stat_checking(p1, p2):
    print("A NEW BATTLE HAS STARTED")
    print(
        "THE ALMIGHTY    " + "\033[91m" + p1.name + "\033[0m" + "    VERSUS THE ALMIGHTY    " + "\033[91m" + p2.name + "\033[0m")
    stats_or_fight = input(
        "Enter fight if you want to go to the fight immediately, enter stats if you want to read stats first: ")
    # if user wants to check stats:
    if "stats" in stats_or_fight:
        print("THE STATS:")
        print("")

        # stats player 1 display
        print(p1.name + "'s" + " STATS:")
        print("")
        print("\033[91m" + "HEALTH: " + "\033[0m" + str(p1.health))
        print("\033[91m" + "DEFENCE: " + "\033[0m" + str(p1.defence))
        print("\033[32m" + "EFFECTIVE HEALTH: " + "\033[0m" + str(p1.effective_health))
        print("\033[36m" + "BASE DAMAGE: " + "\033[0m" + str(p1.base_damage))
        print("\033[34m" + "CRIT DAMAGE: " + "\033[0m" + str(p1.critdamage))
        print("\033[34m" + "CRITCHANCE: " + "\033[0m" + str(p1.critchance))
        print("\033[34m" + "CRITICAL HIT : " + "\033[0m" + str(p1.critical_hit))

        # waiting for user reaction/pauing untill user presses enter
        print("")
        input("PRESS ENTER TO VIEW PLAYER 2's STATS: ")
        print("")

        # stats player 2 display
        print(p2.name + "'s" + " STATS:")
        print("")
        print("\033[91m" + "HEALTH: " + "\033[0m" + str(p2.health))
        print("\033[91m" + "DEFENCE: " + "\033[0m" + str(p2.defence))
        print("\033[32m" + "EFFECTIVE HEALTH: " + "\033[0m" + str(p2.effective_health))
        print("\033[36m" + "BASE DAMAGE: " + "\033[0m" + str(p2.base_damage))
        print("\033[34m" + "CRIT DAMAGE: " + "\033[0m" + str(p2.critdamage))
        print("\033[34m" + "CRITCHANCE: " + "\033[0m" + str(p2.critchance))
        print("\033[34m" + "CRITICAL HIT : " + "\033[0m" + str(p2.critical_hit))
        print("")
        input("Press ENTER to continue")

    else:
        return None


# function for letting user create 2 players or letting the computer generate 2 random fighters
def setting_up_players(amount_of_players):
    setting = input("Enter custom to create custom fighters, enter random for random fighters: ")
    if "custom" in setting and "2" in amount_of_players:

        try:
            # player 1
            name1 = str(input("Enter the name of player 1: "))
            health1 = int(input("Enter P1 health: "))
            defence1 = int(input("Enter P1 defence: "))
            critdamage1 = int(input("Enter P1 critdmg: "))
            critchance1 = int(input("Enter P1 critchance: "))
            basedamage1 = int(input("Enter P1 base dmg: "))
            p1 = Player(name1, health1, critchance1, critdamage1, defence1, basedamage1)

            # player 2
            name2 = str(input("Enter the name of player 2: "))
            health2 = int(input("Enter P2 health: "))
            defence2 = int(input("Enter P2 defence: "))
            critdamage2 = int(input("Enter P2 critdmg: "))
            critchance2 = int(input("Enter P2 critchance num from 1-10, 10 is max: "))
            basedamage2 = int(input("Enter P2 base dmg: "))
            p2 = Player(name2, health2, critchance2, critdamage2, defence2, basedamage2)

            return p1, p2
        except ValueError:
            print("Please enter something valid valid")
            print("")
            # restating the function due to a vlue error
            setting_up_players(amount_of_players)
    elif "custom" in setting and "1" in amount_of_players:
        try:
            # player 2
            name2 = str(input("Enter the name of player 2: "))
            health2 = int(input("Enter P2 health: "))
            defence2 = int(input("Enter P2 defence: "))
            critdamage2 = int(input("Enter P2 critdmg: "))
            critchance2 = int(input("Enter P2 critchance num from 1-10, 10 is max: "))
            basedamage2 = int(input("Enter P2 base dmg: "))
            p2 = Player(name2, health2, critchance2, critdamage2, defence2, basedamage2)

            return "None", p2
        except ValueError:
            print("Please enter something valid valid")
            print("")
            # restating the function due to a vlue error
            setting_up_players(amount_of_players)

    # generating random stats for random characters
    elif "random" in setting and "2" in amount_of_players:
        # list of names for the computer to pick from
        names = ["Bob", "Jeff", "Rudy", "Mick", "Jhonny", "Ruz", "Mike", "Lewis", "Brock", "Dani"]
        p1 = Player(random.choice(names), random.randint(80, 150), random.randint(1, 10), random.randint(10, 150),
                    random.randint(10, 150), random.randint(15, 25))
        p2 = Player(random.choice(names), random.randint(80, 150), random.randint(1, 10), random.randint(10, 150),
                    random.randint(10, 150), random.randint(15, 25))
        # checking for double names
        if p1.name == p2.name:
            p2.name = "Lupo"

        return p1, p2
    elif "random" in setting and "1" in amount_of_players:
        # list of names for the computer to pick from
        names = ["Bob", "Jeff", "Rudy", "Mick", "Jhonny", "Ruz", "Mike", "Lewis", "Brock", "Dani"]
        p2 = Player(random.choice(names), random.randint(80, 150), random.randint(1, 10), random.randint(10, 150),
                    random.randint(10, 150), random.randint(15, 25))

        return "None", p2
    else:
        print("enter something valid")
        setting_up_players(amount_of_players)

# load data function implemention
def loading_players_dialogue(filename):
    print("WELCOME TO THE LOADER!")
    print("")
    players = load_player(filename)
    # printing all players available to load
    for i, player in enumerate(players):
        print(f"{i+1}. {player.name}")
    player_choice = int(input("Which player would you like to load? Enter the number of the player: "))
    player = players[player_choice-1]
    return player


def saving_players_dialogue(p1, p2, filename):
    user_input = input("Would you like to save p1 or p2 (typ p1 or p2 or both): ")
    if "p1" in user_input:
        save_player(p1, filename)
        print("player 1 saved succesfully ")
    elif "p2" in user_input:
        save_player(p2, filename)
        print("saved player 2 succesfully")
    else:
        save_player(p1, filename)
        save_player(p2, filename)
    print("players saved succesfully")
    clear_file_input = input("yes to clear all players from save but save your just used ones, no for no :D")
    if "yes" in clear_file_input:
        clear_file(p1, p2, filename)
    else:
        return 0


