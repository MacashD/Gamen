# MAIN FILE
#imports all the files
import V,F,menu,CP1,CP2,CP3,CP4,CP5,CP6,CP7,CP8,CP9,CP10

#runs the next "CP" or checkpoint in order
def run(CPC): 
	CP_S = [CP1,CP2,CP3,CP4,CP5,CP6,CP7,CP8,CP9,CP10] #CP's are ordered in the array cps
	if CPC > len(CP_S): #if the "CPC" or CP counter is larger than the amount of cps it will end
		input("end of cps\nEnter to continue") #i will add something at the end of the cps
	else: #otherwise if there is another CP to run
		CP_S[CPC-1].CPMAIN() #it will choose the cp based on the CPC and run the CP's main function
		V.cont = False #continue is false as it has done one CP

#splash text
F.splash()

#debug mode
Decision = input("\nthis is a txt based adventure game thing\nversion 0.0.1\nOOF, enter to continue") #determines debug state
if Decision == "DEBUG": #user should enter DEBUG to enter debug mode
	F.cls() #referenced in the F folder
	V.Debug = True 
	input("debug mode activated")

#decision for gamemode
F.cls()
Q = "what gamemode do you wanna play\n \nregular or\nweeb mode or\nmemay mode" # selects a gamemode
options = R,W,M = ["regular","r"],["weeb","weebmode","w"],["meme","mememode","m"]
Foutput = ["R","WEEB","XTREEM MEME"]
GM = F.Fdecision(Q,options,Foutput)
F.cls()

#regular gamemode
if GM == "R": # if regular game mode is chosen this will run 
	while V.running == True: # game loop
		if V.cont == True: # if continue is chosen it will
			F.cls() # clear the screen
			V.CPC += 1 # increment the CPC
			run(V.CPC) # run the CP
		F.cls() #clear the screen if nothing is entered
		menu.bpmenu(True) #displays menu

# maybe later
elif GM == "WEEB":
	print("add weeb version here")
	print("add owo stuff l = w and r = w")
elif GM == "XTREEM MEME":
	print("extreem memer version here") 
# maybe later

# OTHER:

# functions are explained in the F folder
# F.function calls a function from the functions File
# V.variable uses a variable from the variables File
# menu.bpmenu(True/False) shows a menu where you can see the backpack and other stats, if true then the menu will act like it is in the main menu (not in a CP) if false it will show the menu but should be used in CP's to access the backpack or to equip armour etc