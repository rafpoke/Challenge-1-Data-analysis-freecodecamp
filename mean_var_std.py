import numpy as np

def calculate(list):
    
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list, (3,3))

    # calculation results
    calculations = {
        'mean': [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(matrix)],
        'variance': [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix)],
        'standard deviation': [np.std(matrix, axis=1), np.std(matrix, axis=1), np.std(matrix)],
        'max': [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix)],
        'min': [np.min(matrix, axis=0), np.min(matrix, axis=0), np.min(matrix)],
        'sum': [np.sum(matrix, axis = 0), np.sum(matrix, axis = 1), np.sum(matrix)]
    }




    return calculations