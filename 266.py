"""
A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.

"""

from collections import Counter

def step_words(input_word, dictionary):
    input_count = Counter(input_word)
    input_len = len(input_word)
    result = []

    for word in dictionary:
        if len(word) != input_len + 1:
            continue
        word_count = Counter(word)

        # Check that the word has all letters from input_word
        diff = word_count - input_count
        if sum(diff.values()) == 1:  # Only one extra letter
            if input_count - word_count == Counter():
                result.append(word)

    return result

#instead of going through whole alphabet, you can jsut check if there is one extra letter