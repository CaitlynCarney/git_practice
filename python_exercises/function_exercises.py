#1 Define a function named is_two. It should accept one input and return True if the passed input 
#is either the number or the string 2, False otherwise.
numbers = int(input('Please enter a number: '))
def is_two(numbers):
    if numbers == 2 or numbers == "2":
        answer = True
    else:
        answer = False
    return answer
print(is_two(numbers))

        #easier way
def is_two(x):
    return x == 2 or x == "2"

is_two(2)
#2 Define a function named is_vowel. It should return True if the passed string is a vowel, False 
#otherwise.
word = input('Please enter a word: ')
def is_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in word:
            answer = True
            return answer
        else:
            answer = False
    return answer

print(is_vowel(word))


#3 Define a function named is_consonant. It should return True if the passed string is a consonant, 
#False otherwise. Use your is_vowel function to accomplish this.

word = input('Please enter a word: ')
def is_consonant(word):
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    for con in cons:
        if con in word:
            answer = True
            return answer
        else:
            answer = False
    return answer

print(is_consonant(word))

#4 Define a function that accepts a string that is a word. The function should capitalize the 
#first letter of the word if the word starts with a consonant.
word = input('Please enter a word: ')
def capitalize_first_consonant(word):
    first_letter = word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word
print(capitalize_first_consonant(word))

#5 Define a function named calculate_tip. It should accept a tip percentage (a number between 0 
#and 1) and the bill total, and return the amount to tip.
tip_percent = float(input("Please input tip percentage (ex: 0.2 for 20%): "))
amount = int(input("Please input total for bill before tip: "))
def calculate_tip(amount):
    bill_total = (amount * tip_percent) + amount
    return bill_total
print(calculate_tip(amount))

#6 Define a function named apply_discount. It should accept a original price, and a discount 
#percentage, and return the price after the discount is applied.

discount = float(input("Please input discount percentage (ex: 0.2 for 20%): "))
total = int(input("Please input total for bill before disocunt: "))

def apply_discount(total):
    apply_dscount_to_total = (total * discount)
    bill_total = total - apply_dscount_to_total
    return bill_total
print(apply_discount(total))

#7 Define a function named handle_commas. It should accept a string that is a number that 
#contains commas in it as input, and return a number as output.
strings = input("please enter a large number with commas: ")
def handle_commas(strings):
    remove = strings.replace(",", "")
    return remove
print(handle_commas(strings))

#8 Define a function named get_letter_grade. It should accept a number and return the letter 
#grade associated with that number (A-F).
grade = int(input("enter number grade"))
def get_letter_grade(grade):
    while True:
        if grade >= 90:
            print("A")
        elif grade >= 80:
            print("B")
        elif grade >= 70:
            print("C")
        else:
            print("F")
        continue_y_n = input("Would you like to continue?")
        if not continue_y_n.lower().startswith("y"):
            break
print(get_letter_grade(grade))

#9 Define a function named remove_vowels that accepts a string and returns a string with all the 
#vowels removed.
word = input('Please enter a word: ')
def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowels:
            word = word.replace(char,'')
    return word
print(remove_vowels(word))

#10 Define a function named normalize_name. It should accept a string and return a valid python 
#identifier, that is:

    #10.1 anything that is not a valid python identifier should be removed
    #10.2 leading and trailing whitespace should be removed
    #10.3 everything should be lowercase
    #10.4 spaces should be replaced with underscores
        #for example:
        #Name will become name
        #First Name will become first_name
        #% Completed will become completed
names = input('Please enter a full name: ')
def normalize_name(names):
    names = names.lower()
    names = names.replace(" ", "_")
    return names
print(normalize_name(names))

#11 Write a function named cumulative_sum that accepts a list of numbers and returns a list that is 
#the cumulative sum of the numbers in the list.
    #cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

#cumulative sum(1:list[int]) -> list[int]
def cumulative_sum(list_of_numbers):
    sums = [list_of_numbers[0]]
    for n in list_of_numbers[1:]:
        previous_total = sums[-1]
        sums.append(previous_total + n)
    return sums
cumulative_sum(1, 2, 3)
#############Additional Exercise################
    #Once you've completed the above exercises, follow the directions 
    #from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly 
    #comment your code to explain your code.

#B1 Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm 
#and return a string that is the representation of the time in a 24-hour format. Bonus write a 
#function that does the opposite.


#Create a function named col_index. It should accept a spreadsheet column name, and return the 
#index number of the column.
    #col_index('A') returns 1
    #col_index('B') returns 2
    #col_index('AA') returns 27