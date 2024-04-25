import random
import sys
from Weapon import Weapon
from Enemy import Enemy

class Player:
    
    commands = ["quit", "kill", "examine", "read", "use", "get", "drop", "equip"]

    def __init__(self, name):
        self.name = name
        self.hp = max(10,0)
        self.ac = 10
        self.xp = 0
        self.weapon = Weapon()
        self.alive = True
        self.enemy = Enemy()

    def damage(self, attacker, damage):
        print(f"You take {damage} damage from {attacker.name}")
        self.hp -= damage
        if self.hp <= 0:
            print(f"You die!\nGame Over!")
            self.alive = False
    
    def attack(self, target):
        if self.enemy == None:
            print(f"You are not fighting anyone")
            return
        print(f"You swing your {self.weapon.name} at {target.name}")
        attack_roll = random.randint(1,20)
        
        if (attack_roll < target.ac):
            print("You miss!")
        else:
            dmg = random.randint(1,self.weapon.damage)

            if attack_roll == 20:
                dmg *= 2
                print(f"You score a CRITICAL hit on {target.name} for {dmg} damage.")
            elif attack_roll >= target.ac:
                print(f"You hit {target.name} and do {dmg} damage.")
            
            target.damage(self,dmg)
        if self.enemy != None:
            target.attack(self)

    def prompt(self):
        prompt = f"[{self.name}] Xp: {self.xp} Hp: {self.hp} > "
        if self.alive == False:
            return "quit"
        
        cmd = input(prompt)
        verb = cmd.split(" ")[0]
        subject = " ".join(cmd.split(" ")[1:])
        print(f"You [{verb}] [{subject}]")
        if verb not in self.commands:
            print(f"You don't know how to \"{verb}\"")
            return cmd
        
        if verb == "quit":
            sys.exit(0)

        if verb == "kill":
            self.attack(self.enemy)

        return cmd
    