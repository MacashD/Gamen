import time,random,menu,V,F
def CP1():
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
		input()
	F.cls()
#	menu.bpmenu(False) this adds menu
	F.night()
	RI = random.randint(1,25)
	if RI == 25 or V.Debug == True:
		print("event1: the big gae approaches")
		time.sleep(5)
		print("nah jk wouldnt be that mean to drop a b0ss battle on the first CP")
		time.sleep(2)
		F.Dots(3)
		print("here have an upgrade to your stick or something\n")
		if V.oakstick in V.backpack:
			V.oakstick = {"name":"oak stick","damage":1.25,"durability":35}
			V.backpack[0] = V.n
			F.item_to_backpack(V.oakstick,V.backpack)
			print("your oak stick gained 0.25 damage and 10 durability\n",V.oakstick["name"],V.oakstick["damage"],V.oakstick["durability"])
			F.EntCls()
		else:
			print("oh you dont have a stick, sorry thought you did")
			time.sleep(7)
			print("well bye")
			time.sleep(0.5)
			F.EntCls()
	CP_1_VillageReward_s = random.randint(250,750)
	dragon_quest_info = ["_st_ \ndragon or some shit fucked everything \nreward:",CP_1_VillageReward_s,"Gold \nplz help or someshit \n(it seems like in this village they speak english normaly apart from replacing something with someshit)"]
	print(dragon_quest_info[0],dragon_quest_info[1],dragon_quest_info[2])
	options = [V.Y,V.N]
	Foutput = ["yes","no"]
	Q="y / n"
	Decision = F.Fdecision(Q,options,Foutput)
	if Decision == "yes":
		F.cls()
		print("(you accepted the quest)")
		print("dshit")
		F.EntCls()
		V.Gold_Coin["amount"] += CP_1_VillageReward_s
		F.item_to_backpack(V.Gold_Coin,V.backpack)
		#remember this optional bit needs to flow with the rest of the game
	else:
		F.cls()
		print("(you declined the quest)")
		F.EntCls()
	print("you continue on, walking down the path")
	#time.sleep(1)
	print("the sun slowly descending beneath the horizon")
	#time.sleep(3)
	print("the journey seems long and you are running low on food, water and",V.the_big_variable," but you know that something will come up")
	#time.sleep(2)
	print("sadly you havent found anything and its dark and you will probably be fucked if you stay out in the dark for too long")
	#time.sleep(1)
	print("so i would suggest to find a place to settle down")
	#time.sleep(1)
	whyyy = ""
	Q = "options:\n1 for: the ground\n2 for: a bare tree\n3 for: dont"
	ground,TreeByRoad = ["ground","g","1"],["tree","t","the fucking tree","2"]
	options,Foutput = [ground,TreeByRoad,V.N],["ground","tree","no"]
	Decision = F.Fdecision(Q,options,Foutput)
	F.cls()
	if Decision == "ground":
		print("(you decided to sleep on the ground\nthe ground became warmer)")
		time.sleep(2)
		F.Dots(5)
		print("(you took a shit...)\n")
		whyyy = "s"
		time.sleep(3)
		print("(you disgusting human)")
		F.EntCls()
	elif Decision == "tree":
		print("(you decided to sleep in the tree\nit is prickely as there are no leaves\nyou sleep through the night nonetheless)\n*-1hp*")
		V.Player_Stats[0] -= 1
		F.EntCls()
	elif Decision == "no":
		print("(you decided not to sleep,\n seconds later you hear a distant voice saying,\n sleep is for the weak)")
		time.sleep(2)
		F.Dots(3)
		print("(it sounds like it came from very far away so you decide to ignore it)")
		F.EntCls()
		print("you continue on in the dark\nthe moon looks",V.moon[0],V.moon[1])
		F.EntCls()
		RI = random.randint(1,4)
		if V.moon[0] == "RED" or RI != 4:
			print("a red and black striped gremlin came out and attacked!")
			time.sleep(1)
			print("attack sequence")
			F.EntCls()
		else:
			print("unexpectedly you were undisterbed through the knight")
			time.sleep(2)
			print("how lucky")
			F.EntCls()
	print("you press on and find a castle\nits walls are made from stone bricks and the wooden gate infront of you seems impossible to break with what you have")
	F.EntCls()
	Q="what do you wanna do?"
	V.op1,V.op2,V.op3,V.op4 = ["knock","k"],["nothing","n","i dont fucking know","idk"],["something","s"],["piss on the door","piss"]
	options = [V.op1,V.op2,V.op3,V.op4]
	Foutput = ["knock","n","s","piss"]
	Decision = F.Fdecision(Q,options,Foutput)
	if Decision == "piss":
		print("you piss on th\n")
		time.sleep(1)
		print("wait what\n")
		time.sleep(4)
		print("wtf is wrong with you\n")
		if whyyy == "s":
			time.sleep(3)
			print("first the shit and now you...\n")
			time.sleep(7)
			print("there is a toilet anywhere but on the fucking road or the door\n")
			time.sleep(7)
			print("why tho\n")
			time.sleep(3)
			print("ffs\n")
			F.EntCls()
		else:
			time.sleep(1)
			print("fgs this is not like you\n")
			time.sleep(2)
			print("well lets just move on\n")
			F.EntCls()
	if Decision == "knock":
		print("a guard answers your knock by opening the door\n")
	if Decision == "n" or Decision == "s":
		print("a guard opens the door\n")
		time.sleep(2)
		print("seems like they have an open door policy\n")
	time.sleep(2)
	print("guard: why are you here")
	if Decision == "piss":
		print("\nguard: oh you little bitch\nguard: ill have you killed for defileing the kingdom of my bosses bosses boss")
		time.sleep(3)
		print("guard: im pretty high up the ranks i swear")
	F.EntCls()