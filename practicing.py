import numpy as np
import sys
numbers = np.arange(10, dtype=np.int64).reshape(2, 5)
numbers[1:, ::2] = -99
