"""
@jetou
@date : 2017/12/15
@algorithms: automaton_matcher
"""

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for i in range(0, len(Y) + 1)] for i in range(0, len(X) + 1)]
    b = [[0 for i in range(0, len(Y))] for i in range(0, len(X))]
    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = "Slope"
            elif c[i][j + 1] >= c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                b[i][j] = "Up"
            else:
                c[i+1][j+1] = c[i+1][j]
                b[i][j] = "Left"
    return c,b

def print_lcs(b, X, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j] == "Slope":
        a = print_lcs(b, X, i - 1, j - 1)
        return X[i] if a is None else a + X[i]
    elif b[i][j] == "Up":
        return print_lcs(b, X, i - 1, j)
    else:
        return print_lcs(b, X, i, j - 1)

X = "AKKSWERQ"
Y = "ASADW"
c,b = lcs_length(X,Y)
print print_lcs(b, X, len(X) - 1, len(Y) - 1)

