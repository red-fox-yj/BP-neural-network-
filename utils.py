from constant import gift_list
import numpy as np


def code_to_word(data):
    """将编号转化为标签"""
    n_row = data.shape[0]
    n_col = data.shape[1]
    words = np.empty(shape=(n_row, n_col), dtype=object)
    for i in range(n_row):
        for j in range(n_col):
            if data[i][j] == 1:
                words[i][j] = gift_list[j]
    return words
