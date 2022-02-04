import time
import math
from multiprocessing import Process

def quadratic(a, b, c):

    D = b * b - 4 * a * c
    if D > 0:
        t = b * b - 4 * a * c
        t2 = math.sqrt(t)
        x1 = -(b / (2 * a)) + (t2 / (2 * a))
        x2 = -(b / (2 * a)) - (t2 / (2 * a))
        print(f'Quadratic has two numbers: {(x1, x2)}')

    elif D == 0:
        x = (-b / (2 * a))
        print(f'Quadratic has one number:  {(x)}\n')

    else:
        t = 4 * a * c - b * b
        t2 = math.sqrt(t)
        x = (-b / (2 * a))
        y = (t2 / (2 * a))
        print(f'Quadratic has two COMPLEX numbers: {(x, y)}')



if __name__ == '__main__':
 #y1 = time.time()

 quad1 = Process(target=quadratic, args=(6, 11, 35))
 quad2 = Process(target=quadratic, args=(5, -2, -9))

 quad1.start()
 quad2.start()

 quad1.join()
 quad2.join()

 # y2 = time.time()
 # print(f'Time: {y2 - y1}')









