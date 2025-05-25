# action.py
import time
import os

#eat food
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def feed_animation():
    fish = "><((°>"
    food = "@"
    bubble = "  。"

    for step in range(10):
        clear_console()
        print(" " * step + fish)
        print(" " * 20 + food)
        print(" " * (step + 2) + bubble)
        time.sleep(0.15)

    clear_console()
    print(" " * 20 + fish + " eat " + food + "！")
    time.sleep(1)

    for step in reversed(range(10)):
        clear_console()
        print(" " * step + fish)
        time.sleep(0.1)

    clear_console()
    print(f"Feeding completed")