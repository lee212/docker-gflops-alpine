import sys
import datetime
import numpy as np
import resource
import os
import json

try:
    import psutil
    nopsutil = False
except:
    nopsutil = True

def compute_flops(loopcount, MAT_N):
    
    A = np.arange(MAT_N**2, dtype=np.float64).reshape(MAT_N, MAT_N)
    B = np.arange(MAT_N**2, dtype=np.float64).reshape(MAT_N, MAT_N)
    t1 = datetime.datetime.now()
    for i in range(loopcount):
        c = np.sum(np.dot(A, B))
    FLOPS = 2 *  MAT_N**3 * loopcount
    t2 = datetime.datetime.now()
    time_diff = t2 - t1
    time_diff = float("{0}.{1}".format(time_diff.seconds,
        time_diff.microseconds))
    if not nopsutil:
        mem = resource.getrusage(resource.RUSAGE_SELF)
        print (mem)
        process = psutil.Process(os.getpid())
        mi=process.memory_info()
        print mi.rss/1024.0**2
        print mi.vms/1024.0**2
        return (FLOPS / time_diff / 1e9, mem.ru_maxrss)

    return (FLOPS / time_diff / 1e9, time_diff)

if __name__ == "__main__":
    lc = 1
    mat_n = 1024
    if len(sys.argv) > 2:
        if sys.argv[1][0] == "{":
            # json input
            r = "".join(sys.argv[1:])
            r = json.loads(r)
            lc = r['number_of_loop']
            mat_n = r['number_of_matrix']
            cid = r['cid']
        else:
            lc = int(sys.argv[1])
            mat_n =  int(sys.argv[2])

    gflops, time_diff = compute_flops(lc, mat_n)
    print "{},{},{},{},{}".format(cid, lc, mat_n, gflops, time_diff)

