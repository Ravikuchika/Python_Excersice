import numpy as np
import time
a = [1,2,3,4,5,6] * 100000
start = time.time()
b = np.array(a)
new_b = b*2
print("-----",time.time() - start)