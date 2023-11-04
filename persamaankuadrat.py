#Import module math
import math

#Input koefisien
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("Masukkan c: "))
print(f"Persamaannya adalah: {a}x^2 + ({b}x) + {c} = 0")

#Hitung diskriminan (D)
d = (b**2) - (4*a*c)

#Hitung x1 dan x2
x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print("Solusinya adalah {0} dan {1}".format(x1,x2))
