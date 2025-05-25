#display.py
# ASCII function
import os
import time
import random
import sys
import select
def get_ascii_art(species):
    if species == "Clownfish":  
        return [
            "     __     ",
            " ><((° >    ",
            "     ‾‾     "
        ]
    elif species == "Blue Tang":  
        return [
            "           ",
            "  <>><<    ",
            "           "
        ]
    elif species == "Seahorse":  
        return [
            "   _o)     ",
            "  ((       ",
            "   @\\      "
        ]
    elif species == "Coral":  
        return [
            "   ((      ",
            "   ))      ",
            "-—||—-     "
        ]
    elif species == "Crab":  
        return [
            "  <\\   />  ",
            "  (='o_o'=)",
            "  //   \\\\  "
        ]
    elif species == "Sea Turtle":  
        return [
            "   ___     ",
            "  (._.)    ",
            "           "
        ]
    elif species == "Jellyfish":  
        return [
            "           ",
            "  (*)      ",
            " )) ((     "
        ]
    elif species == "Shark":  
        return [
            "           ",
            "< ─ ─ ─ ─ 《《《",
            "           "
        ]
    elif species == "Octopus":  
        return [
            "   @@@@    ",
            "  ( o o )  ",
            "  /|_|_|\\  "
        ]
    elif species == "Whale":  
        return [
            "    ^      ",
            "< == = == 《",
            "    ^      "
        ]
    else:    #unknown species
        return [
            "   ???     ",
            "  (o_o)<<  ",
            "           "
        ]


# Show all the fish in the aquarium (can swim)
def view_aquarium(env, frames=15, delay=0.3, fish_per_row=4):
    wave_chars = ["~", ".", "`", "'", " "]
    display_width = 80

    print("Press Enter at any time to stop the animation...\n")

    for frame in range(frames):
        # Enter（quit)
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            input()  
            print("\n The animation has ended. Return to the menu.\n")
            break

        try:
            os.system('clear')
        except:
            pass

        print("\n=== OceanMate ===\n")

        # display fish
        all_fish_blocks = []
        for fish in env.animals:
            art = get_ascii_art(fish.species)  # get fish ASCII art
            shifted_art = []
            offset_spaces = frame * 2  # Shift 2 Spaces to the right in each frame

            for line in art:
                shifted_line = " " * offset_spaces + line.ljust(15)  # Offset + Fill
                shifted_art.append(shifted_line)

            all_fish_blocks.append(shifted_art)  # Line by line display

        # There are at most four fish in one row（grouping)
        fish_per_row = 4 
        grouped = []  

        for i in range(0, len(all_fish_blocks), fish_per_row):
            group = all_fish_blocks[i:i + fish_per_row]
            grouped.append(group)

        # Print each group
        for group in grouped:
            for row_index in range(3):  # Each fish occupies three rows
                bg = ""
                for _ in range(5):
                    wave = random.choice(wave_chars)
                    bg += wave

                # Print a line of fish
                row = ""
                for fish in group:
                    row += fish[row_index] + "  "  # Leave space between the fish
           
                print(bg + row)

            # Print a blank line to separate different fish groups
            print()

        time.sleep(delay)