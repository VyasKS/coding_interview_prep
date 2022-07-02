from abc import ABC, abstractmethod


# testing pytesseract for Unity text extraction

from PIL import Image
import pytesseract
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'venv/lib/python3.10/site-packages/pytesseract'
# Simple image to string
print(pytesseract.image_to_string(Image.open('/Users/vyasks/Desktop/tesseract_sample_test.png')))


class DenseMatrixInterface(ABC):

    @abstractmethod
    def from_dense_matrix(self, dense_matrix):
        # Functionality is abstracted at interface level and the implementation is left for the child classes
        pass


class SparseMatrix(DenseMatrixInterface):
    """ Creates sparse matrix object from input dense matrix and gives functionality such as add, subtract & display.
     Implements DenseMatrixInterface for reading dense matrix inputs. Therefore, overrides respective abstract class."""

    def __init__(self, matrix, shape):
        self.matrix = matrix
        self.shape = shape
        pass

    def from_dense_matrix(self, dense_matrix):
        """Overrides the abstract method and implements the functionality"""
        super().from_dense_matrix(dense_matrix=self.matrix)

    def add(self, matrix):
        """Add input matrix to the current matrix object and return the sum
        :param matrix List[List[int]] : The matrix to be added
        :return final_matrix (int) : Matrix sum
        """
        # Current matrix object shape
        rows = self.shape[0]
        columns = self.shape[1]
        # Shape of matrix to be added
        rows_to_add = len(matrix)
        cols_to_add = len(matrix[0])
        # Make sure size matches, else raise exception
        if rows != rows_to_add or columns != cols_to_add:
            raise Exception('Invalid matrix size. Violates matrix multiplication size rule.')

        # Create a new matrix for the matrix sum. Shape should match current matrix shape & resulting shape
        # (m x n * n x z = m x z)
        final_matrix = [([0] * cols_to_add) for i in range(rows)]

        # Element by element sum
        for i in range(rows):
            for j in range(cols_to_add):
                final_matrix[i][j] = self.matrix[i][j] + matrix[i][j]

        return final_matrix

    def subtract(self, matrix):
        """
        Subtract input matrix from current matrix object and return difference
            :param matrix : The second matrix
            :return final_matrix : Matrix difference
        """
        # Current matrix object shape
        rows = self.shape[0]
        columns = self.shape[1]
        # Shape of matrix to be added
        rows_to_subtract = len(matrix)
        cols_to_subtract = len(matrix[0])
        final_matrix = [([0] * cols_to_subtract) for i in range(rows)]
        for i in range(rows):
            for j in range(cols_to_subtract):\
                final_matrix[i][j] = self.matrix[i][j] - matrix[i][j]

        return final_matrix
