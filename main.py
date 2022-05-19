from flattenMatrix import *
from testing import *

if __name__ == "__main__":

    try:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
        p = int(input("Enter p: "))
    except:
        print("please enter valid numbers")
        input()

    # create 3 arr
    arr3d = An3dArr(n, m, p)
    print3D(arr3d, n, m, p)

    # create 1d arr
    arr1d = eql1D(arr3d, n, m, p)

    # print 1d array
    print("1D Array")
    print(arr1d)

    # test the code
    error = Three2One_test(arr1d, arr3d, n, m, p)
    print("How many errors were there? ")
    print(error)
    wait = input()
