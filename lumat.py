

print("""تچزیه LU""")


def matprint(mat, start = 1):
    m = len(mat)
    n = len(mat[0])
    s = ""
    for i in range(start, m):
        for j in range(start, n):
            s += str(mat[i][j]) + "\t"
        s += "\n"
    print(s)


n = int(input("سایز ماتریس : ")) + 1



# 2d n*n matrices :
a = [[0 for i in range(n)] for r in range(n)]
l = [[0 for i in range(n)] for r in range(n)]
u = [[0 for i in range(n)] for r in range(n)]

# input:
for i in range(1,n):
    for s in range(1,n):
        a[i][s] = float(input("A({},{}) : ".format(i, s)))
        l[i][s] = u[i][s] = 0
    l[i][i] = 1 # doolittle

# algorithm:
for k in range(1,n):
    for i in range(k,n):
        sigma = 0
        for s in range(1,k-1):
            sigma += l[k][s]*u[s][i]
        u[k][i] = a[k][i] - sigma
    for i in range(k+1,n):
        sigma = 0
        for s in range(1,k-1):
            sigma += l[i][s]*u[s][k]
        l[i][k] = (a[i][k]-sigma)/u[k][k]
    l[k][k] = 0 # doolittle

# output:
print("A = ")
matprint(a)
print("L = ")
matprint(l)
print("U = ")
matprint(u)
