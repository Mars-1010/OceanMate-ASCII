# Main script to run: use python3 main.py

from env import Environment  #Create an aquarium
from game.garbage import garbage_game
from game.bubble import bubble_game
from game.fish import Fish
from env import ADOPTION_CATALOG  #Show the fish that can be raised
from game.chase import chase_game
#Let the fish swim
from game.display import view_aquarium
from game.action import feed_animation

# Initialize the environment
env = Environment() 
#env.load()
print(f"Current seawater: {env.seawater}L")


#env.save()

#Game start
def show_menu():
    print("\n=== OceanMate Menu ===")
    print("1. Check the status")
    print("2. Clear the rubbish （Add seawater）")
    print("3. Scoop up bubbles（Feed chance）")
    print("4. Chase the Light Point （Add happiness）")
    print("5. Feed the fish ")
    print("6. Adoption Center")
    print("7. View the aquarium ")
    print("8. Save and exit")


while True:
    show_menu()
    choice = input("Options（1-8）：")

    if choice == "1":
        print(f"seawater: {env.seawater}L, clarity: {env.clarity}, feed_tokens: {env.feed_tokens}")

    elif choice == "2":
        garbage_game(env)
        print("Add 500L seawater！")

    elif choice == "3":
        bubble_game(env)

    elif choice == "4":
         chase_game(env)

    elif choice == "5":
        if env.feed_tokens > 0 and env.animals:
            feed_animation()  
            for fish in env.animals:
                fish.feed()
            env.feed_tokens -= 1
        else:
            print(" You have no chance to feed or no fish!")

    elif choice == "6":
        print("\nAdoption Center Overview:")
        for name in ADOPTION_CATALOG:
            cost = ADOPTION_CATALOG[name]["cost"]
            clarity_required = ADOPTION_CATALOG[name]["clarity"]

            if env.seawater >= cost and env.clarity >= clarity_required:
                can_adopt = True
            else:
                can_adopt = False
            if can_adopt:
                status = "Available for adoption"
            else:
                status = "Insufficient conditions"
            print(f"- {name}：need {cost}L seawater，clarity ≥ {clarity_required}（{status}）")

        adopt_name = input("Please enter the name of the animal you want to adopt (or press Enter to cancel): ").strip().title()
        if adopt_name in ADOPTION_CATALOG:
            cost = ADOPTION_CATALOG[adopt_name]["cost"]
            clarity_req = ADOPTION_CATALOG[adopt_name]["clarity"]
            if env.seawater >= cost and env.clarity >= clarity_req:
                env.seawater -= cost
                env.animals.append(Fish(species=adopt_name))
                print(f"Successfully adopted {adopt_name}！Current seawater remaining：{env.seawater}L")
            else:
                print("Insufficient conditions for adoption.")
        else:
            print("Unidentified animal names or cancel the operation.")
    elif choice == "7":
        view_aquarium(env)

    elif choice == "8":
        #env.save()
        print("Game state saved, exiting!")
        break

    else:
        print("Invalid input, please try again.")

