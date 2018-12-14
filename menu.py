import time,random,V,F
def bpmenu(main):
	done = False
	while done == False:
		print("you are at CP:",V.CPC+1)
		ENT = input("enter bp to check your backpack or c to continue").lower()
		if main == True and ENT == "continue" or ENT == "c":
			V.cont = True
			done = True
		if main == False and ENT == "continue" or ENT == "c":
			done = True
		if ENT == "backpack" or ENT == "bp":
			F.displayBP()
			BP_MENU = input("\nenter baubs for baub items\narmour for armour\nor stats to see your stats")
			if BP_MENU == "stats" or BP_MENU == "st":
				F.displayPS()
				F.EntCls()
			if BP_MENU == "baubs" or BP_MENU == "ba":
				F.display(V.baub_items)
				Decision = input("(to equip baub items enter equip)")
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
			V.Gold_Coin["amount"] += int(input("amount?"))
			F.item_to_container(V.Gold_Coin,V.backpack)
		if V.Debug == True and ENT == "/save game":
			print("NO")
			F.EntCls()
		F.cls()