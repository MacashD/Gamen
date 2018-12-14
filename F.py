# FUNCTIONS
import V,time,random
def Fdecision(question,options,Foutput): # use: for decisions
	DecisionMade = False
	while DecisionMade == False: # iterates if the input is not in Foutput
		print("\n\n\n") # space 
		Finput = input(question).lower() #outputs the question and takes an input into Finput
		for i in range(0,len(options)): # for each option
			for x in range(0,len(options[i])): # for each option validation
				if Finput == options[i][x]: # decision
					result,DecisionMade = Foutput[i],True # result
	return result
def item_to_container(item,container): # takes an item and moves it to a container
	done = False # done is to make it only iterate once while it searches for space in container
	for x in range(0,len(container)): # checks for a space in a container
		if item["name"] == V.Gold_Coin["name"] and container[x]["name"] == V.Gold_Coin["name"]:
			done = True # if there is a goldcoin in the container it will be added to the stack otherwise it will be put in
		elif container[x] == V.n and done == False: # checks for free space
			container[x],done = item,True # adds item to container's free space
def display(var): # displays armour/baub slots  
	cls()
	if var == V.ArmourSlots: # title either armour:
		varD = "Armour:"
	if var == V.baub_items: # or baubs:
		varD = "baubs:"
	print(varD,"\n") # displays title
	for i in range(0,len(var)): # for each armour/baub piece
		for x in range(0,len(var[i])): # for thier stats
			if x == 0:
				print(var[i]["name"]) #prints name at 0
			if len(var[i]) == 6: # if the slot has an item with a length of 6
				if x == 1: # print the effect text
					print(var[i]["effect"])
				if x == 4: # print the lore text
					print(var[i]["lore"])
		print("")
def displayBP(): # displays items in the backpack
	print("\nbackpack:\n") # displays title
	for x in range(0,len(V.backpack)): # checks every item in backpack
		if V.Debug == False and V.backpack[x] != V.n and V.backpack[x] != V.backpack[0]:
			time.sleep(random.randint(1,2)) # if its not the first item or the user is not in debug mode
		if V.Debug == True: # debug prints all values
			print(V.backpack[x])
		else:
			if V.backpack[x]["name"] == "Gold coin": # if its a gold coin it displays 
				print(V.backpack[x]["amount"],V.backpack[x]["name"])# the amount and the name
			else:
				print(V.backpack[x]["name"]) # regular items just the name
def displayPS(): # displays player stats
	cls()
	print("\nplayer stats:\n") # title
	print(V.Player_Stats[0],"health") # health
	print(V.Player_Stats[1],"defence") # defence points
	print(len(V.backpack),"backpack slots") # backpack slots
def equip(): # equips an item from the backpack to its slot by its tag
	tag = ["helmet","chestplate","leggings","boots","ring","chain","watch","powerstone"]
	for x in range(0,len(V.backpack)):# checks each item in the backpack
		done = False # wrong iteration protection
		if len(V.backpack[x]) == 6: # if the items length is 6 then
			for i in range(0,len(tag)): # it will loop for all the tags 
				if done == False and V.backpack[x]["tag"] == tag[i]:#if its not done and the tag is found 
					def ItemReplace(slot): # replaces item
						if V.backpack[x]["name"] != slot[i]["name"]: #if the slot has an item it will say
							slot[i] = V.backpack[x] # moves from backpack to slot
							V.backpack[x] = V.n
						else:
							if slot == V.baub_items: # the tags slot is full
								print(tag[i+4],"slot full")
							else:
								print(tag[i],"slot full")
							EntCls() # so the user can see
					if i <= 4:
						ItemReplace(V.ArmourSlots) # 1 to 4 is armour slots
					if i > 4:
						i -= 4
						ItemReplace(V.baub_items) # 5 to 8 is baub slots
					done = True 
def night(): # determines moons properties
	if random.randint(1,3) == 3: # 2 in 3 of a blue moon
		if random.randint(1,25) == 25: # 1 in 3 of a white moon
			if random.randint(1,125) == 125: # very small chance of red moon
				V.moon[0],V.moon[1] = V.mooncolour[2],V.mooneffect[2]
		else:
			V.moon[0],V.moon[1] = V.mooncolour[1],V.mooneffect[1]
	else:
		V.moon[0],V.moon[1] = V.mooncolour[0],V.mooneffect[0]
def cls(): # clears screen!
	print("\n"*100)
def EntCls(): # clears screen after the user enters
	input("Enter to Continue")
	cls()
def Dots(seconds): # like time.sleep() but with dots!
	for x in range(0,seconds):
		print(".")
		time.sleep(1)
def splash(): # splash text (random stuff the game says when you start it) like minecraft's
	cls()
	splash = ["SUBSCRIBE TO PEWDIEPIE","you should really subscribe to pewdiepie on youtube","sub2pewdiepie","DO YOUR PART! (subscribe to pewdiepie)","if you dont subscribe to pewdiepie this game wont work correctly","sub to pewdiepie","it is imperatively important that you subcribe to pewdiepie","click the link and click subscribe to pewdiepie","SUBSCRIBE TO PEWDIEPIE GODDAMIT"]
	print("\n" + random.choice(splash),"\nhttps://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw?sub_confirmation=1")