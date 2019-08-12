"""
Code to automatically play 2048
"""
import numpy as np

class responsive_2048_AI():

	def __init__(self,mode):
		self.mode = mode
		self.previous_key = ""

	def decision(self,board,chessboard):
		movable = ["A","W","S","D"]
		scoreconvert = {0:0,
						2:2,
						4:4,
						8:9,
						16:19,
						32:39,
						64:79,
						128:159,
						256:319,
						512:639,
						1024:1279,
						2048:2559,
						4096:5119,
						8192:10239,
						16384:20479}

		if self.mode == "random":
	 		return np.random.choice(movable)

	 	elif self.mode == "simple_corner":
	 		
	 		newboard = chessboard.update_gameboard(board.copy(),"A")
	 		if (newboard == board.copy()).all():
	 			newboard = chessboard.update_gameboard(board.copy(),"W")
 				if (newboard == board.copy()).all():
 					newboard = chessboard.update_gameboard(board.copy(),"S")
 					if (newboard == board.copy()).all():
 						newboard = chessboard.update_gameboard(board.copy(),"D")
 						if (newboard == board.copy()).all():
 							return "C"
 						else:
 							return "D"
 					else:
 						return "S"
 				else:
 					return "W"
 			else:
 				return "A"



	 	elif self.mode == "simple_max":

	 		score = 0
	 		nonzero = 100
	 		decision = movable[0]

	 		for move in movable:
	 			newboard = chessboard.update_gameboard(board.copy(),move)
	 			if (newboard == board.copy()).all():
	 				continue
	 			higher = [scoreconvert[x] for x in newboard]
	 			print move,sum(higher),
	 			if sum(higher) > score:
	 				score = sum(higher)
	 				decision = move
	 				
	 				continue
	 			if sum(newboard) == score:
	 				if len(np.nonzero(newboard)) < nonzero:
	 					nonzero = len(np.nonzero(newboard))
	 					decision = move
	 		print(decision)
	 		return decision






		 	


