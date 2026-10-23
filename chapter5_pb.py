def count_special(A):
    n = len(A)
    total_even = sum(A[i]for i in range(0, n, 2))
    total_odd = sum(A[i]for i in range(1,n,2))

    even_before=odd_before =0 
    count = 0

    for i in range(n):
        even_after = total_even - even_before - (A[i] if i % 2 == 0 else 0)
        odd_after = total_odd - odd_before - (A[i] if i % 2 == 1 else 0)

        new_even = even_before+odd_after
        new_odd = odd_before+even_after

        if new_odd == new_even:
            count+=1
        if i%2 == 0:
            even_before+=A[i]
        else:
            odd_before+=A[i]
    return count

# print(count_special([2, 1, 6, 4]))
# print(count_special([5, 5, 2, 5, 8]))

def syracuse(n,syracuse_li = None):
    if syracuse_li is None:
        syracuse_li = []
    if n%2 == 0:
        n = n//2
        syracuse_li.append(n)
            
    else:
        n = 3*n+1
        syracuse_li.append(n)
    if n == 1:
        return syracuse_li
    return syracuse(n,syracuse_li)
# print(syracuse(5))

# Write a Python program to print the even numbers from a given list.
def print_even_num(li):
    even_number = []
    for i in li:
        if i %2==0:
            even_number.append(i)
    return even_number

def largest_even(li):
    even_number = []
    for i in li:
        if i % 2 == 0:
            even_number.append(i)
    return max(even_number)

# Write a Python program that accepts a list of numbers from the user and prints the largest odd number from the list.
def print_largest_odd():
    li = eval(input("Enter the list"))
    odd_li=[]
    for i in li:
        if i%2 != 0 :
            odd_li.append(i)
    print(max(odd_li))
li = [1,2,3,4,5,6,7,8,9,0]
# Write a Python program that accepts a list of numbers from the user and returns the smallest positive integer number that
def smallestPosInt():
    li = eval(input("Enter A list"))
    pos_li = []
    for i in li:
        if i>0:
            pos_li.append(i)
    print(min(pos_li))
# Write a Python program to swap first and last element of the list.
def swapFirstLast(li):
    li[0],li[-1] = li[-1],li[0]
    return li
# Write a Python program to find the sum of all the elements in the list.
def sumOfList(li):
    return sum(li)
# Write a Python program of Reversing a List.
def reversingList(li):
    return li[::-1]
# Write a Python program to Merging two Dictionaries
def Merging_two_Dictionaries(d1,d2):
    d1.update(d2)
    return d1
# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda
# function.
def SumPosNeg(li):
    pos_li = []
    neg_li = []
    for i in li:
        if i>0:
            pos_li.append(i)
        else:
            neg_li.append(i)
    print(f"the sum of the pos li is {sum(pos_li)} and the sum of the neg li is {sum(neg_li)}")

# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
def listDivBynineteenAndSeventeen(li):
    divisible_by_nineteen = []
    divisible_by_thirteen = []

    for i in li:
        if i %13==0:
            divisible_by_thirteen.append(i)
        if i % 19 == 0:
            divisible_by_nineteen.append(i)
    print(f"the list which is divisible by 19 is {divisible_by_nineteen}")
    print(f"the list which is divisible by 13 is {divisible_by_thirteen}")

def countingInDict(li):
    d = {}
    for i in li:
        d[i] = [i]*li.count(i)
    print(d)

# Write a Program to Print Longest Common Prefix from a given list of strings. The longest common prefix for list of strings is
# the common prefix (starting of string) between all strings. For example, in the given list [“apple”, “ape”, “zebra”], there is no
# common prefix because the 2 most dissimilar strings of the list “ape” and “zebra” do not share any starting characters. If
# there is no common prefix between all strings in the list than return -1.

def question445(li):
    reverse_li = sorted(li,reverse=True)
    prefix =""
    first_string = reverse_li[0]
    last_string = reverse_li[-1]
    for i in range(min(len(first_string),len(last_string))):
        if first_string[i] != last_string[i]:
            break
        
        prefix+=first_string[i]
    return prefix
def encrypt(text,k):
    result = ""
    for g in range(k):
        i = g
        while i<len(text):
            result +=text[i]
            i+=k
    return  result

# print(encrypt("secret message", 3))

def questio448():

# Using map func􀆟on, write a Python program to convert the given list into a tuple of strings. For the given input, the
# program must print the output as shown below -
    li = [1,2,3,4]
    result = tuple(map(str,li))
    print(result)

#     Write a Python program that mul􀆟ply each number of the given list with 10 using lambda func􀆟on. For the given input, the
# program must print the output as shown below -
    result_2 = list(map(lambda x:x*10,li))
    # print(result_2(n)for n in li)
    print(result_2)
def question449(li):
    pos_list = []
    neg_list = []
    for i in li:
        if i < 0 :
            neg_list.append(i)
        else:
            pos_list.append(i)
    print(f"The sum of the positive list is {sum(pos_list)} and the sum of the negative list is {sum(neg_list)}")
def question450(password):
    upper_count = 0 
    lower_count = 0
    num_count = 0

    if len(password)<8:
        print("Invalid")
    for i in password:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
        elif i.isdigit():
            num_count+=1
    if num_count < 1 or lower_count <1 or upper_count <1 :
        print("Invalid Password")
    else:
        print("valid")
def question451(st):
    new_st = st.lower()
    st_list = new_st.split(" ")
    d = {}
    for i in st_list:
        d[i] = d.get(i,0)+1
    print(d)
st = "Dog the quick brown fox jumps over the lazy dog"
def number_to_words(n):
    once = {
         0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen"
    }
    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    if n==0:
        return "zero"
    if n < 20:
        return once[n]
    if n < 100:
        t =(n//10)*10
        u = n%10
        return tens[t] if u==0 else tens[t]+ " "+once[u]

    h = n//100
    rest = n%100
    if rest==0:
        return once[h]+" "+"hundread"
    else:
        return once[h]+" "+"hundread and "+number_to_words(rest)
def question452(password):
    count_upper = 0 
    count_lower = 0 
    special_chr = 0 
    count_digit = 0
    digit = 0 
    if len(password)<8:
        print("This password is invalid")
    for i in password:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
        elif i.isdigit():
            count_digit+=1
            digit = (digit*10)+int(i)
        else:
            special_chr+=1
    if count_digit>3 or count_digit<1 or count_lower<1 or count_upper<1 or special_chr<1:
        print("This password is invalid")
    else:
        print("this Password is valid")
        print(digit)
        print(f"From digit to number {number_to_words(digit)}")

# Write a Python Program using function to count number of strings where the string length is 3 or more and the first and last
# character are same from a given list of string.
def question453(li):
    count =0 
    for i in li:
        if len(i)>=3:
            if i[0]==i[-1]:
                count+=1
    return count

def question454(a):
    n = len(a)
    total_even = sum(a[i] for i in range(0,n,2))
    total_odd = sum(a[i]  for i in range(1,n,2))
    even_before  = odd_before = 0
    count =0 
    for i in range(n):
        even_after = total_even-even_before-(a[i] if i%2==0 else 0)
        odd_after = total_odd-odd_before-(a[i] if i%2==1 else 0)

        new_even = even_before+odd_after
        new_odd = odd_before+even_after

        if new_even == new_odd:
            temp = li[:]
            temp.pop(i)
            count+=1
            print(f"original list{li}")
            print(f"index to be removed {i}")
            print(f"List after removing index {i} {temp}")
        if i %2 == 0 :
            even_before+=a[i]
        else:
            odd_before+=a[i]
    return count

def question455(st):
    st_li = st.split()
    dt = {}
    for i in st_li:
        key = i[0]
        if key not in dt:
            dt[key]= []
        dt[key].append(i)

    print(dt)

def set_password(password):
    
        upper_count =0 
        lower_count = 0 
        digit_count = 0 
        special_char = 0
        special_char_list = ["@","$","_"]
        if len(password) < 8 or len(password) > 15:
            print("follow the password format")
                
        for i in password: 
            if i.isupper():
                upper_count+=1
            elif i.islower():
                 lower_count+=1
            elif i.isdigit():
                digit_count+=1
            elif i in special_char_list:
                special_char+=1
            else:
                return False
        if upper_count<1 or lower_count<1 or digit_count<1 or special_char<1:
            return False
        else:
            return True
            
def question456():
        d={
            "student0":'Student@0',
            "student1":'Student@11',
            "student2":'Student@121',
            "student3":'Student@052',
            "student4":'Student@01278',
            "student5":'Student@0125', 
            "Student6":'Student@042',
            "student7":'Student@07800',
            "student8":'Student@012'}
        updated = False
        for i in range(3):
            username = input("Enter your Username:")
            password = input("Enter your Passwoerd")

            if username in d and password == d[username]:

                for i in range(3):
                    new_password = input("Enter new Password")

                    if set_password(new_password):
                        d[username]=new_password
                        updated = True
                        print("password is updated Successfully")
                        break
                    else:
                        print("Follow the password format")
                if updated == False:
                    print("Pls try after 24h")
                break
            else:
                print("Enter Correct password and username")
        else:
            print("pls try after 24h")
        print("Update Dictionary")
        print(d)
        sorted_dict = {}
        for i in sorted(d,key=lambda item:len(d[item])):
            print(i,d[i])

# Write a Python code which will return the sum of the numbers of the list.
# Return 0 for an empty list.
# Except the number 13 is very unlucky, so it does not count and number that come immediately after 13 also do not count in
# sum.
# Example :
# [1, 2, 3, 4] = 10
# [] = 0
# [1, 2, 3, 4, 13] = 10
# [13, 1, 2, 3, 13] = 5
# [1, 13, 2, 3, 4] = 8
# 4 LJU-2023
# 458 5
def question457(li):
    if li == []:
        return 0
    temp = sum(filter(lambda n:n!=13,li))
    return temp

# Write a Python program which takes a list and returns a list with the elements "shifted left by number of positions entered
# by user".
# Example:
# Input:
# List: [1, 2, 3, 4, 5]
# Shift: 2
# Output:
# [3, 4, 5, 1, 2]

def question458(li,key):
    x = li[key:]+li[:key]
    return x 

# Write a Python program that accepts a list L of size N from the user and reorders its elements in the following pattern: [L[0],
# L[N-1], L[1], L[N-2], L[2], L[N-3], ...].
# Note: You are not allowed to use any additional data structures like lists, strings, or dictionaries. The task must be
# accomplished by rearranging the elements of the original list in-place, without altering the values of the elements
# themselves.
# Example:
# Input list: [ 2, 4, 6, 8, 10]
# Output: [ 2, 10, 4, 8, 6]

def question459(li):
    size = len(li)
    for i in range(1,size-1,2):
        last_element = li.pop()
        li.insert(i,last_element)
    return li
# li = eval(input("enter List"))
# print(question459(li))
def question460(st):
    # Print the string where each word is reversed, but the word order stays the same.
    words = st.split(" ")
    vowel = ["a",'e','i','o','u',"A","E","I","O","U"]
    vowelcount = 0
    reverse_words = []
    vowel_words_list = []
    dic = {}
    for i in words:
        # reverse_words.append(i[::-1])
        print("String with each word reversed:",i[::-1],end=" ")
        # Create a dic􀆟onary with each word as a key and its length as the value.
        dic[i] = len(i)
        # Generate and display a list of words that contain at least 3 vowels.
        for j in i:
            if j in vowel:
                vowelcount+=1
        if vowelcount >= 3:
            vowel_words_list.append(i)
        # reate a dic􀆟onary of character categories: vowels, consonants (le􀆩ers of the alphabet except for the vowels), digits,
    print(f"Dictionary with word lengths:{dic}")
    print(f"Words containing at least 3 vowels {vowel_words_list}")
    category_counts = categories_vowels_consonants_letter_special(st)
    print("Character categories:",category_counts)
    counts = category_counts.values()
    highest_count = max(counts)
    for i,j in category_counts.items():
        if j == highest_count:
            print("Category with highest count",i)

# reate a dic􀆟onary of character categories: vowels, consonants (le􀆩ers of the alphabet except for the vowels), digits,
def categories_vowels_consonants_letter_special(st):
    category_counts = {
    "vowels": 0,
    "consonants": 0,
    "digits": 0,
    "special": 0
}
    vowel = ["a",'e','i','o','u',"A","E","I","O","U"]
    lower_st = st.lower()
    for ch in lower_st:
        if "a" <= ch <= "z":
            if ch in vowel:
                    category_counts["vowels"] += 1
            else:
                    category_counts["consonants"]+=1
        elif "0" <= ch <= "9":
            category_counts['digits']+=1
        else:
            category_counts["special"]+=1
    return category_counts
    
# st = "Computers 2025 are far more powerful and efficient!!"
# question460(st)


# Given a string S containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "{[()]}"
# Output: Valid

def question461(st):
    matching_bracket = {
        "]":"[",
        "}":"{",
        ")":"("
    }
    is_valid = True
    opening_bracket = [] #this will be out temp stack
    for i in st:       
        if i in "({[":
            opening_bracket.append(i)
        elif i in ")}]":
            if len(opening_bracket) == 0:
                is_valid = False
                break
            top_bracket = opening_bracket.pop()
            if top_bracket != matching_bracket[i]:
                is_valid = False
                break
    if is_valid:
        print("valid")
    else:
        print("Not valid")
