# chase.py
import random
import time
import os

#clear the screen content
def clear_console():
    if os.name == 'nt':
        os.system('cls')     # Windows 
    else:
        os.system('clear')   # Mac / Linux 

def chase_game(env):
    arrow_map = {
        'W': '↑',
        'A': '←',
        'S': '↓',
        'D': '→'
    }
    sequence = []
    options = ['W', 'A', 'S', 'D']

    #prepare chase game
    i = 0
    while i < 5:
        direction = random.choice(options) 
        sequence.append(direction)         
        i += 1

    # display arrow
    arrow_display = []
    for char in sequence:
        arrow = arrow_map[char]
        arrow_display.append(arrow)

    print("\n Memorize the following arrow sequence (W↑ A← S↓ D)【Disappear in 3s】")
    print(" ".join(arrow_display))
    time.sleep(3)

    clear_console()

    user_input = input("Please enter the arrow sequence you remember, separated by spaces:").strip().upper().split()

    correct = 0
    length = min(len(sequence), len(user_input))

    for i in range(length):
        if user_input[i] == sequence[i]:
            correct += 1
    added_happiness = correct * 3

    if correct == 0:
        print("All wrong. The fish swam away disappointingly.")
    else:
        print(f"You got {correct} right, all fish gained +{added_happiness} happiness!")

    # Give each fish a happiness boost（<=100)
    for fish in env.animals:
        if 'happiness' in dir(fish):  
            new_happiness = fish.happiness + added_happiness

            if new_happiness > 100:
                new_happiness = 100
            fish.happiness = new_happiness