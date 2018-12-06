import V,time,random
def Fdecision(question,options,Foutput):
	DecisionMade = False
	while DecisionMade == False:
		print("\n\n\n")
		Finput = input(question).lower()
		for i in range(0,len(options)):
			for x in range(0,len(options[i])):
				if Finput == options[i][x]:
					result,DecisionMade = Foutput[i],True
	return result
def item_to_backpack(item,container):
	done = False
	for x in range(0,len(container)):
		if item["name"] == V.Gold_Coin["name"] and container[x]["name"] == V.Gold_Coin["name"]:
			done = True
		elif container[x] == V.n and done == False:
			container[x],done = item,True
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
					def ItemReplace(slot):
						print(V.backpack[x],slot[i])
						if V.backpack[x]["name"] != slot[i]["name"]:
							slot[i] = V.backpack[x]
							V.backpack[x] = V.n
						else:
							print(SLT[i],"slot full")
							EntCls()
					if i <= 4:
						ItemReplace(V.ArmourSlots)
					if i > 4:
						i -= 4
						ItemReplace(V.baub_items)
					done = True
def night():
	if random.randint(1,3) == 3:
		if random.randint(1,25) == 25:
			if random.randint(1,125) == 125:
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