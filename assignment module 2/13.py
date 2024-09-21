input_string = input("Enter a string: ")

if len(input_string) < 3:
    result = input_string

elif input_string.endswith('ing'):
    result = input_string + 'ly'

else:
    result = input_string + 'ing'

print("The resulting string is:", result)
