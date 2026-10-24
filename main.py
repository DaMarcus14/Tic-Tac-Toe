#Tic Tac Toe   (By Python for Foxes)
#there is just a lil bit of math, trust gng trust!



#=====================================================
#imports
import shutil as os #for looks really
import colors as c #dif colors for looks
import time as t #to make it look like the ai is thinking
import placement as p #some functions i like even more seperated
import winnerCheck as wc #see's who is the winner
#=====================================================



#=====================================================
#vars
tl=" " #top left
tm=" " #top middle
tr=" " #top right
ml=" " #middle left
mm=" " #middle middle
mr=" " #middle right
bl=" " #bottom left
bm=" " #bottom middle
br=" " #bottom right
tb="—————" #top barrier
bb="—————" #bottom barrier
theme="dark"
turn="X or O"
#=====================================================



#=====================================================
#lists
screensize=[]
screensize.append(os.get_terminal_size())
top=[tl,"|",tm,"|",tr] #top row
middle=[ml,"|",mm,"|",mr] #middle row
bottom=[bl,"|",bm,"|",br] #bottom row
hboard=[top,tb,middle,bb,bottom] #whole baord
alvSpaces=["TL","TM","TR","ML","MM","MR","BL","BM","BR"] #avaliable spaces
#=====================================================



#=====================================================
#screen size calcs
width=screensize[0].columns #width of terminal (in characters, not pixles!)
hight=screensize[0].lines #hight of terminal (again, in characters)
sfb=(int((width/2)-5)) #spaces for board
#=====================================================



#=====================================================
#functions
def prtb(): #Print the board
 for i in range(len(hboard)):
   print((" "*sfb),*hboard[i])
#=====================================================
def clear():
 c.clear()
 print((" "*(sfb-3)),"||===========||") #uses earlier calc to make logo centered
 print((" "*(sfb-4)),"|| Tic Tac Toe ||")
 print((" "*(sfb-3)),"||===========||")
#=====================================================
def themes(theme):
 theme=theme.lower()
 if(theme=="dark"): #if dark theme then white fg and black bg
   print(c.whitefg+c.blackbg)
 elif(theme=="light"): #if light theme then black fg and white bg
   print(c.blackfg+c.whitebg)
 elif(theme=="classic terminal"): #if classic terminal theme, then green fg and black bg
   print(c.blackbg+c.greenfg)
 else: #if invalid theme, then default to dark
   print(c.blackbg+c.whitefg)
   print("Unknown theme input: Fix: current theme (Dark)")
   input("Press enter to continue... ")
 clear()
#=====================================================
def turns():
 global turn
 if(turn=="X"):
   turn="O"
 else:
   turn="X"
#=====================================================



#=====================================================
#inizalization
print(c.blackbg+c.whitefg) #defaults to dark theme
clear()
print("Welcome to my first proper python game!")
print("While snake would be more fitting then tic tac toe, it's MUCH harder to code!")
print("So this will have to do...")
t.sleep(10)
clear()
print("Let the game begin!")
t.sleep(3)
clear()
print("I lied, we first need to do some customizations and setting changes.")
print("lets start with...")
print(c.redfg+"C"+c.greenfg+"O"+c.bluefg+"L"+c.yellowfg+"O"+c.cyanfg+"R"+c.magentafg+"!") #colorful text!
t.sleep(6)
print(c.rstfg)
clear()
print("Here are the current avaliable themes:")
print("Dark")
print("Light")
print("Classic Terminal")
theme=input("Which one do you want? ")
themes(theme)
print("Remember, you can go back to settings to change it back latter!")
t.sleep(3)
clear()
print("Now turn order. Before every game, you can choose if you or the bot goes first.")
print("But right now, you are choosing if X's or O's go first.")
turn=input('Type "X" or "O" ')
turn=turn.upper()
clear()
while(turn!="X" and turn!="O"): #only does its thing if they didn't type x or o
 print("You had a typo or just typed the wrong letter!")
 turn=input('Type "X" or "O" ')
 turn=turn.upper()
clear()
#=====================================================



#=====================================================
#game logic


#=====================================================



#=====================================================
#end program
input("Press enter to end program... ")
print(c.rstal)
c.clear()
#=====================================================
