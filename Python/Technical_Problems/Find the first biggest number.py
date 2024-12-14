#Find the first biggest number in a list
x=[4,8,1,5,9,3]
maximum = 0
for i in x:
    if maximum <= i:
        maximum = i
print(maximum)
