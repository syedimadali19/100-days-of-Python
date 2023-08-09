#Program to create a simple calculator in python


#taking operator
opt=int(input("Select a number to use an operator:\n1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\n"))

#taking input values
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

#building an if-elif ladder to focus on specific operation
if(opt==1):
    add=num1+num2
    print("The Addition of",num1,"and",num2,"is",add)

elif(opt==2):
    sub=num1-num2
    print("The Subtraction of",num1,"and",num2,"is",sub)

elif(opt==3):
    mul=num1*num2
    print("The Multiplication of",num1,"and",num2,"is",mul)

else:
    if(num2==0):
        print("The Division of",num1,"and",num2,"is Undefined")
    else:
        div=(num1)/(num2)
        print("The Division of",num1,"and",num2,"is",div)
