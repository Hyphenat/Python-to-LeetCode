# String

name ="farhan"
print(name)

# String indexing

print(name[0])
print(name[-1])

# length of string

print(len(name))

# Transversing string

for ch in name:
    print(ch)

# Count a particular character
count=0
for ch in name:
    if(ch=='a'):
        print(ch)
        count+=1
print(count)

# Count vowels

count=0
for ch in name:
    if ch in 'aeiou':
        count+=1
print(count)

# Uppercase

print(name.upper())

# Lowercase

print(name.lower())

# Reverse string

print(name[::-1])

# Palindrome EX:madam,racecar,level
word="racecar"
for ch in word:
    if word==word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
