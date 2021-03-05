import random,os

class Soldier:
    
    def __init__(self):
        self.health = 700
        self.offense = random.randint(30, 100)
        self.defense = random.randint(0, 30)
        self.life = True
    
    
    def show(self):
        print(
        f"""
        health = {self.health}
        offense = {self.offense}
        defense = {self.defense}
        is_life = {self.life}
        
        """)
    
    def war(self, enemy):
        damage = self.offense - enemy.defense
        enemy.health -= damage
        if enemy.health <= 0:
            enemy.life = False
            enemies.remove(enemy)
        
class Enemy:
    
    def __init__(self):
        self.health = 100
        self.offense = random.randint(30, 100)
        self.defense = random.randint(0, 30)
        self.life = True
    
    def show(self):
        print(f"health = {self.health} -->> offense = {self.offense} -->>  defense = {self.defense} --> is_life = {self.life}")
        
    def war(self, soldier):
        damage = self.offense - soldier.defense
        soldier.health -= damage
        if soldier.health <= 0:
            soldier.life = False

            
## DEFINE SOLDIER 
soldier = Soldier()

## DEFINES ENEMIES
enemies = list()
for i in range(1, 5):
    enemies.append(Enemy())

## MAIN
while True:
    os.system("clear")
    
    if soldier.life == False:
        print("GAME OVER !")
        quit()
        
    if not enemies:
        print("YOU WİN !")
        quit()
        
    print("--SOLDIER--")
    soldier.show()
    
    print("--ENEMIES--\n")
    for enemy in enemies:
        enemy.show()
    
    chose = int(input("Chose enemy for defense:"))
    enemy_def = enemies[chose]
    soldier.war(enemy_def)
    
    if enemies:
        enemy_off = enemies[random.randint(0, len(enemies)-1)]
        enemy_off.war(soldier)
    