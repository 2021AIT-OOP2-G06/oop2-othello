import numpy as np



if __name__ == '__main__':
    list = np.zeros((8,8),dtype = int)
    list[3][3] = 1
    list[4][4] = 1
    list[3][4] = 2
    list[4][3] = 2
    while(True):
        val = input()

    print(list)