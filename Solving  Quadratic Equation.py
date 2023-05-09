import math
import cmath

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
# calculate the discriminant
d = b**2 - 4*a*c

# check if the discriminant is negative
if d < 0:
    print("The equation has no real roots.")
     # calculate the roots using the quadratic formula with complex numbers
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
     # print the roots
    print("The roots are {0} and {1}".format(root1, root2))
elif d >0:
       print("The equation has two real roots.")
    # calculate the roots using the quadratic formula
       root1 = (-b + math.sqrt(d)) / (2*a)
       root2 = (-b - math.sqrt(d)) / (2*a)
        # print the roots
       print("The roots are {0} and {1}".format(root1, root2))
else:
      if(d==0):
            print("The equation has one real root")
            # calculate the roots using the quadratic formula
            root = (-b + math.sqrt(d)) / (2*a)
            # print the roots
            print("The root is {0}".format(root))



    
     
   