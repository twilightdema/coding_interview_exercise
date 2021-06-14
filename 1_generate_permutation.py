inp = [i for i in range(3)]

def gen_perm(s, i, out):
    if i == len(s) - 1:
        out.append(s.copy())
    else:
        for j in range(i, len(s)):
            s[j], s[i] = s[i], s[j]
            gen_perm(s, i+1, out)
            s[j], s[i] = s[i], s[j]

print('Input = ' + str(inp))
outs = []
gen_perm(inp, 0, outs)
print('Output: ')
for i, out in enumerate(outs):
    print(' ' + str(i+1) + ") " + str(out))
