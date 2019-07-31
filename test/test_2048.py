import os,sys
import numpy as np

DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(DIR, '..'))

from src.engine_2048 import chessBoard


if __name__ == "__main__":
	# Test up merge
	board = np.array([[512.,8.,2.,0.],
					 [256.,32.,2.,0.],
					 [128.,32.,2.,0.],
					 [ 32.,4.,0.,0.]]).reshape(-1)
	# Test left/right merge
	board = np.array([[512.,8.,2.,0.],
					 [256.,32.,2.,0.],
					 [8.,8.,8.,0.],
					 [ 32.,4.,0.,0.]]).reshape(-1)
	# Test game board full
	board = np.array([[512.,32.,8.,4.],
					 [256.,64.,2.,2.],
					 [128.,16.,4.,4.],
					 [ 32.,8.,4.,8.]]).reshape(-1)
	# Test no left or up movement allowed
	board = np.array([[1024.,16.,8.,4.],
					 [ 256.,64.,4.,2.],
					 [  64.,8.,2.,0.],
					 [   0.,0.,0.,0.]]).reshape(-1)
	# Test Win
	board = np.array([[1024.,0.,0.,0.],
					 [ 512.,4.,0.,4.],
					 [  256.,2.,8.,0.],
					 [   256.,16.,4.,2.]]).reshape(-1)
	# Test lose
	board = np.array([[4,16,2048,0],
					  [2,8,128,8],
					  [8,2,8,2],
					  [2,8,16,4]]).reshape(-1)

	chessBoard(board)