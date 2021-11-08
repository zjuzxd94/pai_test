#
import torch
print(torch.__version__)
import numpy as np
a=np.zeros((1,2,3))
np.save('a.npy', a)

