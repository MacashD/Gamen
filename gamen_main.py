import V,F,menu,CP1,CP2
Decision = input("this is a txt based adventure game thing\nversion 0.0.2\nOOF, enter to continue")
if Decision == "DEBUG":
	F.cls()
	V.Debug = True
	input("debug mode activated")
F.cls()
Q = "what gamemode do you wanna play\n \nregular or\nweeb mode or\nmemay mode"
options = R,W,M = ["regular","r"],["weeb","weebmode","w"],["meme","mememode","m"]
Foutput = ["R","WEEB","XTREEM MEME"]
GM = F.Fdecision(Q,options,Foutput)
F.cls()
if GM == "R":
	while V.running == True:
		if V.cont == True:
			V.cont = False
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
		F.cls()
		menu.bpmenu(True)
elif GM == "WEEB":
	print("add weeb version here")
	print("add owo stuff l = w and r = w")
elif GM == "XTREEM MEME":
	print("extreem memer version here")