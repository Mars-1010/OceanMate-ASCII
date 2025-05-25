# bubble.py
import random

def bubble_game(env):
    print("\n Starting the bubble catching game！")
    bubbles = random.sample(range(1, 21), 10)  
    
    golden_indexes = []
    for i, b in enumerate(bubbles):
        if b % 5 == 0:
            golden_indexes.append(i)

    print("These bubbles floated up.")

    for i, b in enumerate(bubbles):
        print(f"[{i}] {b}", end="   ")
    print("\nNote: Only bubbles divisible by 5 are golden bubbles!")

    # Player input
    selected = input("\nPlease enter the bubble indexes you want to catch (separated by spaces): ").split()
    hits = 0
    misses = 0

    for s in selected:
        if not s.isdigit():
            continue
        index = int(s)
        if 0 <= index < len(bubbles):
            if bubbles[index] % 5 == 0:
                hits += 1
            else:
                misses += 1
        else:
            print(f"Index {index} does not exist, treated as a miss.")
            misses += 1

    env.feed_tokens += hits
    env.clarity -= misses * 5
    print(f"\n Hit {hits} golden bubbles, feeding opportunities +{hits}")
    print(f" Missed {misses} bubbles, clarity -{misses * 5}")
    print(f"Current feeding opportunities: {env.feed_tokens}, clarity: {env.clarity}")