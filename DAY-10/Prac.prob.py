# 1. Find the length of a string without using len().
n="Nandini"
count=0
for x in n:
    count+=1
print(count)
# 2. Reverse a string without using slicing or reversed().
n="Nandini"
rev=""
for i in n:
    rev=i+rev
print(rev)
# 3. Check whether a string is a palindrome.
a="afifa"
if a==a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
# 4. Count the vowels in a string.
n="Nandini"
count=0
for x in n.lower():
    if x in "aeiou":
        count+=1
print(count)
# 5. Count the uppercase and lowercase letters in a string.
a="Nandini"
upper=0
lower=0
for x in a:
    if x.isupper():
        upper+=1
    elif x.islower():
        lower+=1
print("Uppercase letters:",upper)
print("Lowercase letters:",lower)        
# 6. Count the occurrences of a given character in a string.
m="nandu"
count=0
char="n"
for x in m:
    if x==char:
        count+=1
print(count)
# 7. Convert a string to uppercase without using upper().
n="nandini"
result=""
for x in n:
    if 'a'<=x<='z':
        result+=chr(ord(x)-32)
    else:
        result+=x
print(result)
# 8. Remove all spaces from a string.
n="N a n dini"
print(n.replace(" ",""))
# 9. Count the digits in a string.
n="Nandini2185"
count=0
for x in n:
    if x.isdigit():
        count+=1
print(count)
# 10. Swap the first and last characters of a string.
n="Nandini"
n=n[-1]+n[1:-1]+n[0]
print(n)
# 11. Print the characters at even indices of a string.
l="Nandini"
for i in range(len(l)):
    if i%2==0:
        print(l[i])
