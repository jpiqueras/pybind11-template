import py_lib
import numpy as np

py_lib.my_lib.print_package_info()

A = np.array([[2, -1], [-1, 3]])
b = np.array([1, 3])
solver = py_lib.PyLinearSystemSolver(A)
x = solver.solve(b)
print("Solution for x is: ", x)
