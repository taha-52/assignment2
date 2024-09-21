def extract_first_last_two(s):
    if len(s) < 2:
        return ""
    
    first_two = s[:2]
    last_two = s[-2:]
    result = first_two + last_two
    
    return result

input_string = input("Enter a string: ")
print("Result:", extract_first_last_two(input_string))
