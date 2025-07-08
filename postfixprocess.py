def process(equ):
    result = ""
    ops = "-+*/"
    s = []
    for i, n in enumerate(equ):
        if n not in ops:
            try:
                s.append(float(n))
            except ValueError:
                return "ERROR"
        else:
            if n == "/":
                t = s[-2] / s[-1] 
                s.pop()
                s.pop()
                s.append(str(t))
            if n == "*":
                t = s[-1] * s[-2]
                s.pop()
                s.pop()
                s.append(str(t))
            if n == "+":
                t = s[-1] + s[-2]
                s.pop()
                s.pop()
                s.append(str(t))
            if n == "-":
                t = s[-2] - s[-1]
                s.pop()
                s.pop()
                s.append(str(t))
    return "".join(s)