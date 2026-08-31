import enum

class State(enum.Enum):
    OK = "ok"
    DEAD = "morto"

class Robot():
    def __init__(self, name: str, hp: int, attack: int, shield: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack
        self.shield = shield

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack_power}\nShield: {self.shield}\n"

    def attack(self, enemy) -> State:
        if enemy.shield >= self.attack_power:
            enemy.shield -= self.attack_power
        else:
            damage = self.attack_power - enemy.shield
            enemy.shield = 0
            enemy.hp -= damage

        if enemy.hp <= 0:
            enemy.hp = 0
            return State.DEAD
        return State.OK

def select_robot(robots):
    print("---ROBOTS---\n")

    for index, rob in enumerate(robots):
        print(f"[{index}] {rob.name}")

    line = int(input("\n> "))
    return robots[line]

def main():
    robots = []
    running = True

    print("---ROBOT WARS---\n")
    print("Welcome to Robot Wars, a simple game based robot battle, but much fun!\n")
    print("[1] start game")
    print("[2] end game\n")

    while running:
        line = input("> ")
        print("")

        match line.split():
            case ["1"]:
                while running:
                    print("[1] create robot")
                    print("[2] show robots")
                    print("[3] start battle")
                    print("[4] end game\n")

                    line = input("> ")

                    match line.split():
                        case ["1"]:
                            print("\n---CREATE ROBOT---\n")

                            user_name = input("Write robot name: ")
                            user_hp = int(input("Write robot HP: "))
                            user_attack = int(input("Write robot attack: "))
                            user_shield = int(input("Write robot shield: "))

                            robot = Robot(
                                user_name, 
                                user_hp, 
                                user_attack, 
                                user_shield
                            )

                            robots.append(robot)
                            print(f"\n{user_name} was created\n")
                            
                        case ["2"]:
                            if len(robots) == 0:
                                print("\nDon't exist robot created!\n")
                            else:
                                print("\n---ROBOTS---\n")

                                for rob in robots:
                                    print(rob)

                        case ["3"]:
                            if len(robots) < 2:
                                print("\nYou need at least 2 robots to battle\n")
                                continue

                            print("\n---SELECT YOUR ROBOT---\n")

                            player = select_robot(robots)
                            print(f"\nYou select {player.name}\n")

                            print("---SELECT YOUR ENEMY---\n")

                            enemy = select_robot(robots)

                            while player == enemy:
                                print("\nYou can't select you player, please select other robot\n")
                                print("---SELECT YOUR ENEMY---\n")

                                enemy = select_robot(robots)

                            print(f"\nThe enemy is {enemy.name}\n")

                            while True:
                                print("---BATTLE---\n")
                                print("[1] attack")
                                print("[2] show status")
                                print("[3] run\n")

                                line = input("> ")
                                
                                match line.split():
                                    case ["1"]:
                                        state = player.attack(enemy)

                                        if state == State.DEAD:
                                            print(f"\n{enemy.name} died\n")
                                            break

                                        print(
                                            f"\n{player.name} attack {enemy.name}\n\n"
                                            f"{enemy.name} HP: {enemy.hp}\n{enemy.name} Shield: {enemy.shield}\n"
                                        )

                                    case ["2"]:
                                        print("\n---PLAYER STATUS---\n")
                                        print(player)

                                    case ["3"]:
                                        print("\n")
                                        break

                                    case _:
                                        print("Invalid command!\n")

                        case ["4"]:
                            running = False

                        case _:
                            print("Invalid command!\n")

            case ["2"]:
                running = False

            case _:
                print("Invalid command!\n")

main()
