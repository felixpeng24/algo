"""
Problem Statement:

Given a string s of '(', ')', and lowercase English characters, 
remove the minimum number of parentheses to make the input string valid. Return any valid string.

A string is valid if:

Open brackets are closed by the same type of brackets.

Open brackets are closed in the correct order.

Example:
python
Copy
Edit
Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""


-------------


Given a string of parentheses, find the balanced string that can be produced
 from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
"""

#stack, add ( onto stack, pop if ), if theres any left over or there isnt a ) left, then not balanced


# if there are ( left over, we insert )
# if we run out, we add ( in front? idk why this is hard

def balanceParentheses(s):
    res = []
    open_count = 0

    for c in s:
        if c == '(':
            res.append(c)
            open_count += 1
        elif c == ')':
            if open_count > 0:
                res.append(c)
                open_count -= 1
            else:
                # Insert matching '(' before ')'
                res.insert(0, '(')
                res.append(c)
        else:
            res.append(c)  # Shouldn't happen in valid input

    # Add remaining ')' for unmatched '('
    res.extend(')' * open_count)

    return ''.join(res)
