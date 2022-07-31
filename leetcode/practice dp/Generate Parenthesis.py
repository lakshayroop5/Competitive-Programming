n = int(input())


def generate(u, v, b, t, x=n, output=None):
    if output is None:
        output = []
    t += b
    op = u
    cl = v
    print(t, op, cl)
    if x - op == x - cl and len(t) < 2 * x:
        generate(op - 1, cl, '(', t, x, output)

    elif x - op != x - cl and len(t) < 2 * x:
        if op > 0:
            generate(op - 1, cl, '(', t, x, output)
        if cl > 0:
            generate(op, cl - 1, ')', t, x, output)
    if len(t) == 2 * x:
        output.append(t)


out = []
generate(n - 1, n, '(', '', n, out)
print(out)
