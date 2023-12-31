from random import choice

class Bot():# BOT Class
	def play(coor, allowed, turn):
		
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

