# https://pynative.com/python-basic-exercise-for-beginners/#h-exercise-1-calculate-the-multiplication-and-sum-of-two-numbers
# exercise 1

##number1 = int(input("number 1: "))
##number2 = int(input("number 2: "))
##
##if number1 * number2 >= 1000:
##    print(f"The result is {number1 + number2}")
##else:
##    print(f"The result is {number1 * number2}")


# exercise 2

##print("Printing current and previous number sum in a range(10)")
##
##for num in range(10):
##    print(f"Current Number {} Previous Number {} Sum: {}")

# correct

##print("Printing current and previous number sum in a range(10)")
##
##previous_num = 0  # start with 0 for the "previous" before the first loop
##for current_num in range(10):
##    sum_nums = current_num + previous_num
##    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_nums}")
##    previous_num = current_num  # update previous_num for next loop

# exercise 3

##strings = input("Original Strings are: ")
##
##print("Printing only even index chars")
##
####for string in strings:
####    print(strings[::2])
####    break
##
##for string in strings[::2]:
##    print(string)

# exercise 4

def remove_chars(word, n):
# write your code


print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'


