# Approach 1: Simple input and addition


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(type(num1))
print(type(num2))
print(num1 + num2)


#Approach2
num1=input("Enter first number:")
num2=input("Enter second number:")
print(int(num1)+int(num2))



# 1. Get user input. The input() function always returns a string (str).
num1 = input("Enter first decimal number: ")
num2 = input("Enter second decimal number: ")
print(type(num1)) # str
print(type(num2)) # str
print(float(num1) + float(num2)) # 31.0