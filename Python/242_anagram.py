# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically 
# using all the original letters exactly once.

s = "anagram"
t = "nagaram"

saludo = "hola"
hi = "hi"

def check_anagram(s: str, t: str) -> bool:
    # validate if 2 given strings are anagram of 
    # each other 
    
    return True if sorted(s) == sorted(t) else False

print(check_anagram(s, t))
print(check_anagram(saludo, hi))
