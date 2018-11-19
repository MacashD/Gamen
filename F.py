import V
import time
import random
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
		if item[0] == V.Gold_Coin[0] and V.backpack[x][0] == V.Gold_Coin[0]:
			done = True
		elif V.backpack[x] == V.n and done == False:
			V.backpack[x] = item
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
	for x in range(0,len(V.backpack)):
		if V.Debug == False and V.backpack[x] != V.n and V.backpack[x] != V.backpack[0]:
			time.sleep(random.randint(1,2))
		if V.backpack[x][0] == "Gold coin":
			print(V.backpack[x][1],V.backpack[x][0])
		else:
			print(V.backpack[x][0])
	input()
def equip():
	done = False
	SLT = ["helmet","chestplate","leggings","boots","ring","chain","watch","powerstone"]
	for x in range(0,len(V.backpack)):
		if len(V.backpack[x]) == 6:
			for i in range(0,len(SLT)):
				if done == False and V.backpack[x][5] == SLT[i]:
					if i <= 4:
						V.ArmourSlots[i] = V.backpack[x]
					elif i > 4:
						i=i-4
						V.baub_items[i] = V.backpack[x]
					V.backpack[x] = V.n
					done = True
def cls():
	print("\n"*100)
def EntCls():
	input("Enter to Continue")
	cls()