#  env.py
#import json  #Archive and save
#import os    #Create folder
from game.fish import Fish

class Environment:
    def __init__(self):
        self.seawater = 0
        self.clarity = 100
        self.feed_tokens = 0
        self.animals = [Fish("Clownfish"), Fish("Blue Tang")]  
        self.achievements = []

    '''
    #Save the game progress
    def save(self, filename="save_data/game_state.json"):
        folder = os.path.dirname(filename)
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Package the status of the aquarium into a dictionary
        data = {
            "seawater": self.seawater,
            "clarity": self.clarity,
            "feed_tokens": self.feed_tokens,
            "achievements": self.achievements,
            "animals": [fish.to_dict() for fish in self.animals]
        }

        #Save the game data to the file
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    #Load game data 
    def load(self, filename="save_data/game_state.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.seawater = data.get("seawater", 0)
                self.clarity = data.get("clarity", 100)
                self.feed_tokens = data.get("feed_tokens", 0)
                self.achievements = data.get("achievements", [])
                # put fish into self.animals 
                self.animals = []
                for f in data.get("animals", []):
                    fish = Fish.from_dict(f)
                    self.animals.append(fish)
        except FileNotFoundError:
            print("No save file found, starting new game.")
        except Exception as e:
            print(f"Error: {e}")
    '''

# Adoption catalog（Fish Rule Table）
ADOPTION_CATALOG = {
    "Clownfish": {"cost": 50, "clarity": 0},
    "Blue Tang": {"cost": 100, "clarity": 10},
    "Seahorse": {"cost": 150, "clarity": 20},
    "Coral": {"cost": 250, "clarity": 30},
    "Crab": {"cost": 300, "clarity": 25},
    "Sea Turtle": {"cost": 350, "clarity": 40},
    "Jellyfish": {"cost": 400, "clarity": 50},
    "Shark": {"cost": 500, "clarity": 70},
    "Octopus": {"cost": 700, "clarity": 80},
    "Whale": {"cost": 1000, "clarity": 90}
}