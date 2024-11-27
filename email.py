import re

def main():
    email = str(input("Enter an email address: "))
    if re.search(r"\w+@\w.+\.(ac.uk|gov.uk|nhs.net)", email):
        print("Valid")
    else:
        print("Invalid")

main()
