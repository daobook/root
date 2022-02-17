import array, sys

N = 100000000 # 10^8


looprange = xrange if sys.hexversion < 0x3000000 else range
global_vector = array.array('i', looprange(N))
