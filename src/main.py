class Robot():
    def __init__(self, name: str, hp: int, attack: int, shield: int):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.shield = shield

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack}\nShield: {self.shield}\n"

def main():
    print("---ROBOT WARS---")
    print("Welcome to Robot Wars, a simple game based robot battle, but much fun!\n")
    print("[1] start game")
    print("[2] end game\n")

    while True:
        line = input()
        robots = []

        match line.split():
            case ["1"]:
                while True:
                    print("[1] create robot")
                    print("[2] show robot")
                    print("[3] start battle")
                    print("[4] end game\n")

                    line = input()

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
                                print("Don't exist robot created!\n")
                            else:
                                print("---ROBOTS---")
                                for rob in robots:
                                    print(rob)

                        case ["4"]:
                            break

                        case _:
                            print("Invalid command!\n")

            case ["2"]:
                break

            case _:
                print("Invalid command!\n")

main()