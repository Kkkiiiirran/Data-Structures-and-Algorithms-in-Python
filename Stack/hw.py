# https://leetcode.com/problems/valid-parentheses/submissions/1552186732/
def isValid(s):
    stack = []
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i] =='[':
            stack.append(s[i])
        else:
            if not stack: return False
            last = stack.pop()
            if s[i]==')' and last !='(': return False
            if s[i]=='}' and last!='{': return False
            if s[i]==']' and last!='[': return False
    
    if stack: return False
    return True

s1 ="()"
s2 = "()[]{}"
s3="(]"
s4="([])"
s5="["
s6= "]"

input = ["()", "()[]{}", "(]", "([])", "[", "]"]
output = [True, True, False, True, False, False]

for i in range(6):
    if isValid(input[i])!=output[i]:
        print(f"Failed for {i+1} case")

