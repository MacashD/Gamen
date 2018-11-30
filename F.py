import V,time,random
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
		if item["name"] == V.Gold_Coin["name"] and V.backpack[x]["name"] == V.Gold_Coin["name"]:
			done = True
		elif V.backpack[x] == V.n and done == False:
			V.backpack[x] = item
			done = True
def display(var):
	cls()
	if var == V.ArmourSlots:
		varD = "Armour:"
	if var == V.baub_items:
		varD = "baubs:"
	print(varD,"\n")
	for i in range(0,len(var)):
		for x in range(0,len(var[i])):
			if x == 0:
				print(var[i]["name"])
			if len(var[i]) == 6:
				if x == 1:
					print(var[i]["effect"])
				if x == 4:
					print(var[i]["lore"])
		print("")
def displayBP():
	print("\nbackpack:\n")
	for x in range(0,len(V.backpack)):
		if V.Debug == False and V.backpack[x] != V.n and V.backpack[x] != V.backpack[0]:
			time.sleep(random.randint(1,2))
		if V.backpack[x]["name"] == "Gold coin":
			print(V.backpack[x]["amount"],V.backpack[x]["name"])
		else:
			if V.Debug == True:
				print(V.backpack[x])
			else:
				print(V.backpack[x]["name"])
def displayPS():
	cls()
	print("\nplayer stats:\n")
	print(V.Player_Stats[0],"health")
	print(V.Player_Stats[1],"defence")
	print(len(V.backpack),"backpack slots")
def equip():
	SLT = ["helmet","chestplate","leggings","boots","ring","chain","watch","powerstone"]
	for x in range(0,len(V.backpack)):
		done = False
		if len(V.backpack[x]) == 6:
			for i in range(0,len(SLT)):
				if done == False and V.backpack[x]["tag"] == SLT[i]:
					if i <= 4:
						V.ArmourSlots[i] = V.backpack[x]
					elif i > 4:
						i-=4
						V.baub_items[i] = V.backpack[x]
					V.backpack[x] = V.n
					done = True
def night():
	Decision = random.randint(1,3)
	if Decision == 3:
		Decision = random.randint(1,25)
		if Decision == 25:
			Decision = random.randint(1,125)
			if Decision == 125:
				V.moon[0],V.moon[1] = V.mooncolour[2],V.mooneffect[2]
		else:
			V.moon[0],V.moon[1] = V.mooncolour[1],V.mooneffect[1]
	else:
		V.moon[0],V.moon[1] = V.mooncolour[0],V.mooneffect[0]
def cls():
	print("\n"*100)
def EntCls():
	input("Enter to Continue")
	cls()
def Dots(seconds):
	for x in range(0,seconds):
		print(".")
		time.sleep(1)