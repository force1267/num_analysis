

print("""دستور اویلر
تابع f را در دستورات برنامه تغییر دهید""")

def f(x, y):
    return x**2 + y


# input:
n = int(input("تعداد گام :"))
h = float(input("اندازه گام :"))
x0 = float(input("x0 :"))
y0 = float(input("y0 :"))

# algorithm:
xi = x0
yi = y0
for i in range(0,n):
    xip1 = xi + h
    yip1 = yi + h*f(xi,yi)
    xi = xip1
    yi = yip1
    print("y({}) = {}".format(xi, yi))