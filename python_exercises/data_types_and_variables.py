## You have rented some movies for your kids: 
## The little mermaid (for 3 days), Brother Bear (for 5 days, they 
## love it), and Hercules (1 day, you don't know yet if they're 
## going to like it). If price for a movie per day is 3 dollars, how 
## much will you have to pay?

the_little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1

total = (the_little_mermaid_days * 3) + (brother_bear_days * 3) + (hercules_days * 3)
print(total)

## Suppose you're working as a contractor for 3 companies: 
## Google, Amazon and Facebook, they pay you a different rate per hour. 
## Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
## How much will you receive in payment for this week? 
##You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_pays = 400
google_hours_this_week = 6
amazon_pays = 380
amazon_hours_this_week = 4
facebook_pays = 350
facebook_hours_this_week = 10

this_weeks_total = (google_pays * google_hours_this_week) + (amazon_pays * amazon_hours_this_week) + (facebook_pays * facebook_hours_this_week)
print(this_weeks_total)

                # you can also run it like:

google_pays = 400
google_hours_this_week = 6
google_total = google_pays * google_hours_this_week
amazon_pays = 380
amazon_hours_this_week = 4
amazon_total = amazon_pays * amazon_hours_this_week
facebook_pays = 350
facebook_hours_this_week = 10
facebook_total = facebook_pays * facebook_hours_this_week
all_total = google_total + amazon_total + facebook_total

print(all_total)

## A student can be enrolled to a class only if the class is not full and the class schedule 
## does not conflict with her current schedule.
        #Easy way:
class_full = False
schedule_works = True
can_be_enrolled = not class_full and schedule_works
print(can_be_enrolled)

        #more difficult way
class_name_history = "History"
history_max_students = 30
students_enrolled = 25
janes_current_classes = ["Math", "English", "Science"]
can_be_enrolled = None

if ("History" in janes_current_classes) or (students_enrolled >= history_max_students):
        can_be_enrolled = False
else: 
        can_be_enrolled = True
print(can_be_enrolled)


## A product offer can be applied only if people buys more than 2 items, and the offer has not 
## expired. Premium members do not need to buy a specific amount of products.

is_premium_member = False
bought_2_or_more = True
expired_offer = False
product_offer = (is_premium_member or bought_2_or_more) and expired_offer
print(product_offer)

#Create a variable that holds a boolean value for each of the following conditions:

username = 'codeup'
password = 'notastrongpassword'

        #the password must be at least 5 characters

password_length = len(password)
password_length_accepted = password_length >= 5
print(password_length_accepted)

        #the username must be no more than 20 characters

username_length = len(username)
username_length_accepted = username_length <= 20
print(username_length_accepted)

        #the password must not be the same as the username

user_and_pass_accepted = username != password
print(user_and_pass_accepted)

        #bonus neither the username or password can start or end with whitespace

pass_doesnt_contain = password == password.strip()
user_doesnt_contain = username == username.strip()


good_user_and_pass = (password_length_accepted
                        and username_length_accepted
                        and user_and_pass_accepted
                        and pass_doesnt_contain == password == password.strip()
                        and user_doesnt_contain == username == username.strip())
good_user_and_pass
