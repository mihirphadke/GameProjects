class GameObject:
    def __init__(self, name):
        self.name = name

class Location(GameObject):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.connections = {}
        self.items = []
        self.characters = []

    def add_connection(self, direction, location):
        self.connections[direction] = location

    def describe(self):
        print(self.description)

class Character(GameObject):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health

class Player(Character):
    def __init__(self, name, health, location):
        super().__init__(name, health)
        self.location = location
        self.inventory = []

    def move(self, direction):
        if direction in self.location.connections:
            self.location = self.location.connections[direction]
            print(f"You are now in {self.location.name}.")
        else:
            print("You cannot go in that direction.")

class Item(GameObject):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

def create_world():
    room1 = Location("Room 1", "This is room 1.")
    room2 = Location("Room 2", "This is room 2.")
    room3 = Location("Room 3", "This is room 3.")

    room1.add_connection("north", room2)
    room2.add_connection("south", room1)
    room2.add_connection("east", room3)
    room3.add_connection("west", room2)

    sword = Item("Sword", "A sharp, shiny sword.")
    room1.items.append(sword)

    player = Player("Player", 100, room1)

    return player

def main():
    player = create_world()

    while True:
        player.location.describe()

        action = input("What do you want to do? ").lower().split()

        if len(action) == 0:
            continue
        elif action[0] == "quit":
            break
        elif action[0] == "move":
            if len(action) > 1:
                player.move(action[1])
            else:
                print("Please specify a direction.\n")
        else:
            print("Unknown action.")

if __name__ == "__main__":
    main()