import random
# todo fast forward, add some colours to the text

def fight(player1, player2):
    # phrase structure: PLAYER_NAME - fight_phrases_part_1 (VERB) - fight_phrase_part_2 (LOCATION) - dealing X amount of damage
    fight_phrases_part_1 = ["smacked", "slapped", "clobbered", "bashed", "whipped", "pounded", "struck", "hit",
                            "punched", "socked", "slugged", "thrashed", "bopped", "whacked", "smote", "tackled",
                            "bonked", "bopped", "banged", "clonked", "knocked", "smacked", "whacked", "walloped"]

    fight_phrases_part_2 = ["in the face", "in the chest", "in the gut", "in the jaw", "in the nose", "in the eye",
                            "in the ear", "in the throat", "in the groin", "in the leg", "in the arm",
                            "in the shoulder", "in the back", "in the neck", "in the stomach", "in the ribs",
                            "in the shin", "in the ankle", "in the elbow", "in the knee", "in the thigh",
                            "to the floor","to the ground", "against the wall", "against the table"]
    fast_forward = input("Do you want to fastforward or not (typ yes or no): ")

    print("FIGHT IS COMMENCING")
    print("-------------------")
    # selecting starting player for attacks
    if random.randint(0, 1) == 0:
        attacker = player1
        defender = player2
    else:
        attacker = player2
        defender = player1

    # loop for battle
    while attacker.effective_health > 0 and defender.effective_health > 0:
        # setting checking if hit wil be a critical (0-10, 10 == 100%, 5 == 50%, ...)
        crit_chance_effective = random.randint(attacker.critchance, 10)
        # if is a crit
        if crit_chance_effective == 10:
            damage = attacker.critical_hit
            defender.take_damage(damage)
            print("DAMMNNN a critical HIT!")
            # creating phrases
            print(str(attacker.name) + " " + random.choice(fight_phrases_part_1) + " " + str(defender.name) + " " +
                  random.choice(fight_phrases_part_2) + " " + "dealing" + " " + str(damage) + " damage!")
            print(defender.name + " has " + "\033[91m" + str(
                defender.effective_health) + " health left over!" + "\033[0m")
            if "no" in fast_forward:
                input("Press Enter to continue")
            print("")
        # else just a normal hit
        else:
            damage = attacker.base_damage
            defender.take_damage(damage)
            print("OOOF, just a normal HIT!")
            print(str(attacker.name) + " " + random.choice(fight_phrases_part_1) + " " + str(defender.name) + " " +
                  random.choice(fight_phrases_part_2) + " " + "dealing" + " " + str(damage) + " damage!")
            print(defender.name + " has " + "\033[91m" + str(defender.effective_health) + " health left over!" + "\033[0m")
            if "no" in fast_forward:
                input("Press Enter to continue")
            print("")
        # swapping attacker for defender and vice-versa
        attacker, defender = defender, attacker

    # checking who died (outside of loop)
    if player1.effective_health <= 0:
        print(player1.name + " has died!")
        print(player2.name + " was clearly stronger in this mighty fight, they had " + str(
            player2.effective_health) + " health left over!")
    elif player2.effective_health <= 0:
        print(player2.name + " has died!")
        print(player1.name + " was clearly stronger in this mighty fight, they had " + str(
            player1.effective_health) + " health left over!")
