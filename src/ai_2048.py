"""
Code to automatically play 2048
"""
import numpy as np

class AI_2048():

	def __init__(self,mode):
		self.mode = mode
		self.previous_key = ""


	
	def decision(self,moved):

		if self.mode == "random":
	 		return np.random.choice(["W","A","S","D"])

	 	elif self.mode == "simple":
	 		if moved:
	 			self.previous_key = "A"
	 			return "A"
	 		else:
	 			if self.previous_key == "A":
		 			self.previous_key = "W"
		 			return "W"
		 		elif self.previous_key == "W":
					self.previous_key = "S"
		 			return "S"
		 		elif self.previous_key == "S":
		 			self.previous_key = "D"
		 			return "D"
		 		elif self.previous_key == "D":
		 			self.previous_key = "A"
		 			return "C"
		 		#else:
		 		#	self.previous_key = "A"
		 		#	return "A"


