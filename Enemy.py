import random
from Weapon import Weapon

class Enemy:

    names = ["orc", "goblin", "rat", "dog", "villager"]
    
    def __init__(self, name = random.choice(names) ):
        self.name = name
        self.hp = max(10,0)
        self.ac = 10
        self.xp = 0
        self.weapon = Weapon()
        self.alive = True
    
    def damage(self, attacker, dmg):
        self.hp -= dmg
        print(f"{self.name} has {self.hp} hp left")
        if self.hp < 1:
            attacker.xp += self.xp
            self.alive = False
            print(f"{self.name} dies!")
            attacker.enemy = None
            
    def attack(self, target):
        print(f"{self.name} swings at you with their {self.weapon.name}")
        attack_roll = random.randint(1,20)
        
        if (attack_roll < target.ac):
            print("They miss!")
            return
        
        dmg = random.randint(1,self.weapon.damage)

        if attack_roll == 20:
            dmg *= 2
            print(f"{self.name} scores a CRITICAL hit, you take {dmg} damage.")
        elif attack_roll >= target.ac:
            print(f"{self.name} hits you for {dmg} damage.")
        
        target.damage(self,dmg)

