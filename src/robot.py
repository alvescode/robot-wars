from state import State

class Robot():
    def __init__(self, name: str, hp: int, attack: int, shield: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack
        self.shield = shield

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack_power}\nShield: {self.shield}\n"

    def attack(self, target) -> State:
        if target.shield >= self.attack_power:
            target.shield -= self.attack_power
        else:
            damage = self.attack_power - target.shield
            target.shield = 0
            target.hp -= damage

        if target.hp <= 0:
            target.hp = 0
            return State.DEAD
        return State.OK
