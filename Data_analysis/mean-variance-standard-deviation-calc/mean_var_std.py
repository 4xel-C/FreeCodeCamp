import numpy as np

def calculate(nums):
#len checking
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = {'mean': [],
              'variance': [],
              'standard deviation': [],
              'max': [],
              'min': [],
              'sum': [],
              }
    
    #creating the matrix
    matrix = np.array(nums).reshape(3,3)
    
    #calculation part
    calculations['mean'].append(list(matrix.mean(axis=0)))
    calculations['mean'].append(list(matrix.mean(axis=1)))
    calculations['mean'].append(matrix.mean())
    
    calculations['variance'].append(list(matrix.var(axis=0)))
    calculations['variance'].append(list(matrix.var(axis=1)))
    calculations['variance'].append(matrix.var())
    
    calculations['standard deviation'].append(list(matrix.std(axis=0)))
    calculations['standard deviation'].append(list(matrix.std(axis=1)))
    calculations['standard deviation'].append(matrix.std())
    
    calculations['max'].append(list(matrix.max(axis=0)))
    calculations['max'].append(list(matrix.max(axis=1)))
    calculations['max'].append(matrix.max())
    
    calculations['min'].append(list(matrix.min(axis=0)))
    calculations['min'].append(list(matrix.min(axis=1)))
    calculations['min'].append(matrix.min())
    
    calculations['sum'].append(list(matrix.sum(axis=0)))
    calculations['sum'].append(list(matrix.sum(axis=1)))
    calculations['sum'].append(matrix.sum())

    return calculations
