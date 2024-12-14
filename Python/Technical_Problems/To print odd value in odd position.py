#To print odd value in odd position
x = [10,5,22,45,89,47,13,32,23,34,46,45,58,43,91]
for i in range(0,len(x)+1,2):
        if x[i]%2!=0:
            print(x[i],end=" ")
            
