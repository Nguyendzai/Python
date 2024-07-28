# float
a = 1.2 
print(type(a))

# decimal lấy nhiều số hơn . float chỉ 15 số
#từ thư viện decimal -> import mọi thứ (*)
from decimal import*
# lấy bao nhiêu số
getcontext().prec = 30
print(Decimal(10)/3)

#Phân số
from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac))

#số phức (complex)
comp = complex(2,5)
print(comp)
print(comp.real)
print(comp.imag)