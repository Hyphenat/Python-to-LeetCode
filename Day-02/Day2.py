# # List

# nums=[10,20,30,40]

# print(nums[0])
# print(nums[1])

# # Negative listing

# print(nums[-1]) #last element
# print(nums[-2]) #second last element

# # List length

# print(len(nums))

# # Transversing a list 

# for i in nums:
#     print(i)

# for i in range(len(nums)):
#     print(nums[i])

# appending

num=[10,20,6,5]

num.append(30)
print(num)

# pop

num.pop()

print(num)

# updating value

num[1] = 15
print(num)

# Sum of the list

print(sum(num))

# Manual sum method

total=0

for i in num:
    total+=i
    print(total)

# largest element in the list
largest=num[0]
for i in num:
    if i>largest:
        i=largest
    print(largest)

# Count the number of even number in the list
num=[10,25,5,6,24]
count=0
for i in num:
    if i % 2==0:
        count+=1
print(count)
   


