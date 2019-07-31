import sys
import numpy as np

class chessBoard():

	def __init__(self,board=[]):

		self.board = board if board !=[] else np.zeros(16)

		print("*"*20,"\n",np.array(self.board,dtype="int").reshape(4,4))

		while True:
			self.score = np.sum(self.board)
			old_board = self.board
			self.user_input()
			if (self.board == old_board).all():
				print("No merge happened")
				continue
			else:
				cur_board = list(self.board[self.board == 0])
				if len(cur_board) > 1:
					iteration = np.random.choice([1,1,2])
					for _ in range(iteration):
						zero_location = np.random.choice(np.where(self.board == 0)[0])
						self.board[zero_location] = np.random.choice([2,4])
				elif len(cur_board) == 1:
					zero_location = np.random.choice(np.where(self.board == 0)[0])
					self.board[zero_location] = np.random.choice([2,4])

				print("*"*20,"\n",np.array(self.board,dtype="int").reshape(4,4))

				if len(list(self.board[self.board == 0])) == 0:
					lose = True
					for row in self.board.reshape(4,4):
						for i in range(4-1):
							if row[i] == row[i+1]:
								lose = False
					for row in self.board.reshape(4,4).T:
						for i in range(4-1):
							if row[i] == row[i+1]:
								lose = False
					if lose:
						print("You Lost, total score = %s"%self.score)
						sys.exit()
				
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
			print("Quit Game")
			sys.exit()
		else:
			print("Unknown input, Q to quit")
			return user_input()

	def merge(self,length,x,direction="left"):

		new_list = np.zeros(4)
		nonzero_x = np.array(x)[np.nonzero(x)[0]]
		

		if direction == "right":
			nonzero_x = nonzero_x[::-1]

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

		if direction == "right":
			new_list = new_list[::-1]
		if length == nonzero:
			return new_list
		else:
			return self.merge(nonzero, new_list, direction)

	def move_left(self):
		new_board = np.zeros(16)
		for j,row in enumerate(self.board.reshape(4,4)):
			new_board[j*4:(j+1)*4] = self.merge(len(np.nonzero(row)[0]),row,"left")
		self.board = new_board

	def move_right(self):
		new_board = np.zeros(16)
		for j,row in enumerate(self.board.reshape(4,4)):
			new_board[j*4:(j+1)*4] = self.merge(len(np.nonzero(row)[0]),row,"right")
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
	board = np.array([[512.,8.,2.,0.],
					 [256.,32.,2.,0.],
					 [128.,32.,2.,0.],
					 [ 32.,4.,0.,0.]]).reshape(-1)

	board = np.array([[512.,8.,2.,0.],
					 [256.,32.,2.,0.],
					 [8.,8.,8.,0.],
					 [ 32.,4.,0.,0.]]).reshape(-1)

	board = np.array([[512.,32.,8.,4.],
					 [256.,64.,2.,2.],
					 [128.,16.,4.,4.],
					 [ 32.,8.,4.,8.]]).reshape(-1)

	board = np.array([[1024.,16.,8.,4.],
					 [ 256.,64.,4.,2.],
					 [  64.,8.,2.,0.],
					 [   0.,0.,0.,0.]]).reshape(-1)

	board = np.array([[1024.,0.,0.,0.],
					 [ 512.,4.,0.,4.],
					 [  256.,2.,8.,0.],
					 [   256.,16.,4.,2.]]).reshape(-1)
	board = np.array([[4,16,2048,0],
					  [2,8,128,8],
					  [8,2,8,2],
					  [2,8,16,4]]).reshape(-1)

	chessBoard(board)








