from random import sample

first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
email = input('Please enter your email address: ')


def generate_password(first_name, last_name):
    return first_name[:2] + last_name[-2:] + "".join(sample('abcdefghijklmnopqrstuvwxyz', 5))


def print_user_details(first_name, last_name, email, password):
    
    print(first_name, last_name, email, password)


def user_password_count(password):
    if len(password) >= 7:
        return True


automatic_password = generate_password(first_name, last_name)
print("We have generated an automatic password for you: ", automatic_password)

user_reply = input('Type "Yes" if you want to use this password. Type "No" to enter your own password.')

if user_reply == "Yes":
    print_user_details(first_name, last_name, email, automatic_password)
elif user_reply =="No":
    user_new_password = input('Please your new user password = ')
    while not user_password_count(user_new_password):
        user_new_password = input("Please enter a password greater than 7 characters: ")
    print_user_details(first_name, last_name, email, user_new_password)







