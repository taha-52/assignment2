def length_of_longest_word(words):
    longest_word = max(words)
    return len(longest_word)

words_list = ['apple', 'banana', 'cherry', 'watermelon']
print("Length of the longest word:", length_of_longest_word(words_list))
