# activity 4 cayaco

def is_valid(s):
    # check len (2-6 characters only)
    if not (2 <= len(s) <= 6):
        return False
    
    # check that first 2 characters are letters
    if not s[:2].isalpha():
        return False
    
    # check that all characters are alphanumeric (no punctuation)
    if not s.isalnum():
        return False
    
    # numbers must come at the end and first number cannot be '0'
    for i, c in enumerate(s):
        if c.isdigit():
            # first number cannot be '0'
            if c == '0':
                return False
            # all remaining characters must be digits
            if not s[i:].isdigit():
                return False
            break
    
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

main()