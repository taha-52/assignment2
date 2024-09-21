str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

def swap_first_two_chars(s):
    if len(s) < 2:
        return s 
    return s[1] + s[0] + s[2:]
new_str1 = swap_first_two_chars(str1)
new_str2 = swap_first_two_chars(str2)

result = new_str1 + " " + new_str2

print("The resulting string is:", result)
