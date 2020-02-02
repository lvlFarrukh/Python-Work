# Question N0 1

user = {'first_name': 'FARRUKH', 'last_name': 'ASLAM', 'age': '22', 'city': 'Karachi'}
for key, val in user.items():
    print(key,': ',val)

user['qualification'] = input("\nEnter Qualification: ")
# print()
# for key, val in user.items():
#     print(key,': ',val)

del user['qualification']
# print()
# for key, val in user.items():
#     print(key,': ',val)

    
    
# Question N0 2

city = {'Madina': {'country': 'Saudia Arabia','population': '1.1 million','fact': 't is the second holiest city in Islam, after Mecca.'} ,
        'Karachi': {'country': 'Pakistan','population': '14.91 million','fact': 'It is the Sixth largest city in the world by city population.'},
        'New york': {'country': 'Landon','population': '8.623 million','fact': 'New York City is the largest city in the United States.'}}
for key,val in city.items():
    print(f"{key} is in {val['country']}, it population is {val['population']}. The fact of {val['country']} is {val['fact']}\n")


# Question N0 3

age = int(input("Enter Age: "))
if age < 3:
    print("Ticket is free.")
elif age >= 3 and age <= 12:
    print('Prize of ticket is 10$.')
elif age > 12:
    print('Prize of ticket is 15$.')

    
# Question N0 4

def favorite_book(title):
    print(f"\nMy favorite book is {title}")

favorite_book("Deep learning With Python.")


# Question N0 5

from random import randint
r_num = randint(1,30)
for i in range(3):
    num = int(input("Enter number: "))
    
    if num == r_num:
        print("You guss number Successfully.")
        break
    elif r_num > num:
        print("input number is SMALL.")
    elif r_num < num:
        print("input number is LARGE.")
    if i == 2:
        print(f"\n The number is {r_num} better luck next time.")
