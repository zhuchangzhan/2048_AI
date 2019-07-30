import sys
import numpy as np
import argparse


class chessBoard():

	def __init__(self,size):
		self.width = size
		self.height = size
		self.score = 0

		self.board = np.zeros(16)

		while True:
			state = self.game_start()
			if state == False:
				break
			while True:
				val = input("WASD?: ")
				if val == "W" or val == "w":
					self.move_up()
					break
				elif val == "A" or val == "a":
					self.move_left()
					break
				elif val == "S" or val == "s":
					self.move_down()
					break
				elif val == "D" or val == "d":
					self.move_right()
					break
				elif val == "Q" or val == "q":
					return
				else:
					print("unknown input, Q to quit")
				print("step")


	def game_start(self):

		iteration = np.random.choice([1,2])
		
		for i in range(iteration):
			zero_location = np.where(self.board == 0)[0]
			location = np.random.choice(zero_location)
			value = np.random.choice([2,4])
			self.board[location] = value

		not_filled = self.board[self.board == 0]
		print("*"*20)
		print(self.board.reshape(4,4))
		if list(not_filled) == []:
			print("You Lost, total score = %s"%self.score)
			return False
		return True

	def move_left(self):
		board = self.board.reshape(4,4)

		new_board = np.zeros(16)
		for j,row in enumerate(board):
			nonzero_location = row[row!=0]
			rowlen = len(nonzero_location)
			new_row = np.zeros(4)
			if rowlen == 0:
				pass
			elif rowlen == 1:
				new_row[0] = nonzero_location[0]
			else:
				for i in range(rowlen-1):
					if nonzero_location[i] == nonzero_location[i+1]:
						new_row[i] = 2*nonzero_location[i]
						new_row[i+1] = 0
					else:
						new_row[i] = nonzero_location[i]
						new_row[i+1] = nonzero_location[i+1]




			new_board[j*4:(j+1)*4] = new_row

		self.board = new_board
		#print(new_board.reshape(4,4))

	def move_right(self):
		self.move_left()
		board = self.board.reshape(4,4)
		new_board = np.zeros(16)
		for j,row in enumerate(board):
			nonzero_location = row[row!=0]
			rowlen = len(nonzero_location)
			new_row = np.concatenate([np.zeros(4-rowlen),nonzero_location])
			new_board[j*4:(j+1)*4] = new_row
		self.board = new_board


	def move_up(self):
		
		self.board = self.board.reshape(4,4).T.reshape(-1)
		self.move_left()
		self.board = self.board.reshape(4,4).T.reshape(-1)

	def move_down(self):
		self.board = self.board.reshape(4,4).T.reshape(-1)
		self.move_right()
		self.board = self.board.reshape(4,4).T.reshape(-1)





if __name__ == "__main__":
	gameboard = chessBoard(4)
