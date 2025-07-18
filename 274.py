"""
Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4


"""

#start from last open parenthese, work you way out to eval

#have an eval helper function for jsut non parenthese
# -1+2-3+4 type of deal, if its negative store thatnumber by subtracting current value
#could be recurisive

def calculate(s: str) -> int:
    def helper(s, i):
        total = 0
        num = 0
        sign = 1
        
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                total += sign * num
                num = 0
                sign = 1
            elif char == '-':
                total += sign * num
                num = 0
                sign = -1
            elif char == '(':
                num, i = helper(s, i + 1)
            elif char == ')':
                total += sign * num
                return total, i
            i += 1
        
        total += sign * num
        return total, i
    
    s = s.replace(' ', '')
    result, _ = helper(s, 0)
    return result
