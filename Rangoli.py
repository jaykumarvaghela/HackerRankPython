import string

alpha = string.ascii_lowercase
n = int(input())


def funv(size):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    print("\n".join(L[::-1] + L[1:]))


funv(n)
