# 1. Find the length of a string without using len().
n="Nandini"
count=0
for x in n:
    count+=1
print(count)
# 2. Reverse a string without using slicing or reversed().
n="Nandini"
rev=0
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
# 7. Convert a string to uppercase without using upper().
# 8. Remove all spaces from a string.
# 9. Count the digits in a string.
# 10. Swap the first and last characters of a string.
# 11. Print the characters at even indices of a string.
# 12. Reverse each word in a sentence without changing word order.
# 13. Reverse the order of words in a sentence.
# 14. Remove duplicate characters while preserving their original order.
# 15. Find the first non-repeating character in a string.
# 16. Find all duplicate characters in a string.
# 17. Toggle the case of every character in a string.
# 18. Find the longest word in a sentence.
# 19. Replace every occurrence of a character with another character.
# 20. Compress consecutive repeated characters in a string.
# 21. Count the frequency of every character in a string.
# 22. Find the most frequent character in a string.
# 23. Check whether two strings are anagrams.
# 24. Check whether a string contains only digits.
# 25. Check whether one string is a rotation of another.
# 26. Find the common characters between two strings, including duplicates.
# 27. Check whether two strings are isomorphic.
# 28. Find the longest common prefix among a list of strings.
# 29. Check whether a string contains all unique characters.
# 30. Find the minimum number of deletions required to make two strings anagrams.
# 31. Count the occurrences of a substring, including overlapping occurrences.
# 32. Find the first occurrence of a substring without using built-in substring search.
# 33. Check whether one string is a subsequence of another.
# 34. Find the length of the longest substring without repeating characters.
# 35. Find the longest palindromic substring.
# 36. Count all palindromic substrings in a string.
# 37. Find the length of the longest substring that can be made of identical characters using at most k replacements.
# 38. Find all starting indices of substrings that are anagrams of a given pattern.
# 39. Find the minimum window substring containing all characters of another string.
# 40. Find the shortest substring containing every distinct character in the original string.
# 41. Implement string-to-integer conversion with sign, whitespace, and 32-bit overflow handling.
# 42. Add two binary strings without converting them into integers.
# 43. Multiply two non-negative integers represented as strings without converting them into integers.
# 44. Decode a string containing nested repetition patterns.
# 45. Find the minimum edit distance between two strings.
# 46. Implement regular expression matching with . and *.
# 47. Implement wildcard matching with ? and *.
# 48. Count the distinct subsequences of one string that equal another string.
# 49. Find the shortest palindrome by adding characters only to the beginning.
# 50. Implement the KMP string-matching algorithm without using built-in substring search.
