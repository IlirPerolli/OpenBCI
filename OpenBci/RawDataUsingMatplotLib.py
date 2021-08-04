from matplotlib import pyplot as plt
from matplotlib import style
from collections import deque
import time
import numpy as np


style.use("ggplot")
fps_counter = deque(maxlen=50)

FPS = 105
HM_SECONDS_SLICE = 10

data = np.load("seq.npy")
print (len(data))

for i in range(FPS*HM_SECONDS_SLICE, len(data)):
    new_data = data[i-FPS*HM_SECONDS_SLICE:i]
    c8 = new_data[:, 5]

    GRAPH = c8
    print (c8)
    time.sleep(1/FPS)
    plt.plot(c8)
    plt.show()
    break