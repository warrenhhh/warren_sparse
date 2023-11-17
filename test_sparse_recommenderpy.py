# 在 test_sparse_recommender.py

import pytest
from sparse_recommender import sparse_matrix


def test_set():
    test_matrix = sparse_matrix(5, 5)
    test_matrix.set(1, 0, 2)
    test_matrix.set(2, 2, 5)
    test_matrix.set(0, 0, 4)

    assert test_matrix[1, 0] == 2
    assert test_matrix[2, 2] == 5


def test_recommend():
    test_recommend_matrix = sparse_matrix(5, 5)
    test_recommend_matrix.set(1, 1, 3)
    test_recommend_matrix.set(2, 2, 4)
    test_recommend_matrix.set(1, 4, 1)
    test_recommend_matrix.set(1, 1, 1)
    test_recommend_matrix.set(3, 3, 3)
    assert test_recommend_matrix[1, 1] == 1
    # using assert to check this is correct


def test_add_movie():
    test_add_movie_matrix = sparse_matrix(5, 5)
    test_add_movie_matrix.set(2, 2, 2)
    test_add_movie_matrix.set(2, 0, 2)
    test_add_movie_matrix.set(0, 0, 2)
    test_add_movie_matrix.set(1, 3, 3)
    test_add_movie_matrix.set(1, 2, 2)
    assert test_add_movie_matrix[1, 2] == 2
    # using assert to check this is correct


def test_to_dense():
    test_to_dense = sparse_matrix(5, 5)
    test_to_dense.set(1, 1, 3)
    test_to_dense.set(2, 2, 4)
    test_to_dense.set(1, 4, 1)
    test_to_dense.set(1, 1, 1)
    test_to_dense.set(3, 3, 3)
    dense_matrix = test_to_dense.to_dense()
    assert dense_matrix[1, 1] == 1
    # using assert to check this is correct


def test_sparse_matrix():
    test_matrix = sparse_matrix(5, 5)
    test_matrix.set(2, 2, 2)
    test_matrix.set(2, 0, 2)
    test_matrix.set(0, 0, 2)
    test_matrix.set(1, 3, 3)
    test_matrix.set(1, 2, 2)
    assert test_matrix[1, 2] == 2
    # using assert to check this is correct
