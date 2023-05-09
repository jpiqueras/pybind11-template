import my_lib
import numpy as np

A = np.array([[2, -1], [-1, 3]])
b = np.array([1, 3])
solver = my_lib.LinearSystemSolver(A)
x = solver.solve(b)
print("Solution for x is: ", x)