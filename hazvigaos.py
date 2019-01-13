print("""حذفی گاوس برای تبدیل به بالا مثلثی""")


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
a = [[None for i in range(n)] for r in range(n)]
b = [None for r in range(n)]

# input:
for i in range(1,n):
    for j in range(1,n):
        a[i][j] = float(input("A({},{}) : ".format(i, j)))

for i in range(1,n):
    b[i] = float(input("b({}) : ".format(i)))


# algorithm:
stop = 0
for j in range(1, n-1):
    for i in range(j+1, n):
        if a[i][j] != 0:
            mij = a[i][j] / a[j][j]
        else:
            break
        a[i][j] = 0
        b[i] = b[i] - mij*b[j]
        for k in range(j+1, n):
            a[i][k] = a[i][k] - mij*a[j][k]

# output:
print("A = ")
matprint(a)
print("b = ")
matprint([b,b])