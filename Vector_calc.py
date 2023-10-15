
import numpy as np


def vector_len(xi, xj, xk):
    vector_length = np.sqrt((xi**2) + (xj**2) + (xk**2))
    return vector_length

# Get input values for x, y, and z
print("Length of the vector")
xi = int(input("Enter the x-component: "))
xj = int(input("Enter the y-component: "))
xk = int(input("Enter the z-component: "))

result = vector_len(xi, xj, xk)
print(result)

def l1_norm(x1i,x1j,x1k,y1i,y1j,y1k):
    l1_normie = ((x1i-y1i) + (x1j-y1j) + (x1k-y1k))
    return l1_normie

print("calculates l1 l1_norm of x1 to x2")
x1i = int(input("Enter the x-component: "))
x1j = int(input("Enter the x-component: "))
x1k = int(input("Enter the x-component: "))
y1i = int(input("Enter the x-component: "))
y1j = int(input("Enter the x-component: "))
y1k = int(input("Enter the x-component: "))

result1 = l1_norm(x1i,x1j,x1k,y1i,y1j,y1k)
print(result1)