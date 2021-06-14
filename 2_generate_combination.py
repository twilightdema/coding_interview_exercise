inp = [i for i in range(3)]

def gen_comb(s, i, out):
    if i == len(s):
        out.append(s.copy())
    else:
        gen_comb(s, i + 1, out)
        val = s[i]
        s.pop(i)
        gen_comb(s, i, out)
        s.insert(i, val)

print('Input = ' + str(inp))
outs = []
gen_comb(inp, 0, outs)
print('Output: ')
for i, out in enumerate(outs):
    print(' ' + str(i+1) + ") " + str(out))

