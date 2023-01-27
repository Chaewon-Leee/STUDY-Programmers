import numpy as np

def solution(score):
    average = [np.average(i, axis=0) for i in score]
    sorting = sorted(average, reverse=True)
    result = [(sorting.index(i))+1 for i in average]
    return result