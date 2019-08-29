import numpy as np
import cupy as cp
import time

test_size = 10000000

for i in range(1,2):
    # Clean variables
    x = None
    nx = None
    # Update test size
    test_size*=1
    print("=======================================")
    print("Test array size : %d" % test_size)
    # Numpy examples
    print("Numpy run time" )
    t0 = time.time()
    nx = np.arange(test_size).astype('f')
    t1 = time.time()
    els_time = t1-t0
    print("Create array : %f ms" %(els_time*1000))

    t0 = time.time()
    nx *= 5
    t1 = time.time()
    els_time = t1-t0
    print("Arithmetic   : %f ms" %(els_time*1000))

    # Cupy examples    
    print("CUPY run time")
    t0 = time.time()
    x = cp.arange(test_size).astype('f')
    t1 = time.time()
    els_time = t1-t0
    print("Create array : %f ms" %(els_time*1000))

    t0 = time.time()
    x *= 5
    t1 = time.time()
    els_time = t1-t0
    print("Arithmetic   : %f ms" %(els_time*1000))
    print("=======================================")
