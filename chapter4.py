def caesar_cipher(text,key):
        result = []
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                result.append(chr((ord(char) - base+key)%26+ base))
            else:
                result.append(char) #this is for the space 
        return "".join(result)



# Write a Python program to check if a string is palindrome or not.
def palindrome(string):
    temp = string[::-1]
    if temp == string:
        print("This string is palindrome")
    else:
        print("This string is not palindrome")

# Write a Python program to Find length of a string in python.
def lengthString(string):
    print(len(string))

# Write a Python function to find length of a string in python without using len function.
def stringLen(string):
    count = 0 
    for i in string:
        count+=1
    print(count)
# Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.
def calcUpperLower(string):
    upper = 0 
    lower = 0 
    for char in string:
        if char.isupper():
            upper+=1
        else:
            lower+=1
    print(f"the sum of the upper case is {upper} and the sum of the lower case is {lower}")

# Write a Python program to demonstrate the negative index in a Tuple
def demonstrate_tupple():
    tl = (1,2,3,4,5,6)
    print(tl[-1])
    print(tl[-2])
    print(tl[-4])

# Write a program to remove I'th character from string in python.
def removeIthchar(string,i):
    if (i<0) or (i>=len(string)):
        return "This is invalid Index"
    return string[:i]+string[i+1:] 

# Write a program to create a string made of first,middle and last character.

def first_middle_last(text):
    mid = len(text)//2
    print(text[0]+text[mid]+text[-1])


# Write a python program that prompts the user to enter a string and calculate the sum and average of the digits
# present in a string.
# Example 1:
# String: "abc123xyz"
# Sum of digits = 6
# Average of digits = 2.0 Example 2:
# String: "Tuesday"
# No digits found in the string.

def digitcalc(text):
    count = 0
    sum = 0 
    for i in text:
        if i.isdigit():
            count+=1
            sum+=int(i)
    print(f"the Sum of digit is {sum} and the average is{sum/count}")

# Write a program to reverse a given string/
def reverse_string (string):
    print(string[::-1])

# Write a Python program to print even length words in a string.
def even_word_string(string):
    words = string.split()
    for word in words:
        if len(word) %2 == 0:
            print(word)

# Write a Python program to Uppercase Half String from the given string.
def UppercaseHalfString(string):
    mid = len(string) // 2
    print(string[:mid]+string[mid+1:].upper())

# Write a Python program to capitalize the first and last character of each word in a string
def capFirstLast(string):
    st = string[0].upper() + string[1:-1]+string[-1].upper()
    return st
# Write a program to Create a string made of the middle three characters
def middleChar(string):
    mid = len(string)//2
    text = string[mid-1:mid+2]
    return text

# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the
# characters in the s1 are present in s2. The character’s position doesn’t matter.

def twoBalanceString(s1,s2):
    for ch in s1:
        if ch not in s2:
            return False
    return True
# Write a program to Split a string on hyphens
def split_on_hyphens(string):
    return string.split("-")
# Write a program to print maximum and minimum elements in given Tuple.
def MaxandMin_of_tuple(tl):
    maxi = max(tl)
    mini = min(tl)
    print(f"max element in tuple is {maxi} and lowerst is {mini} ")
# Write a Program to print even numbers from given Tuple
def printEven(tuple):
    for i in tuple:
        if i % 2 == 0 :
            print(i)

# Write a program to print sum of even numbers and sum of odd numbers from elements given in tuple.
def sumEvenOdd(tl):
    sum_odd = 0 
    sum_even = 0
    for i in tl:
        if i % 2 == 0 :
            sum_even+=i
        else:
            sum_odd+=i
    print(f"The Sum of the Even is {sum_even} and The Sum of the Odd is {sum_odd}")


# Write a Python program using function to shift the decimal digits n places to the left, wrapping the extra digits around. If
# shift > the number of digits of n, then reverse the string.
# Note:
# Function will take two parameters:
# 1. The number
# 2. How much shift user want

def shiftDigit(n,shift):
    s = str(n)
    length = len(s)
    if shift > length:
        return s[::-1]
    shift = shift % length
    return s[shift::]+s[:shift] #this is working on index you stupid this is not woking on the element 

# Write a Python programme that accepts a string and calculate the number of uppercase letters, lowercase letters and
# number of digits.
# For example,
# Input: Hello Pyth@n is 100% easy
# Output:
# Uppercase letters : 2
# Lowercase letters : 14
# Digits : 3

def cal_upper_lower_digit(st):
    c_upper = 0 
    c_lower = 0 
    c_digit = 0
    for i in st:
        if i.isupper():
            c_upper+=1
        elif i.islower():
            c_lower+=1
        elif i.isdigit():
            c_digit+=1
    return c_upper,c_lower,c_digit

# Write a python program to check the validity of a Password.
# q - 316

def valiation_password(password):
    count_Upper = 0 
    count_digit = 0 
    count_spaceCase = 0 
    if len(password)<8:
        print("This password is Invalid the alpha must be of 8")
        return
    
    for i in password:
        if i.isupper():
            count_Upper+=1
        elif i.isdigit():
            count_digit+=1
        elif not i.isalnum():
            count_spaceCase+=1

    if count_spaceCase <1 or count_digit< 1 or count_Upper < 1:
        print("Your Password is Invalid")
    else:
        print("Your Password Is Valid")

# Write a Python program to return another string similar to the input string, but with its case inverted.
# For example, input of “Mr. Ed” will result in “mR. eD” as the output string.
# Note: Use of built in swapcase function is prohibited.

def swapLetter(st):
    result = []
    for  char in st:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return "".join(result)

# Write a Python program to create a Caesar encryption.
# Note: In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar
# shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in
# which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For
# example, with a right shift of 3, A would be replaced by D, E would become H, and so on. The method is named
# after Julius Caesar, who used it in his private correspondence.
# For Example:
# Input Text : LJIET ENG
# Shift : 3
# Cipher: OMLHW HQJ

def caesar_chipher(text,key):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    result = ""
    for ch in text:
        if ch in upper:
            index = upper.index 