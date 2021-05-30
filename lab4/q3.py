'''
@author Sagnik Chaterjee 

Python class to implement pow(x,n)
'''

import math 

class q3:
	'''
	Python class that implements pow(x,n) and returns the value 
	'''
	def power(self,x:float=1,n:int=0)->float:
		'''
		Returns:
		Returns the power of x raised to n 
		'''
		return math.pow(x,n)

def main():
	x=int(input("Enter x: "))
	n=int(input("Enter n: "))
	print(q3().power(x,n))

if __name__=='__main__':
	main()