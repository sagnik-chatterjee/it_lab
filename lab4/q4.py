'''
@author Sagnik Chaterjee 

Python class which has two methods get_String and print_String.
get_String accept a string from the user and print_String print the string in upper
case.
'''

class q4:

	def __init__(self):
		self.string=""

	def get_String(self):
		'''
		accepts a string from user 
		'''
		self.string=input("Enter the string :- ")

	def print_String(self):
		'''
		prints the string passed 
		'''
		print("The string printed is :- ")
		print(self.string)

def main():
	obj1= q4()
	obj1.get_String()
	obj1.print_String()

if __name__=='__main__':
	main()
