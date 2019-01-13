
print("""رانگ کوتا ۴
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
    K1 = f(xi,yi)
    K2 = f(xi + h/2, yi + h/2*K1)
    K3 = f(xi + h/2, yi + h/2*K2)
    K4 = f(xi + h, yi + h*K3)
    yip1 = yi + (h/6)*(K1+2*K2+2*K3+K4)
    xi = xip1
    yi = yip1
    print("y({}) = {}".format(xi, yi))