def prec(c):
    
    if c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPostfix(s):
    st = []
    result = []

    for i in range(len(s)):
        c = s[i]

        if(c >= '0' and c <= '9'):
            result.append(c)

        elif c == '(':
            st.append('(')

        elif c == ')':
            while st[-1] != '(':
                result.append(st.pop())
            st.pop()
        else:
            while st and (prec(c) < prec(st[-1]) or prec(c) == prec(st[-1])):
                result.append(st.pop())
            st.append(c)
    while st:
        result.append(st.pop())

    return result