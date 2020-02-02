# # Question N0 1:

def fact_num(num):
    if num > 0:
        res = 1
        for i in range(1,num+1):
            res *= i
#             print(res)
        return res
num = int(input("Enter Number: "))
print(f"factorial of {num} is {fact_num(num)}\n")


# Question N0 2:

def check_alpha(alpha):
    cp = 0
    for i in range(len(alpha)):
        if alpha[i].isupper():
            cp += 1
#             print(alpha[i])
    print(f"In word '{alpha}'\n -Number of capital letter is {cp}\n -Number of small letter is {len(alpha)-cp}")
check_alpha(input("Enter Word: "))


# Question N0 3:

def show_even(list):
    even_list = []
    for num in list:
        if (num % 2) == 0:
            even_list.append(num)
    return even_list

even_num = show_even([1,4,5,2,7,5,2])
print("\nEven Number are: ", end = '')
for val in even_num:
    print(val, end = ',')
    


# Question N0 4:

def check_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
check_palindrome(input("Enter Word: "))


Question N0 5:

def isprime(num):
    ch = 0
    for i in range(2,int(num/2+1)):
        for j in range(1,10):
            if i*j == num:
                ch = 1
                break       
    if ch == 1:
        return False
    elif ch == 0:
        return True
        
num = int(input("Enter Number: "))
isprime(num)


# Question N0 6:

def shopping_items(*item):
    print("Shopping Products:")
    for val in item:
        print(f"- {val}")
               
shopping_items('Oil', 'Flour', 'Rice', 'Spices')
