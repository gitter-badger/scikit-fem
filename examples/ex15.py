"""
Author: kinnala

One-dimensional adaptation of example 1.
"""
import numpy as np
from skfem import *

m = MeshLine(np.linspace(0, 1, 10))

e = ElementLineP1()
basis = InteriorBasis(m, e)

@bilinear_form
def laplace(u, du, v, dv, w):
    return du[0]*dv[0]

@linear_form
def load(v, dv, w):
    return 1.0*v

A = asm(laplace, basis)
b = asm(load, basis)

I = m.interior_nodes()

x = 0*b
x[I] = solve(*condense(A, b, I=I))

if __name__ == "__main__":
    m.plot(x)
    m.show()
