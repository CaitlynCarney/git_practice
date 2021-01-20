#1. Import and test 3 of the functions from your functions exercise file.
    #Import each function in a different way:
        #import the module and refer to the function with the . syntax
import math
math.sqrt(81)
        #use from to import the function directly
from math import sqrt
print(sqrt(16))
        #use from and give the function a different name
from math import sqrt as sr
print(sr(36))


#2 For the following exercises, read about and use the itertools module from the standard library 
#to help you solve the problem.
    #2.1 How many different ways can you combine the letters from "abc" with the numbers 1, 2, 
    #and 3?
import itertools
letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']
all = letters + numbers

for r in range(1, 3):
    for s in itertools.product(all, repeat=r):
         print(''.join(s))
    #2.2 How many different ways can you combine two of the letters from "abcd"?
import itertools
letters = ['a', 'b', 'c', 'd']

for r in range(2, 3):
    for s in itertools.product(letters, repeat=r):
         print(''.join(s))
            #13 ways

#3 Save this file as profiles.json inside of your exercises directory. Use the load function from the 
#json module to open this file, it will produce a list of dictionaries. Using this data, write some 
#code that calculates and outputs the following information:
import json
profile = open("profiles.json")
json.load(profile)
    #3.1 Total number of users
total_users = len(list_profiles)
total_users
    #3.2 Number of active users
active_user = [i["_id"] for i in list_profiles if i["isActive"] == True]
num_active = len(active_user)
print(num_active)
            #creating a temporary variable i
            #so for each '_id' is another usernso we run through each one and where isActive = True it gets gounter
            #but if false it is not going to count
            #len(active_users) will then count all the active users and produce the answer

    #3.3 Number of inactive users
inactive_user = [i["_id"] for i in list_profiles if i["isActive"] == False]
num_inactive = len(inactive_user)
print(num_inactive)
    #3.4 Grand total of balances for all users
user_balance = [i["balance"] for i in list_profiles]
float_balance = []
for balance in user_balance:
    balance = balance.replace("$", "")
    balance = balance.replace(",", "")
    balance = float(balance)
    float_balance.append(balance)
total_balance = sum(float_balance)
print(total_balance)
    #3.5 Average balance per user
import statistics as stats
stats.mean(float_balance)
    #3.6 User with the lowest balance
min(float_balance)
    #3.7 User with the highest balance
max(float_balance
    #3.8 Most common favorite fruit
fav_fruit = [i["favoriteFruit"] for i in list_profiles]
types_of_fruits = set(fav_fruit)
print(types_of_fruits) # {'apple', 'banana', 'strawberry'}
table = [
    {"fav_fruit": "apple", "frequency": 0},
    {"fav_fruit": "banana","frequency": 0},
    {"fav_fruit": "strawberry","frequency": 0}
]
for fruit in fav_fruit:
    if fruit == "apple":
        table[0]["frequency"] += 1
    if fruit == "banana":
        table[1]["frequency"] += 1
    if fruit == "strawberry":
        table[2]["frequency"] += 1
table = sorted(table, key = lambda i: i["frequency"])

print("Most common favorite fruit:", table[2]["fav_fruit"])
    #3.9 Least most common favorite fruit
print("Least common favorite fruit:", table[0]["fav_fruit"])
    #3.10 Total number of unread messages for all users
list_of_greetings = [i["greeting"] for i in list_profiles]
unread_messages = []
for greeting in list_of_greetings:
    unread_messages += [int(i) for i in greeting.split() if i.isdigit()]

total_number_of_unread = sum(unread_messages)
print(total_number_of_unread)