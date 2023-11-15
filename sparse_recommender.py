import numpy as np
from scipy.sparse import csr_matrix


class sparse_matrix(csr_matrix):

    def __init__(self, row, col, dtype=np.int32):
        super().__init__((row, col), dtype=dtype)
        self.initialize_sparse_matrix()
    
    def initialize_sparse_martix(self):
        self.set = 0
        self.get = {}
        self.recommend = {}
        self.add_movie = {}
        self.to_dense = {}
        pass

    def set(self, row, col, value):
        if value != 0 and 0 <= row < self.initrow and 0 <= col < self.initcol:
            sparse_matrix.setmatrix[row, col] = value
        else:
            print("error")

    def get(self, row, col):
        if 0 <= row < self.initrow and 0 <= col < self.initcol:
            return sparse_matrix.getmatrix.get[row, col, 0]
        else:
            print("error")

    def recommend(self, user_vector):
        if self.shape[1] == user_vector.shape[0]:
            recommendation_vector = csr_matrix
            ((self.shape[0], user_vector.shape[1]))
            for row_value in range(self.row):
                for col_value in range(user_vector.col):
                    result_value = 0
                    for index in range(self.col):
                        result_value = self.get(row_value, index) * user_vector.get(index, col_value)
                        recommendation_vector.set(row_value, col_value, result_value)
            return recommendation_vector
        else:
            print("col is not the same with user_vector, error")
    
    def add_movie(self, user_vector):
        if self.shape == user_vector.shape:
            recommendation_vector = csr_matrix((self.shape[0], user_vector.shape[1]))
            for row_value in range(self.row):
                for col_value in range(user_vector.col):
                    new_value = self.get_value(row_value, col_value) + user_vector.get(row_value, col_value)
                    recommendation_vector = csr_matrix(row_value, col_value, new_value)
            return recommendation_vector
        else:
            print("row is not the same with user_vector, error")
    
    def to_dense(self):
        dense_matrix = self.toarray()
        return dense_matrix

    




    




