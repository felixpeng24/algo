"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".



"""

#we start from big and go small
#use a hashmap for the remainders




def numSS(num):
    numberHash = {
        1: 'A',  2: 'B',  3: 'C',  4: 'D',  5: 'E',  6: 'F',  7: 'G',
        8: 'H',  9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
        15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
        22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }

    if num <= 26:
        return numberHash[num]
    
    while num > 0:
        dividend = num // 26
        return numSS(dividend) + numberHash[num % 26]
    
print(numSS(3799))

def number_to_column(n):
    result = ""
    while n > 0:
        n -= 1  # Adjust for 1-based indexing
        result = chr((n % 26) + ord('A')) + result
        n //= 26
    return result

print(number_to_column(3799))

def coltonum(s):
    letterHash = {
    'A': 1,  'B': 2,  'C': 3,  'D': 4,  'E': 5,  'F': 6,  'G': 7,
    'H': 8,  'I': 9,  'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    # pwr = len(s) - 1
    # res = 0
    # for letter in s:
    #     res += letterHash[letter] * (26 ** pwr)
    #     pwr -= 1
    # return res
    result = 0
    for c in s:
        result = result * 26 + letterHash[c]
    return result


print(coltonum('EPC'))
        

