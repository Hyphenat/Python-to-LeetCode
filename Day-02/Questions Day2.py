# Print first and last element of the list
list=[5,10,15,20,25]
print(list[0])
print(list[-1])

# sum of the list
sum=0
list=[10,20,30,40]
for i in list:
    sum+=i
print(sum)

list=[7, 15, 2, 90, 35]

# largest element in the list
largest=list[0]
for i in list:
    if i> largest:
        largest=i
    print(largest)

# count of odd number in the list
list=[1, 2, 3, 4, 5, 6, 7]
count=0
for i in list:
    if i %2!=0:
        count+=1
print(count)