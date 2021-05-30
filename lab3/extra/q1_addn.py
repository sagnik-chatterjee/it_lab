def main():
    p=int(input("Enter the size of the list : "))
    list1=[]
    while p >0:
        q=int(input())
        list1.append(q)
        p=p-1 
        
    list1.sort()
    print(list1[0])
    
main()
    