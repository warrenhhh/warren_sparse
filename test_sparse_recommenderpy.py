# csr_matrix
# create a test sparse matrix

import pytest
from sparse_recommender import sparse_matrix



def test_set():
    test_matrix = sparse_matrix(5, 5)
    test_matrix.set(1, 0, 2)
    test_matrix.set(2, 2, 5)
    test_matrix.set(0, 0, 4)

    assert test_matrix.get(1, 0) == 2
    assert test_matrix.get(2, 2) == 5

def test_recommend():
    test_recommend_matrix = sparse_matrix(5,5)
    test_recommend_matrix.set(1, 1, 3)
    test_recommend_matrix.set(2, 2, 4)
    test_recommend_matrix.set(1, 5, 1)
    test_recommend_matrix.set(1, 1, 1)
    test_recommend_matrix.set(3, 3 ,3)
    test_recommend_matrix.get(1, 1, 1)

def test_add_movie():
    test_add_movie_matrix = sparse_matrix(5, 5)
    test_add_movie_matrix.set(2, 2, 2)
    test_add_movie_matrix.set(2, 0, 2)
    test_add_movie_matrix.set(0, 0, 2)
    test_add_movie_matrix.set(1, 3, 3)
    test_add_movie_matrix.set(1, 2, 2)

def test_to_dense():
    test_to_dense = sparse_matrix(5, 5)
    test_to_dense.set(1, 1, 3)
    test_to_dense.set(2, 2, 4)
    test_to_dense.set(1, 5, 1)
    test_to_dense.set(1, 1, 1)
    test_to_dense.set(3, 3 ,3)
    test_to_dense.get(1, 1, 1)

def test_sparse_matrix():
    test_matrix = sparse_matrix(5, 5)
    test_matrix.set(2, 2, 2)
    test_matrix.set(2, 0, 2)
    test_matrix.set(0, 0, 2)
    test_matrix.set(1, 3, 3)
    test_matrix.set(1, 2, 2)
