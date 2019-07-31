import sys
import numpy as np

class chessBoard():

	def __init__(self):
		self.score = 0
		self.board = np.zeros(16)
		while True:
			state = self.game_start()
			if state == False:
				print("You Lost, total score = %s"%self.score)
				break
			while True:
				if self.user_input():
					break

	def game_start(self):

		iteration = np.random.choice([1,1,2])
		for _ in range(iteration):
			zero_location = np.where(self.board == 0)[0]
			location = np.random.choice(zero_location)
			value = np.random.choice([2,4])
			self.board[location] = value

		print("*"*20)
		print(self.board.reshape(4,4))
		self.score = np.sum(self.board)
		if list(self.board[self.board == 0]) == []:
			for row in self.board.reshape(4,4):
				for i in range(4-1):
					if row[i] == row[i+1]:
						return True
			for row in self.board.reshape(4,4).T:
				for i in range(4-1):
					if row[i] == row[i+1]:
						return True
			return False
		return True

	def user_input(self):

		val = input("WASD?: ")
		if val == "W" or val == "w":
			self.move_up()
		elif val == "A" or val == "a":
			self.move_left()
		elif val == "S" or val == "s":
			self.move_down()
		elif val == "D" or val == "d":
			self.move_right()
		elif val == "Q" or val == "q":
			sys.exit()
		else:
			print("unknown input, Q to quit")
			return False
		return True

	def merge(self,length=4, x=[8,4,2,2]):

		new_list = np.zeros(4)
		nonzero_x = np.array(x)[np.nonzero(x)[0]]
		done = True
		for i in range(len(nonzero_x)):
			try:
				if nonzero_x[i] == nonzero_x[i+1] and done:
					done = False
					new_list[i] = nonzero_x[i]*2
					nonzero_x[i+1] = 0
				else:
					new_list[i] = nonzero_x[i]
			except:
				new_list[i] = nonzero_x[i]
		nonzero = len(np.nonzero(new_list)[0])
		if length == nonzero:
			return new_list
		else:
			return self.merge(nonzero, new_list)

	def move_left(self):
		board = self.board.reshape(4,4)
		new_board = np.zeros(16)
		print(self.board)
		for j,row in enumerate(board):
			new_row = self.merge(len(np.nonzero(row)[0]),row)
			new_board[j*4:(j+1)*4] = new_row
		print(new_board)
		#sys.exit()
		self.board = new_board

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
	gameboard = chessBoard()










