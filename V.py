# VARIABLES
import random
# validation for yes and no variables
Y,N = ["yes","y","fuck yes"],["no","n","fuck off","3"]
# validation for 1 to 4 options
op1,op2,op3,op4 = ["1","one"],["2","two"],["3","three"],["4","four"]
# debug mode, running for the regular game mode, continue variable, CP counter
Debug,running,cont,CPC = False,True,False,0
# nothing 
n = {"name":"nothing"}
#moon colour effect and general
mooncolour = ["blue","white","RED"]
mooneffect = ["(the elements that consist of ice and water seem powerfull tonight)","(just a normal night)","(EVIL THRIVES TONIGHT)"]
moon = ["mooncolour","mooneffect"]
#secrets (probably will remove)
if random.randint(1,100) == 100:
	the_big_variable = "something to do"
else:
	the_big_variable = "*and that other shit you mortals need to stay alive...*"
#player stats
backpack = [n,n,n,n,n,n,n,n,n,n] #backpack and slots
Phealth = 20 # player health
Defence = 0 # defence points
#mainhand
mainhand = n # mainhand

#items
Gold_Coin = {"name":"Gold coin","amount":0,"lore":"can be used as a currency in some societys"}

oakstick = {"name":"oak stick","damage":1,"durability":25}

flintstone = {"name":"flint stone","damage":10,"durability":0}

small_pebbles = {"name":"small pebbles","damage":2,"durability":0}

Delta_Rune = {"name":"Delta Rune","effect":"revive once in battle","damage":0,"durability":1,"lore":"seems to be eminating a powerful aura... you are filled with determination","tag":"powerstone"}

TurtleShell = {"name":"turtle shell","effect":"lightweight: III\nhard: III","durability":15,"defence":15,"lore":"an empty turtle shell... seems like it fits you","tag":"chestplate"}

iron_boots = {"name":"iron boots","effect":"heavy: I\nmalluable: II\nstrong: III","durability":25,"defence":20,"lore":"just some iron boots","tag":"boots"}
#items

# player slots

# baubs: name,effect,durability,damage,lore            watch item is for pimp/rapper joke
ring = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"ring"}
chain = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"chain"}
watch = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"watch"}
power_stone = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"powerstone"}
baub_items = [ring,chain,watch,power_stone]

# armour: name,effect,durability,defense,lore
helm = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"helmet"}
chestplate = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"chestplate"}
leggings = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"leggings"}
boots = {"name":"nothing","effect":"","durability":0,"damage":0,"lore":"","tag":"boots"}
ArmourSlots = [helm,chestplate,leggings,boots]

# player slots
#player stats
Player_Stats = [Phealth,Defence,backpack,baub_items,ArmourSlots,mainhand]
#player stats


#WIP
#pstattest = open("Player stats",'x')
#print(pstattest)