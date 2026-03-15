# wap to find the greatest of 3 numbers entered by the user
num = int(input("Enter first number- "))
num1 = int(input("Enter second number- "))
num2 = int(input("Enter third number- "))
if (num >= num1 and num >= num2):
    print("First number is greatest",num)
elif(num1 >= num2):
    print("Second number is greatest",num1)
else:
    print("Third number is greatest",num2)
