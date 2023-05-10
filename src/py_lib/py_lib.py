from my_lib import LinearSystemSolver
import numpy as np


class PyLinearSystemSolver(LinearSystemSolver):
    def _pretty_print_matrix(self, matrix: np.ndarray) -> str:
        row_format = "{:>15}" * matrix.shape[1]
        rows = [row_format.format(*row) for row in matrix]
        return "\n".join(rows)

    def solve(self, input_vector: np.ndarray) -> np.ndarray:
        """
        Solve the linear system and beautifully print the contents of the matrix,
        the input coefficient vector, and the solution vector.

        Args:
            input_vector (np.ndarray): The input coefficient vector as a numpy array.

        Returns:
            np.ndarray: The solution vector as a numpy array.
        """
        print("Matrix: [A]")
        # print(self._pretty_print_matrix(self.matrix))
        print("\nInput Coefficient Vector:")
        print(self._pretty_print_matrix(input_vector.reshape(-1, 1)))

        solution = super().solve(input_vector)
        print("\nSolution Vector:")
        print(self._pretty_print_matrix(solution.reshape(-1, 1)))

        return solution
