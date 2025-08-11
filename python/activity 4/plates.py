def is_valid(s):
    # Check length (2-6 characters)
    if not (2 <= len(s) <= 6):
        return False
    
    # Check that first 2 characters are letters
    if not s[:2].isalpha():
        return False
    
    # Check that all characters are alphanumeric (no punctuation)
    if not s.isalnum():
        return False
    
    # Check for numbers - they must come at the end and first number cannot be '0'
    for i, c in enumerate(s):
        if c.isdigit():
            # First number cannot be '0'
            if c == '0':
                return False
            # All remaining characters must be digits
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