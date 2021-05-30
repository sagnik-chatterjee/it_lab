'''
@author Sagnik Chaterjee 

Python class to get all possible unique subsets from a set of distinct 
integers 
'''


class q1:
	'''
	to find the all possible unique subsets
	'''

	def subsetsRecur(self,current,sset):
		'''
		generate the subsets recursively 
		'''
		if sset:
			return self.subsetsRecur(current,sset[1:])+self.subsetsRecur(current+[sset[0]],sset[1:])
		return [current]

	def sub_sets(self,sset):
		return self.subsetsRecur([],sorted(sset))



def main():
	h=int(input('Enter the size of the list:- '))
	list_1=[]
	while (h > 0):
		q=int(input())
		list_1.append(q)
		h=h-1
	q= q1().sub_sets(list_1)
	print(q)

if __name__=='__main__':
	main()