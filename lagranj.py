

print("""درونیابی لاگرانژ""")


points = []
n = int(input("تعداد نقاط : "))

# input:
for i in range(0,n):
    xi = float(input("x{} : ".format(i+1)))
    fi = float(input("f{} : ".format(i+1)))
    points.append( (xi, fi) )
x = float(input("x : "))

# algorithm:
p = 0
for i in range(0,n):
    xi = points[i][0]
    fi = points[i][1]
    li = 1
    for j in range(0,n):
        xj = points[j][0]
        if i is not j:
            li = li * (x - xj) / (xi - xj)
    p = p + li*fi

# output:
print("P{}({}) = {}".format(n-1, x, p))