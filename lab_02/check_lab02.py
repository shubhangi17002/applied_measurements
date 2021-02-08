import numpy as np

def check_p01(keff):
    if np.abs((keff-12560)/12560)<0.05:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
