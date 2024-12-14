#To Print Second Maximum Number in a List
x = [69,96,88,55,44,43,24]
first_biggest = 0
second_biggest = 0
for i in x:
    if i > first_biggest:
        second_biggest = first_biggest
        first_biggest = i
    elif i > second_biggest and i!= first_biggest:
        second_biggest = i
        print("Second Biggest Number is:",second_biggest)
