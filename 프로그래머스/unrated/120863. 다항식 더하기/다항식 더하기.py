def solution(polynomial):
    x, num = 0, 0
    res = polynomial.split(" + ")
    for i in res:
        if i.isnumeric():
            num += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    x = str(x)
    num = str(num)
    if x == "0" and num == "0":
        return "0"
    if x == "0":
        return num
    if x == "1":
        x = ""
    if num == "0":
        return x + "x"
    return x + "x + " + num