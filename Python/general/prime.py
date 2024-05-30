"""
def check_prime():
    number = input("Enter a number: ")
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")

check_prime()
"""

def check_prime():
    number = int(input("Enter a number: "))
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")

check_prime()
