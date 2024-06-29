from validator_collection import validators

try:
    email_address = validators.email(input("What's your email address? "), allow_empty = True)
    print("Valid")
except:
    print("Invalid")
