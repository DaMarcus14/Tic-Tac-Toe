#This is just here so the whole locating where to place what is not in main and clauge it up
def pos(location,turn):
 #setup
 location=location.upper()
 global hboard
  #row of board
 if(location[0]=="T"):
   fir=0
 elif(location[0]=="M"):
   fir=2
 else: #if(location[0]=="B"):
   fir=4
  #column of board
 if(location[1]=="L"):
   sec=0
 elif(location[1]=="M"):
   sec=2
 else: #if(location[1]=="R"):
   sec=4


 #Placing thing on board
 hboard[fir][sec]=turn
