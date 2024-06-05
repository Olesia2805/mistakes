"""
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]

input_string = "A man a plan a canal Panama"
print("There is a palindrome:", is_palindrome(input_string))
"""

import re

def is_palindrome(s):
    
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s)

    if s == s[::-1]:
        return True
    
    return False

def test_is_palindrome():
 # Test 1: Normal palindrome
 assert is_palindrome("A man, a plan, a canal, Panama") == True, "Test 1 failed"

 # Test 2: Palindrome with different cases
 assert is_palindrome("No 'x' in Nixon") == True, "Test 2 failed"

 # Test 3: Palindrome with numbers
 assert is_palindrome("12321") == True, "Test 3 failed"

 # Test 4: Not a palindrome
 assert is_palindrome("Hello, world!") == False, "Test 4 failed"

 # Test 5: An empty string
 assert is_palindrome("") == True, "Test 5 failed"

 # Test 6: Palindrome with symbols
 assert is_palindrome("Was it a car or a cat I saw?") == True, "Test 6 failed"

 # Test 7: Palindrome of one character
 assert is_palindrome("a") == True, "Test 7 failed"

 print("All tests passed")

# Running tests
test_is_palindrome()