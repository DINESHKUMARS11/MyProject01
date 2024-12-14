#To Print Maximum Number in a List
x = [10,5,20,48,89,42,13]
max = x[0]
for i in x:
    if i > max:
        max = i
print("Maximum Number is:",max)
