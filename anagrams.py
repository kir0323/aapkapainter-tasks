"""Write a code that checks if two given strings are anagrams
Sample Input: Mary Army
Output: Yes"""


def check(s1, s2):
    if sorted(s1.lower()) == sorted(s2.lower()):
        print("Yes")
    else:
        print("Noo")


check("Mary", "Army")
