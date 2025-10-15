
from collections import Counter
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.personality = personality
        self.furniture = []
    
    def set_catchphrase(self, new_catchphrase):
        is_alphabetic_and_whitespace = all(c.isalpha() or c.isspace() for c in new_catchphrase)
        
        if len(new_catchphrase) > 0 and len(new_catchphrase) < 20 and is_alphabetic_and_whitespace:
            self.catchphrase = new_catchphrase
        else:
            print(f"'{new_catchphrase}' is not a valid catchphrase.")
    def add_item(self, item_name):
        items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        itemset = set(items)
        if item_name in itemset:
            self.furniture.append(item_name)
    def print_inventory(self):
        if(not self.furniture):
            print("Inventory empty")
        cnt = Counter(self.furniture)
        inventory_parts = [f"{key}: {value}" for key, value in cnt.items()]
        
        inventory_str = ", ".join(inventory_parts)
        
        print(inventory_str)
        
# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()
    

"""alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)"""

"""alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)"""

def of_personality_type(townies, personality_type):
    res = []
    for v in townies:
        if v.personality == personality_type:
            res.append(v.name)
    return res

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

