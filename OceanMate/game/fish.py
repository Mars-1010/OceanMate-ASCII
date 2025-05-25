# fish.py

class Fish:
    def __init__(self, species, happiness=50, name=None):
        self.species = species  
        self.name = name or species  
        self.happiness = happiness

    def feed(self):
        if self.happiness < 100:
            self.happiness = min(self.happiness + 10, 100)
            print(f"{self.name} has been fed! Current happiness: {self.happiness}")
        else:
            print(f"{self.name} is already very happy (happiness maxed out)")

    def get_mood(self):
        if self.happiness >= 80:
            return "Happy"
        elif self.happiness >= 50:
            return "Normal"
        elif self.happiness >= 20:
            return "Low mood"
        else:
            return "About to die"

    '''
    #Support the save and load of game data
    def to_dict(self):
        return {
            "species": self.species,
            "name": self.name,
            "happiness": self.happiness
        }

    @staticmethod
    def from_dict(data):
        return Fish(
            species=data["species"],
            happiness=data.get("happiness", 50),
            name=data.get("name", data["species"])
        )
   '''
