import numpy as np

def check_p01(a,b):
    if (np.abs((a-1.4)/1.4)<0.05) & (np.abs((b-0.5)/0.5)<0.05):
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
