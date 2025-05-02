
MMIN_NUMBER:int = 1 
MMAX_NUMBER:int = 101
RRANDOM_NUMBER:int = 10
import numpy as np

number_list = np.random.randint(MMIN_NUMBER,MMAX_NUMBER,RRANDOM_NUMBER);
print(*number_list);