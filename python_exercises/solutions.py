#############################################Python Assessment
#######################Instructions
        ##Carefully read through the instructions and problems before beginning work.

        ##Do your work in a file named solutions.py. It does not matter where this file is on your 
        #computer, but keep track of the location so that you can turn it in.

        ##When the time is up, upload your solutions.py file to Google Classroom.

#######################Grading
        ##Your assessment will be graded based on the examples given.

        ##One point will be awarded for each problem that is correctly solved.

        ##Each problem includes sample output from an interactive Python session (i.e. running 
        #the python command from your terminal). If the examples for each problem can be run, 
        #and the correct output produced, you will receive credit for the problem.

        ##No partial credit will be awarded, and no credit is given if the function is misnamed, or 
        #if the function does not run (i.e. it produces an error when we try to run it).

#######################Problems

#1 Write a function named isnegative. It should accept a number and return a boolean value based on 
#whether the input is negative.

number = int(input("Please enter a number (negative or positive): "))
def isnegative(number):
    if number < 0:
        answer = True
    else:
        answer = False
    return answer
print(isnegative(number))

#2 Write a function named count_evens. It should accept a list and return the number of even 
#numbers in the list.

numbers = [4, 5, 8, 10, 12]
def count_evens(numbers):
    for num in numbers:
        if num % 2 == 0: 
           print(num, end = " ") 

print(count_evens(numbers))

#3 Write a function named increment_odds. It should accept a list of numbers and return a new 
#list with the odd numbers from the original list incremented.

numbers = [4, 5, 8, 10, 12]
def increment_odds(numbers):
    for num in numbers:
        if num % 2 != 0: 
           print(num, end = " ") 

print(increment_odds(numbers))

#4 Write a function named average. It should accept a list of numbers and return the mean of the 
#numbers.

def average(numbers):
    return sum(numbers) / len(numbers)
numbers = [4, 6, 8, 10, 12]
print(average(numbers))

#5 Create a function named name_to_dict. It should accept a string that is a first name and last 
#name separated by a space, and return a dictionary with first_name and last_name keys.

def name_to_dict(name):
    first, last = name.split()
    print("first_name = {first}".format(first=first))
    return("last_name = {last}".format(last=last))
print(name_to_dict(name))

#6 Write a function named capitalize_names. It should accept a list of dictionaries where each 
#dictionary represents a person and has keys first_name and last_name. It should return a list 
#of dictionaries with each person's name capitalized.

names = {'first_name': "Caitlyn", 'last_name': "Carney"}
def capitalize_names(d):
   new_dict = dict((k.upper(), v.upper()) for k, v in d.items())
   return new_dict
print(capitalize_names(names))

#7 Write a function named count_vowels. It should accept a word and return a number that is the 
#number of vowels in the given word. "y" should not count as a vowel.

word = input('Please enter a word: ')
def count_vowels(word):
    count = 0
    vowel = "aeiouAEIOU"
    for letter in word: 
        if letter in vowel: 
            count = count + 1
    return(count) 
    
print(count_vowels(word))

#8 Write a function named analyze_word. It should accept a string that is a word and return a 
#dictionary with information about the word: the total number of characters in the word, the 
#original word, and the number of vowels in the word.

def analyze_word(word):
    def count_characters(word):
        count_letters = len(word)
        print(count_letters)
    def count_vowels(word):
        count = 0
        vowel = "aeiouAEIOU"
        for letter in word: 
            if letter in vowel: 
                count = count + 1
        print(count) 
    dictionary = {'num_of_characters': count_characters(word), 'original_word': word, 
                         'vowel_count': count_vowels}
    return dictionary

print(analyze_word(word))

#######################Hints
        ##When a problem says return, it means return, not print.

        ##When a problem says that a function will take in an input, then it means the function 
        #must be defined so that it takes in an argument as its input, rather than relying on 
        #variables defined outside the function.

        ##Points will only be awarded for a complete, correct function. This means it is better 
        #to have one completed function, rather than 8 half-finished ones.

        ##Run your code frequently to check for syntax errors.

        ##You can check to see if a problem is correct by running python on your command line and 
        #testing the examples given.