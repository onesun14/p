#101.011 > 5.375
#0* 1/2 + ..
def float_maker(t):
    result = 0
    for i in range(len(t)):
        if t[i] == '0':
            a = 0 * (1 / (2 ** (i + 1)))
        elif t[i] == '1':
            a = 1 * (1 / (2 ** (i + 1)))
        result += a
    return result

def tmaker(num):
    a = int(num)
    b = []
    result = ''
    while a != 0 and len(b) < 23:
        a = a * 2
        if a >= 10 ** len(num):
            a -= 10 ** len(num)
            b.append(1)
        elif a < 10 ** len(num):
            b.append(0)

    for i in b:
        result += str(b[i])
    return result

print(float_maker(input()))
print(tmaker(input()))