import numpy as np

from src.engine_2048 import chessBoard
from src.ai_2048 import responsive_2048_AI


def play_2048(init_board = []):

	board = init_board if init_board !=[] else np.zeros(16)
	#old_board = board.copy()

	AI = responsive_2048_AI(mode="simple_max")
	chessboard = chessBoard()

	for i in range(1000):

		board,over = chessboard.place_random(board)

		
		print(np.array(board,dtype="int").reshape(4,4))
		print("*"*40)

		if over:
			print("Game over")
			break

		decision = AI.decision(board,chessboard)
		if decision == "C":
			print("Game over C")
			break
		board = chessboard.update_gameboard(board,decision)

		

		
"""
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
"""



if __name__ == "__main__":

	play_2048()


