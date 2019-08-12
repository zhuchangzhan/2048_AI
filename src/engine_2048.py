"""

rewrite the 100-line 2048 so that it's more ai friendly.
I fell victim to my own preaching: premature optimization if root of all evil.

"""
import sys
import numpy as np

class chessBoard():

	def __init__(self,board=[]):

		self.board = board if board !=[] else np.zeros(16)
		self.update_gameboard()
		while True:
			old_board = self.board.copy()
			output = self.user_input(player) 
			if (self.board == old_board).all() and output == None:
				print("No merge happened",self.val)
				self.previous_move = False
				continue
			self.previous_move = True
			if self.update_gameboard():
				print("You Lost, total score = %s"%np.sum(self.board))
				break

	def user_input(self,player):

		self.val = input("WASD?: ") if player == "Human" else self.AI.decision(self.previous_move)
		if self.val == "W" or self.val == "w":
			self.move_up()
		elif self.val == "A" or self.val == "a":
			self.move_left()
		elif self.val == "S" or self.val == "s":
			self.move_down()
		elif self.val == "D" or self.val == "d":
			self.move_right()
		elif self.val == "Q" or self.val == "q":
			print("Quit Game")
			sys.exit()
		elif self.val == "C" or self.val == "c":
			return "C"
		else:
			print("Unknown input, Q to quit")
			return self.user_input(player) if player == "Human" else sys.exit() 

	def update_gameboard(self):

		count_zero = len(self.board[self.board == 0])
		print(count_zero)
		if count_zero > 0:
			iteration = count_zero if count_zero == 1 else np.random.choice([1,1,2])
			for _ in range(iteration):
				zero_location = np.random.choice(np.where(self.board == 0)[0])
				self.board[zero_location] = np.random.choice([2,4])
			print("*"*20)
			print(np.array(self.board,dtype="int").reshape(4,4))
			return False
		else:
			print("*"*40)
			print(np.array(self.board,dtype="int").reshape(4,4))
			for row in self.board.reshape(4,4):
				for i in range(4-1):
					if row[i] == row[i+1]:
						return False
			for row in self.board.reshape(4,4).T:
				for i in range(4-1):
					if row[i] == row[i+1]:
						return False
			return True

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

	def move_left(self):
		for i,row in enumerate(self.board.reshape(4,4)):
			self.board[i*4:(i+1)*4] = self.merge_row(row,"left")

	def move_right(self):
		for i,row in enumerate(self.board.reshape(4,4)):
			self.board[i*4:(i+1)*4] = self.merge_row(row,"right")
		
	def move_up(self):
		self.board = self.board.reshape(4,4).T.reshape(-1)
		self.move_left()
		self.board = self.board.reshape(4,4).T.reshape(-1)

	def move_down(self):
		self.board = self.board.reshape(4,4).T.reshape(-1)
		self.move_right()
		self.board = self.board.reshape(4,4).T.reshape(-1)






