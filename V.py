import random
Y,N,Debug,FH = ["yes","y","fuck yes"],["no","n","fuck off","3"],False,False
op1,op2,op3,op4 = ["1","one"],["2","two"],["3","three"],["4","four"]
running,cont,ENT,Decision,CP = True,False,0,0,0
n = ["nothing"]
mooncolour = ["blue","white","RED"]
mooneffect = ["(the elements that consist of ice and water seem powerfull tonight)","(just a normal night)","(EVIL THRIVES TONIGHT)"]
moon = ["mooncolour","mooneffect"]
#gamestuff
RI = random.randint(1,100)
if RI == 100:
	the_big_variable = "something to do"
else:
	the_big_variable = "*and that other shit you mortals need to stay alive...*"
Phealth = 20
Defence = 0
#mainhand
mainhand = n
#items
Gold_Coin = ["Gold coin",0,"can be used as a currency in some societys"]
# [name,damage,durability,]
oakstick = ["oak stick",1,25]
flintstone = ["flint stone",10,0]
small_pebbles = ["small pebbles",2,0]
Delta_Rune = ["Delta Rune","revive once in battle",0,1,"'seems to be eminating a powerful aura... you are filled with determination'","powerstone"]
TurtleShell = ["turtle shell","lightweight\nhard",15,15,"'an empty turtle shell... seems like it fits you'","chestplate"]
#delta rune is a power_stone
# baubs: name,effect,durability,damage,lore            watch item is for pimp/rapper joke
ring = ["nothing","",0,0,"","ring"]
chain = ["nothing","",0,0,"","chain"]
watch = ["nothing","",0,0,"","watch"]
power_stone = ["nothing","",0,0,"","powerstone"]
# armour: name,effect,durability,defense,lore
helm = ["nothing","",0,0,"","helmet"]
chestplate = ["nothing","",0,0,"","chestplate"]
leggings = ["nothing","",0,0,"","leggings"]
boots = ["nothing","",0,0,"","boots"]
ArmourSlots = [helm,chestplate,leggings,boots]
backpack = [n,n,n,n,n,n,n,n,n,n]
baub_items = [ring,chain,watch,power_stone]
#player stats
#pstattest = open("Player stats",'x')
#print(pstattest)
Player_Stats = [Phealth,Defence,backpack,baub_items,mainhand]