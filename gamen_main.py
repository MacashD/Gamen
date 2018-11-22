#changelog:
import time,random,F,V,CP1,CP2
print("this is a txt based adventure game thing\nversion 0.0.2\nOOF, enter to continue")
Decision = input()
if Decision == "DEBUG":
	F.cls()
	print("debug mode activated")
	V.Debug = True
	V.FH = True
	input()
elif Decision == "1517":
	F.cls()
	print("hallifordian?")
	V.FH = True
	V.Debug = False
	input()
F.cls()
Foutput = ["R","WEEB","XTREEM MEME"]
Q = "what gamemode do you wanna play\n \nregular or\nweeb mode or\nmemay mode"
R,W,M = ["regular","r"],["weeb","weebmode","w"],["meme","mememode","m"]
options = [R,W,M]
GM = F.Fdecision(Q,options,Foutput)
F.cls()
if GM == "R":
	options = [V.op1,V.op2,V.op3,V.op4]
	Foutput = ["oakstick","flintstones","smallpebbles","nothing"]
	Q = "pick a starting weapon\n1 for an oak stick\n2 for 3 flint stones\n3 for 16 small pebbles\n4 for no starting weapon ONLY FOR THE MOST ARDCORE OF MADLADS"
	Decision = F.Fdecision(Q,options,Foutput)
	if Decision == "oakstick":
		F.item_to_backpack(V.oakstick,V.backpack)
	elif Decision == "flintstones":
		V.flintstone[2] = 3
		F.item_to_backpack(V.flintstone,V.backpack)
	elif Decision == "smallpebbles":
		V.small_pebbles[2] = 16
		F.item_to_backpack(V.small_pebbles,V.backpack)
	elif Decision == "nothing":
		print("goodluck")
		F.EntCls()
	F.cls()
	while V.running == True:
		if V.cont == True:
			F.cls()
			V.CP += 1
			#CP's
			if V.CP == 1:
				CP1.CP1()
			elif V.CP == 2:
				CP2.CP2()
			else:
				print("end of cps")
				F.EntCls()
			V.cont = False
		F.cls()
		print("you are at CP:",V.CP+1)
		ENT = input("enter bp to check your backpack or c to continue").lower()
		if ENT == "continue" or ENT == "c":
			V.cont = True
		if ENT == "backpack" or ENT == "bp":
			F.displayBP()
			BP_MENU = input("\nenter baubs for baub items\nar for armour\nor st/stats to see your stats")
			if BP_MENU == "stats" or BP_MENU == "st":
				F.displayPS()
				F.EntCls()
			if BP_MENU == "baubs" or BP_MENU == "ba":
				F.display(V.baub_items)
				Decision == input("(to equip baub items enter equip)")
				if Decision == "equip":
					F.equip()
			if BP_MENU == "armour" or BP_MENU == "ar":
				F.display(V.ArmourSlots)
				Decision = input("(to equip armour enter equip)")
				if Decision == "equip":
					F.equip()
			if BP_MENU == "equip":
				F.equip()
		if ENT == "equip":
			F.equip()
		if V.Debug == True and ENT == "/as":
			V.backpack += [V.n]
		if V.Debug == True and ENT =="/var":
			print(globals())
			F.EntCls()
		if V.Debug == True and ENT == "/add gold":
			V.Gold_Coin[1] += int(input("amount?"))
			F.item_to_backpack(V.Gold_Coin,V.backpack)
		if V.Debug == True and ENT == "save game":
			print("NO")
elif GM == "WEEB":
	print("add weeb version here")
	print("add owo stuff l = w and r = w")
elif GM == "XTREEM MEME":
	print("extreem memer version here")