'''
@author Sagnik Chatterjee
Python program to sort words in alphabetical order 
'''

def main():
	print("Enter the string")
	str_1=input()

	words = [word for word in str_1.split()]

	print("The original words without sorting are:- \n")
	for word in words:
		print(word)
	
	##sorting the list 
	words.sort()

	print("The sorted words are :- \n")
	for word in words:
		print(word)

if __name__=='__main__':
	main()
