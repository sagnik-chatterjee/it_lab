'''
@author Sagnik Chatterjee
Python program to implement a simple calculator which performs addition, 
subtraction, multiplication and division
'''

def addition(num1 =0 ,num2=0):
    '''
    Adds the 2 args provided 
    Return:
        The value obtained after adding the 2 values 
    '''
    return num1+num2 

def subtraction(num1=0,num2=0):
    '''
    Subtracts the 2 args provided
    Return:
        The value obtained after subtracting these 2 values 
    '''
    return num1-num2 

def divides_float(num1 ,num2):
    '''
    Floating point divison of  the 2 args provided 
    Return:
        The value obtained after dividing the 2 values 
    '''
    try:
        return num1/num2
    except Exception as e:
        print(e)

def divides_int(num1,num2):
    '''
    Integer type divison of  the 2 args provided 
    Return:
        The value obtained after dividing the 2 values 
    '''
    try:
        return num1//num2
    except Exception as e:
        print(e)
        

def multiplication(num1 ,num2):
    '''
    Adds the 2 args provided 
    Return:
        The value obtained after multiplying the 2 values 
    '''
    return num1*num2 


def main():
    status=True
    while status:
        num1=int(input('Enter the first value:- '))
        num2=int(input('Enter the second value:- '))

        op=input("Enter the operation to be done :- \n")
        if op=='+':
            print(addition(num1,num2))
        elif op=='-':
            print(subtraction(num1,num2))
        elif op=='*':
            print(multiplication(num1,num2))
        elif op=='/':
            print(divides_float(num1,num2))
        elif op=='//':
            print(divides_int(num1,num2))
        else:
            print("Invalid choice .")

        h=input("Continue ?(y|N)")

        if(h=='y' or y=='Y'):
            status=True 
        else:
            status=False 
            break

main()