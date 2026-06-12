class Troop:
    def __init__(self, hp, damage, velocity, atk_velocity):

        # Atributos basicos
        self.hp = hp
        self.dmg = damage
        self.vel = velocity
        self.atk_vel = atk_velocity

        # Atributos derivados
        self.dps = self.dmg / self.atk_vel
    
    def single_hit(self, objective : Troop):
        objective.hp = objective.hp - self.dmg

    def dps_attack(self, objective : Troop):
        objective.hp = objective.hp - self.dps
    
    def is_alive(self):
        return self.hp > 0
    
    def show_hp(self):
        print(f"HP:{self.hp}")
        


barbarian = Troop(500, 100, 1, 1.2)
goblin = Troop(300,30, 2, 0.6)


seconds = 1
while(barbarian.is_alive() and goblin.is_alive()):
    print(f"In second {seconds}s")
    goblin.dps_attack(barbarian)
    print(f"Gobling attacks barbarian and left him at {barbarian.hp}")

    barbarian.dps_attack(goblin)
    print(f"Barbarian attacks a Goblin and left him at {goblin.hp}\n")

    
    seconds += 1

barbarian.show_hp()
goblin.show_hp()