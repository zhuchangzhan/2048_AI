"""

rewrite the 100-line 2048 so that it's more ai friendly.
I fell victim to my own preaching: premature optimization if root of all evil.

"""
import sys
import numpy as np

class chessBoard():

	def __init__(self):
		pass
 
	def place_random(self,board):

		count_zero = len(board[board == 0])
		if count_zero > 0:
			iteration = count_zero if count_zero == 1 else np.random.choice([1,1,2])
			for _ in range(iteration):
				zero_location = np.random.choice(np.where(board == 0)[0])
				board[zero_location] = np.random.choice([2,4])
			return board,False
		else: # evaluate if the game is lost
			for row in board.reshape(4,4):
				for i in range(4-1):
					if row[i] == row[i+1]:
						return board,False
			for row in board.reshape(4,4).T:
				for i in range(4-1):
					if row[i] == row[i+1]:
						return board,False
			return board,True

	def update_gameboard(self,board,decision):

		if decision == "W":
			return self.move_up(board)
		elif decision == "A":
			return self.move_left(board)
		elif decision == "S":
			return self.move_down(board)
		elif decision == "D":
			return self.move_right(board)
		else:
			print("Unknown input, Q to quit")
			sys.exit() 


	def merge_row(self,row,direction="left"):

		nonzero_item   = row[np.nonzero(row)[0]]
		if direction == "right":
			nonzero_item = nonzero_item[::-1]

		new_row = np.zeros(4)
		for i in range(len(nonzero_item)):
			new_row[i] = nonzero_item[i]
			if i>=len(nonzero_item)-1:
				break
			if nonzero_item[i] == nonzero_item[i+1] and nonzero_item[i] != 0:
				new_row[i] = nonzero_item[i]*2
				nonzero_item[i+1] = 0

		if direction == "right":
			new_row = new_row[::-1]
		if len(np.nonzero(row)[0]) == len(np.nonzero(new_row)[0]):
			return new_row
		else:
			return self.merge_row(new_row,direction)

	def move_left(self,board):
		for i,row in enumerate(board.reshape(4,4)):
			board[i*4:(i+1)*4] = self.merge_row(row,"left")
		return board

	def move_right(self,board):
		for i,row in enumerate(board.reshape(4,4)):
			board[i*4:(i+1)*4] = self.merge_row(row,"right")
		return board

	def move_up(self,board):
		board = board.reshape(4,4).T.reshape(-1)
		board = self.move_left(board)
		board = board.reshape(4,4).T.reshape(-1)
		return board

	def move_down(self,board):
		board = board.reshape(4,4).T.reshape(-1)
		board = self.move_right(board)
		board = board.reshape(4,4).T.reshape(-1)
		return board





