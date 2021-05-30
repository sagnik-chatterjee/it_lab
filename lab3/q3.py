'''
@author Sagnik Chatterjee
Python program to implement binary search with recursion 

'''
from typing import List
def binary_search_recursive(arr:List, elem:int, start:int, end:int):
    '''
	Recursive binary search algorithm that finds the element in a list 
	in O(logn) array.
	'''
    if start > end:
        return -1

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)

def main():
	n=int(input("Enter the size of the list for binary search: "))
	list_1=[]
	print("Now enter the elements of the list")
	while n>0:
		p=int(input(""))
		list_1.append(p)
		n=n-1
	list_1.sort() ## sorting the list incase it was not sorted 
	
	check=int(input("Enter the element to search :- "))
	result = binary_search_recursive(list_1,check,0,len(list_1)-1)
	
	if result!=-1:
		print("Element found at index :- ",result)
	else:
		print("Element not found")

	 
	

main()