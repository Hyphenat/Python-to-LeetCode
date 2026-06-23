# Print first and last character of the string
name="farhan"

print(name[0])
print(name[-1])

# count of a particular character in the string('a')
word="banana"
count=0
for ch in word:
    if ch =='a':
        count+=1
print(count)

# count of vowels in the string
word="education "
count=0
for ch in word:
    if ch in'aeiou':
        count+=1
print(count)

# Reverse string
print(name[::-1])

# Palindrome or not palindrome
word="level"

for ch in word:
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")