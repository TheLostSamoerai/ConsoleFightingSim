import random
# todo add arour, spells, new abilities like evading an attack
class Player:
    def __init__(self, name, health, critchance, critdamage, defence, base_damage, magic_find):
        self.name = name
        self.health = health
        self.defence = defence
        self.effective_health_reserve = self.health * (1 + (self.defence / 100)) // 1       # formula for E-HP = heath * (1 + (defence / 100))      last // 1 is to round it off
        self.effective_health = self.health * (1 + (self.defence / 100)) // 1
        self.base_damage = base_damage
        self.critchance = critchance
        self.critdamage = critdamage
        self.critical_hit = self.base_damage * (1 + self.critdamage / 100) // 1     # this formula might need some more work
        self.magic_find = magic_find


    def take_damage(self, damage):
        self.effective_health -= damage


    def find_armour_message(self, armour_type, armour_dict):
        find_phrases = ["WAAAAAAAUUW ", "Ohhh myyy gawwdddd ", "GOD DANG ", "BEEPBOOPBAP ", "SUDDENLY "]
        find_location_phrases = [" in the bushes!", " on the ground!", " behind a tree!", " under a rock!", " that  the leaves!"]
        print(random.choice(find_phrases) + self.name + " found a piece of armour: " + armour_type + random.choice(find_location_phrases))
        print("It wil give " + self.name + " " + str(armour_dict[armour_type]) + " defence! That's nice!")

    def apply_armour(self, armour_type, armour_dict):
        armour_defence_bonus = armour_dict[armour_type]
        self.defence += armour_defence_bonus
        self.effective_health = self.effective_health * (1 + (self.defence / 100)) // 1