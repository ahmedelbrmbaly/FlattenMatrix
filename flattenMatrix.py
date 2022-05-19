def An3dArr(n, m, p):
    """
    The function to add Items to 3d Array os ize n*m*p.

    Parameters:
        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returns:
        3d array with items from 0 to n*m*p
    """
    arr = []
    num = 0
    # add items to 3d array
    for i in range(n):
        arr.append([])

        for j in range(m):
            arr[i].append([])

            for k in range(p):
                arr[i][j].append(num)
                num += 1
    return arr


def print3D(arr, n, m, p):
    '''
    Function print 3d array

     Parameters:
        arr (List): The 3d array.
        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returns:
        Void

    '''
    print("3D Array")
    for i in range(n):
        print("New I:" + str(i))
        print()
        for j in range(m):
            print("New j:" + str(j))
            for k in range(p):
                print(arr[i][j][k], end=' ')


def eql1D(arr3d, n, m, p):
    """
    The function create 1d array an maps all 3d to 1d

    Parameters:
        arr3d (List): The 3d array.
        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returns:
        1d array with items equal to 3d arr
    """
    arr1d = []
    for i in range(n):
        for j in range(m):
            for k in range(p):
                arr1d.append(arr3d[i][j][k])

    return arr1d


def Three2One(i, j, k, n, m, p):
    '''
    Function converts from 3d arr with index[i][j][k]
    to 1d index

    Parametrs:
        i(int): index n
        j(int): index m
        k(int): index p

        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returs:
        index(int): equivelent 1d index

    '''

    index = k + j * p + i * p * m

    return index


def One2Three(index, n, m, p):
    '''
    Function converts from 1d arr[index] to  3d[i][j][k]

    Parametrs:

        index(int): equivelent 1d index
        n (int): diminsion
        m (int): diminsion
        p (int): diminsion

    Returs:
        i(int): index n
        j(int): index m
        k(int): index p


    '''

    pass


def edit1d(arr1d, i, j, k):
    '''
    Function edit equivelent item in index using 3d index i,j,k 

    Parametrs:

        arr1d(list): 1d array
        i(int): index n
        j(int): index m
        k(int): index p

    Returs:
        Void


    '''
    pass


def clear1d(arr1d, i, j, k):
    '''
    Function clear equivelent item in index using 3d index i,j,k 

    Parametrs:

        arr1d(list): 1d array
        i(int): index n
        j(int): index m
        k(int): index p

    Returs:
        Void


    '''
    pass
