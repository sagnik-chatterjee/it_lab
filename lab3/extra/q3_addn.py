## program to multiply 2 matrices


def main():
    n,m=map(int,input("Enter the dimension of matrix 1 ").split())
    a,b=map(int,input("ENter the dimension of matrix 2 ").split())
    
    if(m!=a):
        print("This matrix multiplication will not work ")
        quit()
    else:
        matrix1=[[]]
        for i in range(0,n+1):
            for j in range(0,i+1):
                matrix1.append(j)
            