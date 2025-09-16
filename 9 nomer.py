from math import *
a = 1.825 * 10**2
b = 18.225
c = -3.298 * 10**-2
f = abs(a**(b/a) - cbrt(b/a))
d = b - a
g = cos(b) - (c/(a-b))
w = 1 + (b-a)**2
s = f+g*(d/w)
print(round(s,5))