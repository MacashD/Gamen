#changelog:
import time
import random 
Y,N = ["yes","y","fuck yes"],["no","n","fuck off","3"]
op1,op2,op3,op4 = ["1","one"],["2","two"],["3","three"],["4","four"]
running,cont,ENT,Decision,CP = True,False,0,0,1
n = ["nothing"]
#gamestuff
RI = random.randint(1,100)
if RI == 100:
	the_big_variable = "something to do"
else:
	the_big_variable = "*and that other shit you mortals need to stay alive...*"
Phealth = 20
#mainhand
mainhand = n
#items
Gold_Coin = ["Gold coin",0,"can be used as a currency in some societys"]
# [name,damage,durability,]
oakstick = ["oak stick",1,25]
flintstone = ["flint stone",10,0]
small_pebbles = ["small pebbles",2,0]
Delta_Rune = ["Delta Rune","revive once in battle",0,1,"'seems to be eminating a powerful aura... you are filled with determination'","powerstone"]
TurtleShell = ["turtle shell","lightweight\nhard",15,15,"'an empty turtle shell... seems like it fits you'","chestplate"]
#delta rune is a power_stone
# baubs: name,effect,durability,damage,lore            watch item is for pimp/rapper joke
ring = ["nothing","",0,0,"","ring"]
chain = ["nothing","",0,0,"","chain"]
watch = ["nothing","",0,0,"","watch"]
power_stone = ["nothing","",0,0,"","powerstone"]
# armour: name,effect,durability,defense,lore
helm = ["nothing","",0,0,"","helmet"]
chestplate = ["nothing","",0,0,"","chestplate"]
leggings = ["nothing","",0,0,"","leggings"]
boots = ["nothing","",0,0,"","boots"]
ArmourSlots = [helm,chestplate,leggings,boots]
backpack = [n,n,n,n,n,n,n,n,n,n]
baub_items = [ring,chain,watch,power_stone]
#backpack slots
#player stats
#pstattest = open("Player stats","W")
#print(pstattest)
Player_Stats = [Phealth,backpack,baub_items,mainhand]
#functions
def Fdecision(question,options,Foutput):
	DecisionMade = False
	while DecisionMade == False:
		print("\n\n\n")
		Finput = input(question).lower()
		for i in range(0,len(options)):
			for x in range(0,len(options[i])):
				if Finput == options[i][x]:
					result = Foutput[i]
					DecisionMade = True
	return result
def item_to_backpack(item,backpack):
	done = False
	for x in range(0,len(backpack)):
		if item[0] == Gold_Coin[0] and backpack[x][0] == Gold_Coin[0]:
			done = True
		elif backpack[x] == n and done == False:
			backpack[x] = item
			done = True
def display(var):
	print("")
	for i in range(0,len(var)):
		for x in range(0,len(var[i])):
			if x == 0 or x == 1 or x == 4:
				print(var[i][x])
		print("")
def displayBP():
	print("\n")
	print("backpack:\n")
	for x in range(0,len(backpack)):
		if Debug == False and backpack[x] != n and backpack[x] != backpack[0]:
			time.sleep(random.randint(1,2))
		if backpack[x][0] == "Gold coin":
			print(backpack[x][1],backpack[x][0])
		else:
			print(backpack[x][0])
	input()
def equip():
	done = False
	SLT = ["helmet","chestplate","leggings","boots","ring","chain","watch","powerstone"]
	for x in range(0,len(backpack)):
		if len(backpack[x]) == 6:
			for i in range(0,len(SLT)):
				if done == False and backpack[x][5] == SLT[i]:
					if i <= 4:
						ArmourSlots[i] = backpack[x]			
					elif i > 4:
						i=i-4
						baub_items[i] = backpack[x]
					backpack[x] = n
					done = True
def cls():
	print("\n"*100)
def EntCls():
	input()
	cls()
#functions
#st
print("this is a txt based adventure game thing\nversion 0.0.2\nOOF, enter to continue")
Decision = input()
if Decision == "DEBUG":
	cls()
	print("debug mode activated")
	Debug = True
	FH = True
	input()
elif Decision == "1517":
	cls()
	print("hallifordian?")
	FH = True
	Debug = False
	input()
else:
	Debug = False
	FH = False
cls()
Foutput = ["R","WEEB","XTREEM MEME"]
Q = "what gamemode do you wanna play\n \nregular or\nweeb mode or\nmemay mode"
R,W,M = ["regular","r"],["weeb","weebmode","w"],["meme","mememode","m"]
options = [R,W,M]
GM = Fdecision(Q,options,Foutput)
cls()
if GM == "R":
	options = [op1,op2,op3,op4]
	Foutput = ["oakstick","flintstones","smallpebbles","nothing"]
	Q = "pick a starting weapon\n1 for an oak stick\n2 for 3 flint stones\n3 for 16 small pebbles\n4 for no starting weapon ONLY FOR THE MOST ARDCORE OF MADLADS"
	Decision = Fdecision(Q,options,Foutput)
	if Decision == "oakstick":
		item_to_backpack(oakstick,backpack)
	elif Decision == "flintstones":
		flintstone[2] = 3
		item_to_backpack(flintstone,backpack)
	elif Decision == "smallpebbles":
		small_pebbles[2] = 16
		item_to_backpack(small_pebbles,backpack)
	elif Decision == "nothing":
		print("goodluck")
		EntCls()
	cls()
	while running == True:
		if cont == True:
			cls()
			if CP == 1:
				#checkpoint
				if Debug == True:
					RI = 25
				else:
					RI = random.randint(1,25)
				if RI == 25:
					print("event1: the big gae approaches")
					time.sleep(5)
					print("nah jk wouldnt be that mean to drop a b0ss battle on the first CP")
					time.sleep(2)
					for x in range(0,3):
						print(".")
						time.sleep(1)
					print("here have an upgrade to your stick or something")
					for x in range(0,len(backpack)):
						if backpack[x] == oakstick:
							oakstick = ["oak stick",1.25,35]
							backpack[x] = n
							item_to_backpack(oakstick,backpack)
							print("your oak stick gained 0.25 damage and 10 durability",oakstick)
							EntCls()
					if backpack[0] != oakstick:
						print("oh you dont have a stick, sorry thought you did")
						time.sleep(7)
						print("well bye")
						time.sleep(0.5)
						EntCls()
				CP_1_VillageReward_s = random.randint(250,750)
				#personal messages
				if FH == True:
					print("here are what some people have decided to say to you")
					RI = random.randint(1,200)
					if RI == 200:
						print("This is a crap game")
					RI = random.randint(1,10)
					if RI == 10:
						print("r,u,nor,mal")
					RI = random.randint(1,1000000000)
					if RI == 1000000000:
						print("seyon: fuck you")
					RI = random.randint(1,1000)
					if RI == 1000:
						print("adam is lgbt")
					EntCls()
				#personal messages
				dragon_quest_info = ["_st_ \ndragon or some shit fucked everything \nreward:",CP_1_VillageReward_s,"Gold \nplz help or someshit \n(it seems like in this village they speak english normaly apart from replacing something with someshit)"]
				print(dragon_quest_info[0],dragon_quest_info[1],dragon_quest_info[2])
				options = [Y,N]
				Foutput = ["yes","no"]
				Q="y / n"
				Decision = Fdecision(Q,options,Foutput)
				if Decision == "yes":
					cls()
					print("(you accepted the quest)")
					print("dshit")
					EntCls()
					Gold_Coin[1] = Gold_Coin[1] + CP_1_VillageReward_s
					item_to_backpack(Gold_Coin,backpack)
					#remember this optional bit needs to flow with the rest of the game
				else:
					cls()
					print("(you declined the quest)")
					EntCls()
				print("you continue on, walking down the path")
				time.sleep(1)
				print("the sun slowly decending beneath the horison")
				time.sleep(3)
				print("the journey seems long and you are running low on food, water and",the_big_variable," but you know that something will come up")
				time.sleep(2)
				print("sadly you havent found anything and its dark and you will probably be fucked if you stay out in the dark for too long")
				time.sleep(1)
				print("so i would suggest to find a place to settle down")
				time.sleep(1)
				Q = "options:\n1 for: the ground\n2 for: a bare tree\n3 for: dont"
				ground,TreeByRoad = ["ground","g","1"],["tree","t","the fucking tree","2"]
				options = [ground,TreeByRoad,N]
				Foutput = ["ground","tree","no"]
				Decision = Fdecision(Q,options,Foutput)
				cls()
				if Decision == "ground":
					print("ground = true")
				elif Decision == "tree":
					print("they are sleeping in the tree")
				elif Decision == "no":
					print("(you decided not to sleep,\n seconds later you hear a distant voice saying,\n sleep is for the weak)")
					time.sleep(2)
					for x in range(0,3):
						print(".")
						time.sleep(1)
					print("(it sounds like it came from very far away so you decide to ignore it)")
					EntCls()
					#continue
				CP = 2
			elif CP == 2:
				#checkpoint2
				cls()
				RI = random.randint(1,3)
				if RI == 3:
					print("event1: big b0ss battle\n\nGaint fucking turtle!")
					print("add combat shit here")
					print("you got a turtle shell")
					item_to_backpack(TurtleShell,backpack)
					#remember to cls()
				print("gamen2")
				input()
			cont = False
		cls()
		print("you are at CP:",CP)
		ENT = input("enter bp to check your backpack or c to continue\nbaubs for baub items\nar for armour").lower()
		if ENT == "continue" or ENT == "c":
			cont = True
		if ENT == "backpack" or ENT == "bp":
			displayBP()
		if ENT == "baubs" or ENT == "ba":
			display(baub_items)
			print("(to equip baub items enter equip)")
			EntCls()
		if ENT == "armour" or ENT == "ar":
			display(ArmourSlots)
			print("(to equip armour enter equip)")
			EntCls()
		if ENT == "equip":
			equip()
		if Debug == True and ENT == "/as":
			backpack = backpack + [n]
		if Debug == True and ENT =="/var":
			print(globals())
			EntCls()
		if Debug == True and ENT == "/add gold":
			Gold_Coin[1] = Gold_Coin[1] + int(input("amount?"))
			item_to_backpack(Gold_Coin,backpack)
elif GM == "WEEB":
	print("add weeb version here")
	print("add owo stuff l = w and r = w")
elif GM == "XTREEM MEME":
	print("extreem memer version here")
