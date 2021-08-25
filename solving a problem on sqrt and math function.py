# this problem is " x^2 - 5x + 6 = 0 "
# then   x =? 
# hints   x = ((-b +- √b^2 - 4ac) / 2a)
# a = 1 ; b = -5 ; c = 6
# so we using here ((    math.sqrt()    ))
import math 
a = int(input("Input for a :- "))
b = int(input("Input for b :- "))
c = int(input("Input for c :- "))
inside_root = ((b) ** 2) - (4 *a*c)
sqrt = math.sqrt(inside_root)
x2 = 2 * a
x1 = -b + sqrt
x3 = -b - sqrt
sum1 = x1 // x2
sum2 = x3 // x2
print ("----------" + "x = " + "(" + str(sum1) + "," + str(sum2) + ")")

