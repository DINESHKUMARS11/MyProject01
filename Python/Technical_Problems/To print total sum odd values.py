#To print total sum odd values
x = [10,5,20,48,89,42,13]
sum = 0
for i in range(0,len(x)):
    if x[i]%2!=0:
        sum = sum + x[i]
print("Toal sum of Odd Values is:",sum)
