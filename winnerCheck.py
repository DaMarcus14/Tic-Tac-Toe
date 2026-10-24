#This only has the function to check the winner
#there are 8 dif ways to win
def winc():
  #setup
  global tl,tm,tr,ml,mm,mr,bl,bm,br
 
  #Checks if any of the 
  if(tl==tm==tr): #1
    print(f"Winner is {tl}'s!")
  elif(ml==mm==mr): #2
    print(f"Winner is {ml}'s!")
  elif(bl==bm==br): #3
    print(f"Winner is {bl}'s!")
  elif(tl==ml==bl):#4
    print(f"Winner is {tl}'s!")
  elif(tm==mm==bm): #5
    print(f"Winner is {tm}'s!")
  elif(tr==mr==br): #6
    print(f"Winner is {tr}'s!")
  elif(tl==mm==br): #7
    print(f"Winner is {tl}'s!")
  elif(bl==mm==tr): #8
    print(f"Winner is {bl}'s!")

  #if none is satisfied, no one won yet
  else:
    tl=tl
