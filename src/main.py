class Robot():
    def __init__(self, name: str, hp: int, attack: int, shield: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack
        self.shield = shield

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack_power}\nShield: {self.shield}\n"

    def attack(self, enemy):
        enemy.hp -= self.attack_power

def select_robot(robots):
    print("\n---ROBOTS---")

    for index, rob in enumerate(robots):
        print(f"[{index}] {rob.name}")

    line = int(input(">"))
    return robots[line]

def main():
    robots = []
    running = True

    print("---ROBOT WARS---")
    print("Welcome to Robot Wars, a simple game based robot battle, but much fun!\n")
    print("[1] start game")
    print("[2] end game\n")

    while running:
        line = input(">")

        match line.split():
            case ["1"]:
                while running:
                    print("\n[1] create robot")
                    print("[2] show robot")
                    print("[3] start battle")
                    print("[4] end game\n")

                    line = input(">")

                    match line.split():
                        case ["1"]:
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
                            print("")
                            
                        case ["2"]:
                            if len(robots) == 0:
                                print("\nDon't exist robot created!\n")
                            else:
                                print("\n---ROBOTS---")
                                for rob in robots:
                                    print(rob)

                        case ["3"]:
                            if len(robots) < 2:
                                print("You need at least 2 robots to battle\n")
                                continue

                            print("\nSelect your robot: ")
                            player = select_robot(robots)
                            print(f"You select {player.name}")

                            print("\nSelect your enemy: ")
                            enemy = select_robot(robots)
                            print(f"The enemy is {enemy.name}")

                        case ["4"]:
                            running = False

                        case _:
                            print("Invalid command!\n")

            case ["2"]:
                running = False

            case _:
                print("Invalid command!\n")

main()