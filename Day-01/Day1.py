#Hello world 
print("Hello World")

#variable
name = "Farhan"
age = 22

print(name)
print(age)

print(type(name))
 
#  Inputs

# name = input("Enter name: ")
# print(name)

# int Inputs

# age = int(input("enter age:"))
# print(age)

# Arithmetic 
a=10
b=15

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

# comparison

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# If else

age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Multiple conditions

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
else :
    print("Grade c")

# # For Loop

# for i in range(1,6):
#     print(i)

i=1
while i <=5:
    print(i)
    i+=1

# Functions

def greet():
    print("Hello World")

greet()

# Funtion with parameter

def greet(name):
    print("Hello", name )

greet("Farhan")

 #Funtion with return value

def add(a,b):
    return a+b

result = add(10,20)
print(result)

