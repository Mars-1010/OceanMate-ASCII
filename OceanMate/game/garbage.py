# garbage.py
import random
def garbage_game(env):
    print("\nStarting the garbage cleaning game!")
    garbage_items = ["banana peel", "plastic bottle", "glass shard", "old fishing net", "rusty can"]

    # Select the quantity of garbage
    available = len(garbage_items)
    if available < 3:
        num_items = available  
    else:
        num_items = random.randint(3, available)

    selected = random.sample(garbage_items, k=num_items)

    print("You found some ocean garbage:")
    for item in selected:
        print(f" - {item}")
        input("Press ‘Enter’ to clean up...")  #Wait for Enter
        env.clarity += 1

    print("\nCleaning completed!")
    print(f"You gained +{num_items} clarity, current clarity is {env.clarity}")
    env.seawater += 500
    print("Bonus: You injected 500L of seawater!")