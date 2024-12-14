# Write a python program for fibonacci series 
num = int(input("Enter Number of Values: "))
num1 = 0
num2 = 1
num3 = num2
count = 1
while count <= num:
    print(num1, end=" ")
    count = count + 1
    num1, num2 = num2, num3
    num3 = num1 + num2
print()
