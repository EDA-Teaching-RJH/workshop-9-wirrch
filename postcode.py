import re

def main():
    address = "University of Kent, Canterbury, Kent, CT2 7NT"
    postcode = address.split(", ")[3]
    print(postcode)
    if re.search(r"^\w{2,3}\s{1}\w{2,3}$", postcode):
        print("Valid")
    else:
        print("Invalid")

main()
