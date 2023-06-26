from random import choice
from time import sleep
from bot import *

def verify(coor, running, end): # Function to verify if someone won
	test1 = coor["A1"]==coor["A2"] and coor["A2"]==coor["A3"] and coor["A3"]!="[ ]"
	test2 = coor["B1"]==coor["B2"] and coor["B2"]==coor["B3"] and coor["B3"]!="[ ]"
	test3 = coor["C1"]==coor["C2"] and coor["C2"]==coor["C3"] and coor["C3"]!="[ ]"
	test4 = coor["A1"]==coor["B1"] and coor["B1"]==coor["C1"] and coor["C1"]!="[ ]"
	test5 = coor["A2"]==coor["B2"] and coor["B2"]==coor["C2"] and coor["C2"]!="[ ]"
	test6 = coor["A3"]==coor["B3"] and coor["B3"]==coor["C3"] and coor["C3"]!="[ ]"
	test7 = coor["A1"]==coor["B2"] and coor["B2"]==coor["C3"] and coor["C3"]!="[ ]"
	test8 = coor["A3"]==coor["B2"] and coor["B2"]==coor["C1"] and coor["C1"]!="[ ]"
	if test1==True and coor["A1"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test1==True and coor["A1"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test2==True and coor["B1"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test2==True and coor["B1"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test3==True and coor["C1"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test3==True and coor["C1"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test4==True and coor["A1"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test4==True and coor["A1"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test5==True and coor["A2"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test5==True and coor["A2"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test6==True and coor["A3"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test6==True and coor["A3"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test7==True and coor["A1"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test7==True and coor["A1"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if test8==True and coor["A3"]=="[x]" and end==False:
		print("P1 wins !!!")
		running = False
		end = True
	if test8==True and coor["A3"]=="[o]" and end==False:
		print("P2 wins !!!")
		running = False
		end = True
	if allowed==[]:
		print("Equal !!!")
		running = False
		end = True
	return (running, end)

print("Welcome to XO game !!!\nYou are X")
running = True
end = False
turn = 1
letters = ["A", "B", "C"]
empty = "[ ]"
coor = {
"A1":empty,
"A2":empty,
"A3":empty,
"B1":empty,
"B2":empty,
"B3":empty,
"C1":empty,
"C2":empty,
"C3":empty
}
allowed = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
P1, P2 = "", ""

print('Turn {}:'.format(turn)+"\n   (1)(2)(3)"+"\n(A)"+coor["A1"]+coor["A2"]+coor["A3"]+"\n(B)"+coor["B1"]+coor["B2"]+coor["B3"]+"\n(C)"+coor["C1"]+coor["C2"]+coor["C3"]+"\n")	

while running:
	P1 = input("----------------------------------------\nPlayer 1 : ")
	while P1 not in allowed:
		print("Wrong Value !!!")
		P1 = input("Player 1 : ")
	allowed.remove(P1)
	
	coor[P1] = coor[P1].replace(" ", "x")
	print('Turn {}:'.format(turn)+"\n   (1)(2)(3)"+"\n(A)"+coor["A1"]+coor["A2"]+coor["A3"]+"\n(B)"+coor["B1"]+coor["B2"]+coor["B3"]+"\n(C)"+coor["C1"]+coor["C2"]+coor["C3"]+"\n")	

	settings = verify(coor, running, end)
	running = settings[0]
	end = settings[1]
	if end == True:
		break
	sleep(1)
	P2 = Bot.play(coor=coor, allowed=allowed, turn=turn)
	allowed.remove(P2)
	
	coor[P2] = coor[P2].replace(" ", "o")
	print('Turn {}:'.format(turn)+"\n   (1)(2)(3)"+"\n(A)"+coor["A1"]+coor["A2"]+coor["A3"]+"\n(B)"+coor["B1"]+coor["B2"]+coor["B3"]+"\n(C)"+coor["C1"]+coor["C2"]+coor["C3"]+"\n")	
	
	settings = verify(coor, running, end)
	running = settings[0]
	end = settings[1]
	if end == True:
		break

	turn += 1
