import os
class Controller:
  def play_game(self):
    global world
    world = World()
    world.create_world()
    while True:
      triforcecount = 0
      for i in world.itemnames:
        for j in player.inventory:
          if i == j:
            triforcecount += 1
      if triforcecount == 3:
        print("woop woop you won!!!!!!")
        break
      else: 
        print("what do you want to do?\n")
        print("answer 0 to describe the room you are in\n")
        print("answer 1 to move to another room\n")
        print("answer 2 to pick up an item in the room\n")
        print("answer 3 to check your inventory\n")
        try:
          invoer = int(input("your answer: "))

          os.system("cls")
          
          if invoer == 0:
            print(" ")
            player.location.describe()
          elif invoer == 1:
            roominvoer = input(" \nok, what room do you want to go to? ")
            os.system("cls")
            player.go_to_room(roominvoer)
          elif invoer == 2:
            iteminvoer = input(" \nok, what item do you want to pick up? ")
            os.system("cls")
            player.pick_up_item(iteminvoer)
          elif invoer == 3:
            print("")
            player.check_inventory()
          else: 
            print("")
            print("choose from one of the numbers above\n")
        except ValueError:
          print("")
          print("put in a number\n")

        
class World:
  def __init__(self, insertrooms = [], insertitems = []):
    self.rooms = insertrooms
    self.items = insertitems
  
  def create_world(self):
    global tf1
    global tf2
    global tf3
    tf1 = Item("triforce of power")
    tf2 = Item("triforce of wisdom")
    tf3 = Item("triforce of courage")
    global room1
    global room2
    global room3
    global room4
    room1 = Room("your house", ["the dungeon"])
    room2 = Room("the dungeon", ["your house", "the forest"], ["triforce of power"])
    room3 = Room("the forest", ["the dungeon", "the ancient castle"], ["triforce of wisdom"])
    room4 = Room("the ancient castle", ["the forest"], ["triforce of courage"])
    self.rooms = [room1, room2, room3, room4]
    self.items = [tf1, tf2, tf3]
    self.itemnames = [tf1.name, tf2.name, tf3.name]
    global player
    player = Player("lonk", self.first_room())

  def first_room(self):
    return room1


class Room:
    def __init__(self, insertname, insertexits = [], insertitems = []):
        self.exits = insertexits
        self.items = insertitems
        self.name = insertname
    
    def add_exit(self, room):
      self.exits.append(room)

    def describe(self):
      print("your location is: " + self.name + "\n")
      if self.exits == []:
        print("this room has no exits" + "\n")
      else:
        print("this room leads to: " + ', '.join(self.exits) + "\n")
      if self.items == []:
        print("there are no items in this room" + "\n")
      else:
        print("items in this room are: " + ', '.join(self.items) + "\n")


    def add_item(self, item):
      self.items.append(item)

    def remove_item(self, item):
      self.items.remove(item)


class Item():
  def __init__(self, insertname, inserttype = "triforce"):
    self.name = insertname
    self.type = inserttype

class Player():
  def __init__(self, insertname, insertlocation, insertinventory = []):
    self.name = insertname
    self.inventory = insertinventory
    self.location = insertlocation

  def go_to_room(self, name):
    if name in self.location.exits:
      for room in world.rooms:
        if room.name == name: 
          self.set_current_room(room)
    else:
      print("that is not an exit in this room" + "\n")

  def set_current_room(self, room):
    self.location = room
    print("your location is now " + room.name + "\n")

  def get_current_room(self):
    print(self.location.name)

  def pick_up_item(self, item):
    if item in self.location.items:
      self.inventory.append(item)
      print("you picked up " + item + "\n")
      self.location.remove_item(item)
    else:
      print("item doesn't exist here" + "\n")
  
  def check_inventory(self):
    if self.inventory == []:
      print("your inventory is empty" + "\n")
    else:
      print("your inventory contains: " + ", ".join(self.inventory) + "\n")



controller = Controller()
controller.play_game()
