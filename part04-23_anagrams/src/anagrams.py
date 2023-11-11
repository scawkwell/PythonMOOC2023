# Write your solution here
def anagrams(string_1, string_2):
    if sorted(string_1) == sorted(string_2):
        return True
    else:
        return False
    
