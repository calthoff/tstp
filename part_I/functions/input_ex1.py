
# I shortened the message that gets printed in this example.
# The example in older versions of the book prints "How old are you?"
# I did this so the example will fit better on smaller devices.
# If you have an older version of the book, you can email
# me at cory@theselftaughtprogrammer.io 
# to update to the newest version. Thank you so much for reading!

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")
