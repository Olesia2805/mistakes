"""
def count_vowels():
    word = input("Enter the word: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in word:
        if letter in vowels:
            count += non_vowels_count

    print("Number of vowels in a word:", count)

count_vowels()
"""

def count_vowels():
    
    word = input("Enter the word: ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1
        
    print("Number of vowels in a word:", count)

count_vowels()