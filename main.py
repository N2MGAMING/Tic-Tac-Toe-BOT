from random import choice
from time import sleep

class Bot(self):# BOT Class
	def play(self, coor, allowed, turn):
		
		n = True # n variable to see if the Bot played according to the condition Table
		
		# Start of the condition table
		test1 = (coor["A1"]==coor["A2"]!="[ ]" or coor["A2"]==coor["A3"]!="[ ]" or coor["A1"]==coor["A3"]!="[ ]") and turn>1 
		test2 = (coor["B1"]==coor["B2"]!="[ ]" or coor["B2"]==coor["B3"]!="[ ]" or coor["B1"]==coor["B3"]!="[ ]") and turn>1
		test3 = (coor["C1"]==coor["C2"]!="[ ]" or coor["C2"]==coor["C3"]!="[ ]" or coor["C1"]==coor["C3"]!="[ ]") and turn>1
		test4 = (coor["A1"]==coor["B1"]!="[ ]" or coor["B1"]==coor["C1"]!="[ ]" or coor["A1"]==coor["C1"]!="[ ]") and turn>1
		test5 = (coor["A2"]==coor["B2"]!="[ ]" or coor["B2"]==coor["C2"]!="[ ]" or coor["A2"]==coor["C2"]!="[ ]") and turn>1
		test6 = (coor["A3"]==coor["B3"]!="[ ]" or coor["B3"]==coor["C3"]!="[ ]" or coor["A3"]==coor["C3"]!="[ ]") and turn>1
		test7 = (coor["A1"]==coor["B2"]!="[ ]" or coor["B2"]==coor["C3"]!="[ ]" or coor["A1"]==coor["C3"]!="[ ]") and turn>1
		test8 = (coor["A3"]==coor["B2"]!="[ ]" or coor["B2"]==coor["C1"]!="[ ]" or coor["A3"]==coor["C1"]!="[ ]") and turn>1
		P2 = ""
		
		# Studying Player 1 moves and reply with the best action
		if (coor["A2"]=="[x]" or coor["C2"]=="[x]" or coor["B1"]=="[x]" or coor["B3"]=="[x]") and turn==1:
			while P2 not in allowed:
				P2 = choice(["A1", "C1", "B2", "B3"])
				n = False
		
		if coor["B2"]=="[x]" and turn==1:
			while P2 not in allowed:
				P2 = choice(["A1", "C1", "A3", "C3"])
				n = False
		
		if (coor["A1"]=="[x]" or coor["A3"]=="[x]" or coor["C1"]=="[x]" or coor["C3"]=="[x]") and turn==1:
			while P2 not in allowed:
				P2 = "B2"
				n = False
		
		if test1==True:
			possibilities = ["A1", "A2", "A3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test2==True:
			possibilities = ["B1", "B2", "B3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test3==True:
			possibilities = ["C1", "C2", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test4==True:
			possibilities = ["A1", "B1", "C1"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test5==True:
			possibilities = ["A2", "B2", "C2"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test6==True:
			possibilities = ["A3", "B3", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test7==True:
			possibilities = ["A1", "B2", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test8==True:
			possibilities = ["A3", "B2", "C1"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		# Searching the possibility of winning
		if test1==True and (coor["A1"]=="[o]" or coor["A2"]=="[o]" or coor["A3"]=="[o]"):
			possibilities = ["A1", "A2", "A3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test2==True and (coor["B1"]=="[o]" or coor["B2"]=="[o]" or coor["B3"]=="[o]"):
			possibilities = ["B1", "B2", "B3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test3==True and (coor["C1"]=="[o]" or coor["C2"]=="[o]" or coor["C3"]=="[o]"):
			possibilities = ["C1", "C2", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test4==True and (coor["A1"]=="[o]" or coor["B1"]=="[o]" or coor["C1"]=="[o]"):
			possibilities = ["A1", "B1", "C1"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test5==True and (coor["A2"]=="[o]" or coor["B2"]=="[o]" or coor["C2"]=="[o]"):
			possibilities = ["A2", "B2", "C2"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test6==True and (coor["A3"]=="[o]" or coor["B3"]=="[o]" or coor["C3"]=="[o]"):
			possibilities = ["A3", "B3", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test7==True and (coor["A1"]=="[o]" or coor["B2"]=="[o]" or coor["C3"]=="[o]"):
			possibilities = ["A1", "B2", "C3"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False
		
		if test8==True and (coor["A3"]=="[o]" or coor["B2"]=="[o]" or coor["C1"]=="[o]"):
			possibilities = ["A3", "B2", "C1"]
			for i in possibilities:
				if i in allowed:
					P2 = i
					n = False


		if n==True:
			P2 = choice(allowed)
		# End of the table condition
		return P2

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
	P2 = Bot.play(coor, allowed, turn)
	allowed.remove(P2)
	
	coor[P2] = coor[P2].replace(" ", "o")
	print('Turn {}:'.format(turn)+"\n   (1)(2)(3)"+"\n(A)"+coor["A1"]+coor["A2"]+coor["A3"]+"\n(B)"+coor["B1"]+coor["B2"]+coor["B3"]+"\n(C)"+coor["C1"]+coor["C2"]+coor["C3"]+"\n")	
	
	settings = verify(coor, running, end)
	running = settings[0]
	end = settings[1]
	if end == True:
		break

	turn += 1
