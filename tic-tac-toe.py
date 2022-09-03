from random import choice, randint

board = [
	[" "," "," "],
	[" "," "," "],
	[" "," "," "]
]

sign1 = "X"
sign2 = "O"

player1 = input("Player 1: ")
player2 = input("Player 2: ")

first_move = True


def print_board():
	for row in board:
		print(row)
	print("")
	
def reset():
	first_move = True
	for row in range(3):
		for column in range(3):
			board[row][column] = " "
			
def win(board):
	#checking rows
	if board[0][0] == board[0][1] == board[0][2] !=  " " or board[1][0] == board[1][1] == board[1][2] != " " or board[2][0] == board[2][1] == board[2][2] != " ": 
		return True
	
	#checking columns
	elif board[0][0] == board[1][0] == board[2][0] != " " or board[0][1] == board[1][1] == board[2][1] != " " or board[0][2] == board[1][2] == board[2][2] != " ":
		return True
		
	#checking diagonals
	elif board[0][0]  == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
		return True
		
	else:
		return False
		
def continue_(continue_input):
	while continue_input.lower() not in ("y","n"):
		print("Wrong option, try again\n")
		continue_input =  input("Continue(Y/N)?:")
		
	if continue_input.lower() == "y":
		return True
	elif continue_input.lower() == "n":			
		return False
		
def full_board(board):
	draw = 0
	for row in board:
		for item in row:
			if item == " ":
				draw +=1
	
	if draw == 0:
		draw= 0
		return True
		
def bot(sign):
	global done
	#checking rows
	for row in range(3):
		if board[row][0] == board[row][1] == sign or board[row][1] == board[row][2] == sign or board[row][0] == board[row][2] == sign:
					for i in range(3):
						if board[row][i] == " " and done == 0:
							board[row][i] = sign1
							done += 1
					
	# checking columns
	for col in range(3):
		if board[0][col] == board[1][col] == sign  or board[1][col] == board[2][col] == sign or board[0][col] == board[2][col] == sign:
					for i in range(3):
						if board[i][col] == " " and done == 0:
							board[i][col] = sign1
							done += 1
						
	#checking diagonal
	if board[0][0] == board[1][1] == sign or board[1][1] == board[2][2] == sign or board[0][0] == board[2][2] == sign:
				for i in range(3):
					if board[i][i] == " " and done == 0:
						board[i][i] = sign1
						done += 1
						
	if board[0][2] == board[1][1] == sign or board[1][1] == board[2][0] == sign or board[0][2] == board[2][0] == sign:
				for i in range(3):
					if board[i][2-i] == " " and done == 0:
						board[i][2-i] = sign1
						done += 1
	
	
print_board()
while True:

	print("{} move".format(player1))
	
	#game with computer
	if player1.lower() == "pc":
		done = 0
		
		while True:
			#checking fow win
			bot(sign1)
			#checking for block
			bot(sign2)
			
			if done == 0:
				if first_move:
					first_move == False
					while True:
						row = choice((0,2))
						column = choice((0,2))
						if board[row][column] == " ":
							board[row][column] = sign1
							break
						
				else:
					while True:
						row = randint(0,2)
						column = randint(0,2)
						if board[row][column] == " ":
							board[row][column] = sign1
							break
				break
					
			else:
					break
					
			
	else:
		while True:
			while True:
				row= input("Row: ")
				if row in ["1","2","3"]:
					break
				else:
					print("Wrong position, try again\n")
				
			while True:
				column = input("Column:")
				if column in ["1","2","3"]:
					break
				else:
					print("Wrong position, try again\n")
				
			if board[int(row)-1][int(column)-1] == " ":
				board[int(row)-1][int(column)-1] = sign1
				break
			else:
				print("Choose different tile\n")
	
	print_board()
	
	if win(board) == True or full_board(board) == True:
		move  = 0
		if win(board) == True:
			print("\n{} win!\n".format(player1))
		else:
			print("\nDraw\n")
		
		continue_input =  input("Continue(Y/N)?:")
		if continue_(continue_input) == True:
			reset()
			print_board()
		else:
			break
			
	#changing players and signs
	sign1, sign2 = sign2, sign1
	player1, player2 = player2, player1