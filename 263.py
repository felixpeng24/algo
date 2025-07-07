"""
Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.
"""

def is_terminal(char):
    return char in '.?!‽'

def is_separator(char):
    return char in ',;:'

def is_valid_sentence(sentence):
    if not sentence:
        return False

    # Rule 1: Must start with capital letter
    if not sentence[0].isupper():
        return False

    i = 1
    n = len(sentence)

    # Rule 2: After the capital, must be lowercase or space
    if i < n and not (sentence[i].islower() or sentence[i] == ' '):
        return False

    last_char = sentence[0]
    while i < n:
        c = sentence[i]

        if c == ' ':
            # Rule 3: Only one space between words
            if last_char == ' ':
                return False
            if i + 1 < n and not sentence[i + 1].islower():
                return False
        elif is_terminal(c):
            # Rule 4: Must be no space before terminal mark
            if last_char == ' ':
                return False
            if i != n - 1:
                return False  # terminal mark must be at the end
        elif c.islower() or is_separator(c):
            pass
        else:
            return False

        last_char = c
        i += 1

    # Must end with a terminal mark
    return is_terminal(sentence[-1])

def stream_checker(stream):
    sentence = ''
    for c in stream:
        sentence += c
        if is_terminal(c):
            trimmed = sentence.strip()
            if is_valid_sentence(trimmed):
                print(trimmed)
            sentence = ''
