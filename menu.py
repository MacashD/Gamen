import time,random,V,F
def bpmenu():
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
		F.EntCls()