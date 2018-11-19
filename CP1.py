import time
import random
import V
import F
def CPONE():
	if V.Debug == True:
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
		for x in range(0,len(V.backpack)):
			if V.backpack[x] == V.oakstick:
				V.oakstick = ["oak stick",1.25,35]
				V.backpack[x] = V.n
				F.item_to_backpack(V.oakstick,V.backpack)
				print("your oak stick gained 0.25 damage and 10 durability",V.oakstick)
				F.EntCls()
		if V.backpack[0] != V.oakstick:
			print("oh you dont have a stick, sorry thought you did")
			time.sleep(7)
			print("well bye")
			time.sleep(0.5)
			F.EntCls()
	CP_1_VillageReward_s = random.randint(250,750)
	#personal messages
	if V.FH == True:
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
		F.EntCls()
	#personal messages
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
		V.Gold_Coin[1] = V.Gold_Coin[1] + CP_1_VillageReward_s
		F.item_to_backpack(V.Gold_Coin,V.backpack)
		#remember this optional bit needs to flow with the rest of the game
	else:
		F.cls()
		print("(you declined the quest)")
		F.EntCls()
	print("you continue on, walking down the path")
	time.sleep(1)
	print("the sun slowly decending beneath the horison")
	time.sleep(3)
	print("the journey seems long and you are running low on food, water and",V.the_big_variable," but you know that something will come up")
	time.sleep(2)
	print("sadly you havent found anything and its dark and you will probably be fucked if you stay out in the dark for too long")
	time.sleep(1)
	print("so i would suggest to find a place to settle down")
	time.sleep(1)
	Q = "options:\n1 for: the ground\n2 for: a bare tree\n3 for: dont"
	ground,TreeByRoad = ["ground","g","1"],["tree","t","the fucking tree","2"]
	options = [ground,TreeByRoad,V.N]
	Foutput = ["ground","tree","no"]
	Decision = F.Fdecision(Q,options,Foutput)
	F.cls()
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
		F.EntCls()
		#continue
	V.CP = 2