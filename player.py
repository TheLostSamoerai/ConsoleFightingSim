# imports

class Player:
    def __init__(self, name, health, critchance, critdamage, defence, base_damage):
        self.name = name
        self.health = health
        self.defence = defence
        self.effective_health = self.health * (1 + (self.defence / 100)) // 1       # formula for E-HP = heath * (1 + (defence / 100))      last // 1 is to round it off
        self.base_damage = base_damage
        self.critchance = critchance
        self.critdamage = critdamage
        self.critical_hit = self.base_damage * (critdamage * 0.01) // 1


    def take_damage(self, damage):

        self.effective_health -= damage
