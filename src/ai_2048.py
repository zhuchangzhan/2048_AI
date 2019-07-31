"""
Code to automatically play 2048
"""
import numpy as np

class AI_2048():

	def __init__(self,mode):
		self.mode = mode
	
	def decision(self):
		if self.mode == "random":
	 		return np.random.choice(["W","A","S","D"])
	 		