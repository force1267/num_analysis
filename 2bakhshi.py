

print("""پیدا کردن ریشه به روش دو بخشی
تابع f را در دستورات برنامه تغییر دهید""")

def f(x):
    return x**3 + 1
# input:
print("""در بازه a تا b""")
a = float(input("a : "))
b = float(input("b : "))
e = float(input("اپسیلون :"))

# algorithm:
c = (a + b) / 2
while f(c) > e or f(c) < -e:
    if f(a)*f(c) > 0:
        a = c
    elif f(a)*f(c) < 0:
        b = c
    c = (a + b) / 2
    print("f({}) = {}".format(c, f(c)))
print("f({}) = {} ~= 0".format(c, f(c)))