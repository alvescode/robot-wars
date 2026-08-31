import time

from robot import Robot
from state import State

def select_robot(robots):
    print("---ROBOTS---\n")

    for index, rob in enumerate(robots):
        if rob.hp > 0:
            print(f"[{index}] {rob.name}")

    while True:
        try:
            line = int(input("\n> "))

            if line < 0 or line >= len(robots):
                print("Invalid robot!")
                continue

            robot = robots[line]

            if robot.hp <= 0:
                print("This robot is dead!")
                continue

            return robot

        except ValueError:
            print("Please enter a number!")

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
                            while user_name == "":
                                print("Invalid name!")
                                user_name = input("Write robot name: ")

                            while True:
                                try:
                                    user_hp = int(input("Write robot HP: "))

                                    if user_hp <= 0:
                                        print("Invalid HP!")
                                        continue

                                    break

                                except ValueError:
                                    print("Please enter a number!")

                            while True:
                                try:
                                    user_attack = int(input("Write robot attack: "))

                                    if user_attack <= 0:
                                        print("Invalid attack!")
                                        continue

                                    break

                                except ValueError:
                                    print("Please enter a number!")

                            while True:
                                try:
                                    user_shield = int(input("Write robot shield: "))

                                    if user_shield < 0:
                                        print("Invalid shield!")
                                        continue

                                    break

                                except ValueError:
                                    print("Please enter a number!")

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
                                            print(f"{player} win!")
                                            break

                                        print(f"\n{player.name} attack {enemy.name}\n")
                                        time.sleep(1)
                                        print(f"{enemy.name} HP: {enemy.hp}\n{enemy.name} Shield: {enemy.shield}\n")
                                        time.sleep(1)

                                        state = enemy.attack(player)

                                        if state == State.DEAD:
                                            print(f"\n{player.name} died\n")
                                            print(f"{enemy} win!")
                                            break

                                        print(f"\n{enemy.name} attack {player.name}\n")
                                        time.sleep(1)
                                        print(f"{player.name} HP: {player.hp}\n{player.name} Shield: {player.shield}\n")
                                        time.sleep(1)

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
