#To print count of odd value and even value
x = [10,5,23,45,89,47,13]
odd_count = 0
even_count = 0
for i in range(0,len(x)):
    if x[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Total Odd Count is:",odd_count)
print("Total Even Count is:",even_count)
