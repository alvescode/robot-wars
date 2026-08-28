class Robot():
    def __init__(self):
        self.name: str
        self.hp: int
        self.attack: int
        self.shield: int

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack}\nShield: {self.shield}\n"

    def robotName(self, user_name: str):
        self.name = user_name

    def robotHp(self, user_hp: int):
        self.hp = user_hp

    def robotAttack(self, user_attack: str):
        self.attack = user_attack

    def robotShield(self, user_shield: int):
        self.shield = user_shield

def main():
    print("---ROBOT WARS---")
    print("Welcome to Robot Wars, a simple game based robot battle, but much fun!\n")
    print("[1] start game")
    print("[0] end game\n")

    while True:
        line = input()

        match line.split():
            case ["1"]:
                while True:
                    print("[1] create robot")
                    print("[2] show robot")
                    print("[0] end game\n")

                    line = input()

                    match line.split():
                        case ["1"]:
                            robot = Robot()

                            user_name = input("Write robot name: ")
                            robot.robotName(user_name)

                            user_hp = input("Write robot HP: ")
                            robot.robotHp(int(user_hp))
                            
                            user_attack = input("Write robot attack: ")
                            robot.robotAttack(int(user_attack))

                            user_shield = input("Write robot shield: ")
                            robot.robotShield(int(user_shield))

                            print("")
                        case ["2"]:
                            print(robot)
                        case ["0"]:
                            break
                        case _:
                            print("Invalid command!\n")
            case ["0"]:
                break
            case _:
                print("Invalid command!\n")

main()