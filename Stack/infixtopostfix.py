# https://www.geeksforgeeks.org/problems/infix-to-postfix-1587115620/1
# 
def InfixtoPostfix( s):
    def check(op):
        if op=='^': return 3
        elif op=='*' or op=='/': return 2
        elif op=='+' or op=='-': return 1
        else: return 0
        
    stack =[]
    ans = ""
    for i in range(len(s)):
        if '0'<=s[i]<='9' or 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
            ans+=s[i]
        elif s[i]=='(':
            stack.append('(')
        elif s[i]==')':
            while stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
            
        else:
            prec = check(s[i])
            
            while stack and prec<=check(stack[-1]):
                ans+=stack.pop()
            stack.append(s[i])
    while stack: ans+=stack.pop()
    return ans
string = "a+b*(c^d-e)^(f+g*h)-i"