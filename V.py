import random
Y,N,Debug = ["yes","y","fuck yes"],["no","n","fuck off","3"],False
op1,op2,op3,op4 = ["1","one"],["2","two"],["3","three"],["4","four"]
running,cont,ENT,Decision,CP = True,False,0,0,0
n = {"name":"nothing"}
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
Gold_Coin = {
	"name":"Gold coin",
	"amount":0,
	"lore":"can be used as a currency in some societys"
}
oakstick = {"name":"oak stick","damage":1,"durability":25}
flintstone = {"name":"flint stone","damage":10,"durability":0}
small_pebbles = {"name":"small pebbles","damage":2,"durability":0}
Delta_Rune = {"name":"Delta Rune","effect":"revive once in battle","damage":0,"durability":1,"lore":"seems to be eminating a powerful aura... you are filled with determination","tag":"powerstone"}
TurtleShell = {
	"name":"turtle shell",
	"effect":"lightweight: III\nhard: III",
	"durability":15,
	"defence":15,
	"lore":"an empty turtle shell... seems like it fits you",
	"tag":"chestplate"
}
iron_boots = {
	"name":"iron boots",
	"effect":"heavy: I\nmalluable: II\nstrong: III",
	"durability":25,
	"defence":20,
	"lore":"just some iron boots",
	"tag":"boots"
}
#delta rune is a power_stone
# baubs: name,effect,durability,damage,lore            watch item is for pimp/rapper joke
ring = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"ring"}
chain = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"chain"}
watch = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"watch"}
power_stone = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"powerstone"}
# armour: name,effect,durability,defense,lore
helm = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"helmet"}
chestplate = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"chestplate"}
leggings = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"leggings"}
boots = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"boots"}
ArmourSlots = [helm,chestplate,leggings,boots]
backpack = [n,n,n,n,n,n,n,n,n,n]
baub_items = [ring,chain,watch,power_stone]
#player stats
#pstattest = open("Player stats",'x')
#print(pstattest)
Player_Stats = [Phealth,Defence,backpack,baub_items,mainhand]