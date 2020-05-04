
############# story line zone

# Hooray this is the begining!



choice = None  # the varibale to assinging inputs to


def theBegining():
	while True:
		print( "Hello welcome to a brand new adventure in a glaxie simulator just generated.\n\nYour the contestant!\n\nOur generator has givin you the name MUG.\n\nWould you like to begin?\n")
		choice = input()
		if choice.lower() == "yes":
			print("Great!\n")
			break

		else:
			print("Well this is akward\n")

def part1_TheGoblinBreserkes ():
	print("At the start of this adventure you begin like every other adventure. In the middle of a clearing in the forest. Of course you have no idea where you came from or who you are. What you do know is that you have a wooden stick and your name is MUG. (It is acctually quite rare for you to know what your name is at the start of a adventure)\n")
	print("In this adventure you will use voice commands to control yourself. Lets learn a few. \n\nType Items into the console to look at your curent inventory")
	choice = input()
	openItems(choice)


########### storyline zone


def openItems(choice): # opens your inventory
	if choice.lower() == "items":
		print("Items:\n")
		if len(currentCharacter.items) == 0:
			print("You do not have any items right now\n")
		else:
			for i in currentCharacter.items:
				print(i.name + "\n")

characters = [] # list of all the characters

#the type character. 
class character:
  def __init__(self,health,Class):
    self.weapon = None
    self.items = []
    self.Class = Class
    self.isUnlocked = False



# creates a character with stats (health,class)
def createCharacter(health,Class):
	char = character(health,Class)
	characters.append(char)


createCharacter(5,"warrior") # example character


currentCharacter = characters[0] # the curent character
currentCharacter.isUnlocked = True #make the curent character unlocked so its not dumb

allItems = []


class rec:
  def __init__(self,name,num):
    self.name = name
    self.num = num


class itemClass:
  def __init__(self,name,txt):
    self.name = name
    self.recs = []


class item:
  def __init__(self,name):
    
  	pass

while True:
	theBegining()
	part1_TheGoblinBreserkes()
