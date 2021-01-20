###1 Conditional Basics

    #a. prompt the user for a day of the week, print out whether the day is Monday or not
        #without human interaction
is_it_monday = True
if is_it_monday:
    print('It is Monday!')
else:
    print('It is not Monday yet!')

is_it_monday = False
if is_it_monday:
    print('It is Monday!')
else:
    print('It is not Monday yet!')

        #with human interaction:
weekday_selection = input("Please enter a day of the week.")
if weekday_selection.startswith("Mon"):
    print("That day is Monday")
else:
    print("This day is not Monday")
    #b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

it_the_weekend = True
if it_the_weekend:
    print('Woohoo! Its the weekend!')
else:
    print('Its not the weekend just yet!')

it_the_weekend = False
if it_the_weekend:
    print('Woohoo! Its the weekend!')
else:
    print('Its not the weekend just yet!')

        #with human interaction
if weekday_selection == "Saturday" or weekday_selection == "Sunday":
    print(f"{weekday_selection} is a weekend day!")
else:
    print(f"{weekday_selection} is not a weekend day!")

    #c create variables and make up values for
        #the number of hours worked in one week
        #the hourly rate
        #how much the week's paycheck will be
        #write the python code that calculates the weekly paycheck. You get paid time and a half 
        #if you work more than 40 hours
hours_worked_this_week = 49
hourly_rate = 10
hours_over_40 = 9
overtime_pay_rate = hourly_rate + (hourly_rate / 2)
this_weeks_pay_with_ot = (hours_worked_this_week * hourly_rate) + (hours_over_40 * overtime_pay_rate)
this_weeks_base_pay = hours_worked_this_week * hourly_rate

if hours_worked_this_week < 40:
    print(this_weeks_base_pay)
elif hours_worked_this_week > 40:
    print(this_weeks_pay_with_ot)
else:
    print('Didnt work this week')

         # easier way to do it
hours_worked = 41
if hours_worked > 40:
    overtime_hours =hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 0.5)
else:
    overtime_pay = 0
paycheck = hours_worked * hourly_rate + overtime_pay
print(paycheck)
##2 Loop Basics

    #a. While


        #2.1 Create a while loop that runs so long as i is less than or equal to 15
i = 5
while i <= 15:
    print(i)
    break
        #2.2 Each loop iteration, output the current value of i, then increment i by one.
while i <= 15:
    print(f"i: {i}")
    i += 1
        #2.3 Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each 
        #number with a new line.
n = 0
while n < 101:
    print(n)
    n += 2
        #2.4 Alter your loop to count backwards by 5's from 100 to -10.
n = 100
while n < 101 and n > 0:
    print(n)
    n -= 5
        #2.5 Create a while loop that starts at 2, and displays the number squared on each line while 
        #the number is less than 1,000,000.
n = 2
while n < 1000000:
    print(n)
    n = n ** 2
        #2.6 Write a loop that uses print to create the output shown below
n = 5
while n <= 15:
    print(n)
    n += 1
    # b. For Loops

        #2.7 Write some code that prompts the user for a number, then shows a multiplication table up 
        #through 10 for that number.
i = 7
for n in range(1, 11):
   print(i, 'x', n, '=', i * n)
        #2.8 Create a for loop that uses print to create the output shown below.

for i in range(1, 10):
    print(str(i) * i)
    ### This one prints the answer to the question

n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for i in range(1, i+1):
        print(i, end="")
    print()
    ### this one wont print the 1-22-333-4444-55555-666666-7777777-88888888-999999999, but it is
    ### important to not that by doing this it will return 1-12-123-1234-12345-123456-1234567-etc.


    # c. break and continue

        #2.9 Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to 
        #continue prompting the user if they enter invalid input. (Hint: use the isdigit method 
        #on strings to determine this). Use a loop and the continue statement to output all the 
        #odd numbers between 1 and 50, except for the number the user entered.
while True: #True is a condition which is checked before the loop runs, and if it is true the 
            #loop will run if it is false, it will not run
    odd_number_input = input('enter an odd number 1-50. ')
    if odd_number_input.isdigit():
        odd_number_input = int(odd_number_input)
        break
i = 1
while i <= 50:
    if i == odd_number_input:
        print(f"Skipping this odd number: {i}")
        i += 2
        continue
    print(f"Here is an odd number: {i}")
    i += 2

        #2.10 The input function can be used to prompt for input and use that input in your python code. 
        #Prompt the user to enter a positive number and write a loop that counts from 0 to that 
        #number. (Hints: first make sure that the value the user entered is a valid number, also 
        #note that the input function returns a string, so you'll need to convert this to a numeric 
        #type.)


        #2.11 Write a program that prompts the user for a positive integer. Next write a loop that prints 
        #out the numbers from the number the user entered down to 1.

while True:
    pos_number_input = input('enter an pos number 1-50. ')
    if pos_number_input.isdigit():
        pos_number_input = int(pos_number_input)
        if pos_number_input <= 0:
            continue
        break
for i in range(0, pos_number_input + 1):
    print(i)

while True:
    pos_number_input = input('enter an pos number 1-50. ')
    if pos_number_input.isdigit():
        pos_number_input = int(pos_number_input)
        if pos_number_input <= 0:
            continue
        break
for i in range(pos_number_input, 0, -1):
    print(i)

##3 Fizzbuzz

    #a. One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
    #Developed by Imran Ghory, the test is designed to test basic looping and conditional logic 
    #skills.

        #3.1 Write a program that prints the numbers from 1 to 100.
        #3.2 For multiples of three print "Fizz" instead of the number
        #3.3 For the multiples of five print "Buzz".
        #3.4 For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1, 101):
    if  i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    print(i)

##4 Display of table of powers

    #4.1 Prompt the user to enter an integer.

    #4.2 Display a table of squares and cubes from 1 to the value entered.
    #4.3 Ask if the user wants to continue.
    #4.4 Assume that the user will enter valid data.
    #4.5 Only continue if the user agrees to.   
int_input = int(input("enter n integer: "))
print("number | squared | cubed")
print("------ | ------- | -----")
for i in range(1, int_input + 1):
    print(f"{i} | {i**2} | {i**3}")

    #Bonus: Research python's format string specifiers to align the table

#5 Convert given number grades into letter grades.

    #5.1 Prompt the user for a numerical grade from 0 to 100.
    #5.2 Display the corresponding letter grade.
    #5.3 Prompt the user to continue.
    #5.4 Assume that the user will enter valid integers for the grades.
    #5.5 The application should only continue if the user agrees to.
    #Grade Ranges:
        #A : 100 - 88
        #B : 87 - 80
        #C : 79 - 67
        #D : 66 - 60
        #F : 59 - 0
while True:
    num_grade = int(input("enter number grade"))
    if num_grade >= 88:
        print("A")
    elif num_grade >= 80:
        print("B")
    elif num_grade >= 67:
        print("C")
    elif num_grade >= 60:
        print("D")
    else:
        print("F")
    continue_y_n = input("Would you like to continue?")
    if not continue_y_n.lower().startswith("y"):
        break
    #Bonus Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

##6 Create a list of dictionaries where each dictionary represents a book that you have read. Each 
#dictionary in the list should have the keys title, author, and genre. Loop through the list and 
#print out information about each book.
books = [
    {"title": " City of Bones", "author": " Cassandra Claire", "genre": " Fantasy"},
    {"title": " Vampire Kiss", "author": " Ella Summers", "genre": " Fantasy"},
    {"title": " Harry Potter and the Chamber of Secrets", "author": " JK Rowling", "genre": " Fantasy"},
    {"title": " Nineteen Eighty Four", "author": " Geroge Orwell", "genre": "Science Fiction"},
    {"title": " The Hitchhiker's Guide to the Galaxy", "author": " Douglas Adams", "genre": " Humour"}
]
for book in books:
    print("---")
    print("titles:{}".format(book['title']))
    print("author:{}".format(book['author']))
    print("genre:{}".format(book['genre']))

    #a. Prompt the user to enter a genre, then loop through your books list and print out the titles 
    #of all the books in that genre.
books = [
    {"title": " City of Bones", "author": " Cassandra Claire", "genre": " Fantasy"},
    {"title": " Vampire Kiss", "author": " Ella Summers", "genre": " Fantasy"},
    {"title": " Harry Potter and the Chamber of Secrets", "author": " JK Rowling", "genre": " Fantasy"},
    {"title": " Nineteen Eighty Four", "author": " Geroge Orwell", "genre": "Science Fiction"},
    {"title": " The Hitchhiker's Guide to the Galaxy", "author": " Douglas Adams", "genre": " Humour"}
]
genre_selected = input("Please choose a genre: ")
book_selected = [book for book in books if book['genre'] == genre_selected]
