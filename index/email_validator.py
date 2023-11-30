import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

all_emails = [
    "user@example.com",
    "nodot@com",
    "user.name@example.co.uk",
    "missingsign.com",
]

def add_email(email):
    choice = input("\nWould you like to add your email?\n----------------------\nA: Add email\nQ: Quit\nEnter [A] or [Q]:\n")
    if choice.upper() == "Q":
        exit()
    elif choice.upper() == "A":
        pass
    else:
        print("Invalid response; please try again!")
        add_email(email)
    all_emails.append(email)
    print("\nYour email has been added!\n")

def main():
    choice = input("Welcome to Email Validator!\n----------------------\nA: Add email\nQ: Quit\nEnter [A] or [Q]:\n")
    if choice.upper() == "Q":
        exit()
    elif choice.upper() == "A":
        pass
    else:
        print("Invalid response; please try again!")
        main()
    custom_email = input("Enter your email address:\n")
    if validate_email(custom_email):
        print(f"✅{custom_email} is a valid email address")
    else:
        print(f"❌ {custom_email} is not a valid email address")
    add_email(custom_email)
    for email in all_emails:
        if validate_email(email):
            print(f"✅ {email} is a valid email address")
        else:
            print(f"❌ {email} is not a valid email address")
    print("")
    main()
    
main()