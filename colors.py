#colored text shortcuts    (Coded by Python for Foxes)

'''
how to use: first, before any other code, type "import colors"
then type "print(colors.(any option bellow) + "any text here" )"
Ex. print(colors.cyanfg+colors.blackbg+"Hello World!")
this will give you "Hello World!" with cyan text and a black background
'''

#clears the screen of any txt (if any background effect is active, it highlights the entire terminal/output)
def clear():
  print("\033[H\033[J", end="")

#text itself
blackfg='\033[30m' #black
redfg='\033[31m' #red
greenfg='\033[32m' #green
yellowfg='\033[33m' #yellow
bluefg='\033[34m' #blue
magentafg='\033[35m' #magenta/light purple
cyanfg='\033[36m' #cyan
whitefg='\033[37m' #white
rstfg='\033[39m' #reset

#text background/highlighter effect
blackbg='\033[40m' #black
redbg='\033[41m' #red
greenbg='\033[42m' #green
yellowbg='\033[43m' #yellow
bluebg='\033[44m' #blue
magentabg='\033[45m' #magenta/light purple
cyanbg='\033[46m' #cyan
whitebg='\033[47m' #white
rstbg='\033[49m' #reset

#text style
bld='\033[1m' #bold/bright
thn='\033[2m' #thin/dim
nor='\033[22m' #normal
rstal='\033[0m' #reset all (even colors)
