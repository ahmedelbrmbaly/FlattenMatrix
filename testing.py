from flattenMatrix import *


def Three2One_test(arr1d, arr3d, n, m, p):
    '''
    Function tests that the convert is done correctly

    Parametrs :
        arr1d(list): 1d Array list
        arr3d(list): 3d array list
        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returns:
        error (int): error number

    '''
    error = 0
    num = 0
    s = 0
    for i in range(n):
        for j in range(m):
            for k in range(p):
                print("i = ", s)
                s += 1
                num = Three2One(i, j, k, n, m, p)
                print("i,j,k", i, j, k)
                print(arr3d[i][j][k])
                print("num:", num)
                print(arr1d[num])
                print("iteration: ", s)

                print(num)
                if (arr3d[i][j][k] == arr1d[num]):

                    print("ok")
                else:
                    print("error")
                    error += 1
    return error
