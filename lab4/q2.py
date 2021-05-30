'''
@author Sagnik Chaterjee 

Python class to find a pair of elements (indices of the two numbers) from
a given array whose sum equals a specific target number. 
'''
from typing import List 

class q2:
	'''
	class finds the pair of elements from given list 
	such that sum equals a specific target number.
	'''
	def specific_value(self,list1:List,target:int)->List:
		'''
		method which finds the pair of elements which have the speicifc sum
		Returns :
		A list of tuples of the pair which give the target sum.
		'''
		pair=[]
		for i in range(len(list1)):
			for j in range(len(list1)):
				if i!=j:
					if(list1[i]+list1[j]==target):
						tup_le =(list1[i],list1[j])
						pair.append(tup_le)
		return pair 



def main():
	p=int(input("Enter the size of the list"))
	list1=[]
	while (p>0):
		h=int(input())
		list1.append(h)
		p=p-1
	target=int(input("Enter the target value "))
	print(q2().specific_value(list1,target))

if __name__=='__main__':
	main()
