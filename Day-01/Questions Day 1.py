# Q1.Print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)

# Q2. Print even or odd from a given number 
# number = int(input("Enter a number:"))

# if number/2 ==0:
#     print("Even")
# else:
#     print("Odd")

#  Q3. Print the square of a number

def sq(x):
    return x*x

result = sq(5)
print(result)

# Q4 Cube of the number

def cube(x):
    return x*x*x

result=cube(5)
print(result)

# Q5. Print positive or negative from a given number

def pos(x):
    if x>0:
        return "positive"
    else:
        return "negative"

result=pos(5)
print(result)

# Q6. Print the largest number from two numbers

def two(x,y):
    if x>y:
        return x
    else:
        return y
result=two(5,6)
print(result)