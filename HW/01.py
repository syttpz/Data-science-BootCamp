'''
Homework Questions
1. Write a program that takes a word as an input and print the number of vowels in the word.
2. Iterate through the following list of animals and print each one in all caps.

  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
4. Write a program to check if a string is a palindrome or not.
5. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
'''

def printNumVow():
    word: int = input("Please input a word: ")
    count = 0
    if not word.isalpha():
        raise ValueError("Input should only contain letters")
        return
    for char in word:
        if char.lower() in 'aeiou':
            count += 1
    return count

def printAnimals(li: list):
    for animal in li:
        print(animal.upper())

def printOddEven(x: int):
    for i in range(1, x+1):
        if i % 2 == 0:
            print(str(i) + " - even")
        else:
            print(str(i) + " - odd")

def isPalindrome(s: str):
    if not s.isalpha():
        raise ValueError("Input should only contain letters")
        return
    s = s.lower()
    return s == s[::-1]


def sum_of_integers(a: int, b: int):
    return a + b;


if __name__ == "__main__":
    print(printNumVow())
    animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    printAnimals(animals)
    printOddEven(20)
    check_palin = input("Please input a word (Palindrome check): ")
    print(isPalindrome(check_palin))
    a, b = input("Input two integers: ").split()
    print(sum_of_integers(int(a), int(b)))
