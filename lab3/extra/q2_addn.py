#bubble sort 

def bubble_sort(list1):
    n=len(list1)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1]= list1[j+1],list1[j]
    
    return list1                


def main():
    p=int(input("Enter the the size of the list "))
    arr=[]
    while p>0:
        q=int(input())
        arr.append(q)
        p=p-1
    print(bubble_sort(arr))

main()
        