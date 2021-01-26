import numpy as np

def check_p01(w1):
    if (w1-26.603176406342666)/26.603176406342666<0.01:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points

def check_p02(w2):
    if (w2-40)/40<0.01:
        points = 2
        print('Nice work!')
        return points
    else:
        points = 0
        print('Whoops, try again')
        return points
        