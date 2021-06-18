number_of_pair = 5
output = []

def gen(nopen, nclose, s):
    if nopen == 0 and nclose == 0:
        output.append(s)
        return
    if nopen > 0:
        gen(nopen - 1, nclose, s + '(')
    if nclose > nopen:
        gen(nopen, nclose - 1, s + ')')

gen(number_of_pair, number_of_pair, '')

for i, out in enumerate(output):
    print(' ' + str(i) + ') ' + str(out))

    