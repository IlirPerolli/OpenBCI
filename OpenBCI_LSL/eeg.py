import numpy as np
from pylsl import StreamInlet, resolve_stream
import time
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque

last_print = time.time()
fps_counter = deque(maxlen=150)

#first resolve an eeg stream on the lab network
print ("looking for an eeg stream...")
streams = resolve_stream('type','EMG')
#krijo nje hyrje per te lexuar nga streami dhe merr valet EEG
inlet = StreamInlet(streams[0])

channel_data = {}

while True: #sa iterime (me mire while true)
    for i in range(8):
        sample, timestamp = inlet.pull_sample()
        if i not in channel_data:
            channel_data[i] = sample
        else:
            channel_data[i].append(sample)
    fps_counter.append(time.time() - last_print)
    last_print = time.time()
    cur_raw_hz = 1/(sum(fps_counter)/len(fps_counter))
    print (cur_raw_hz)
    time.sleep(1)

    # for chan in channel_data:
    #     plt.plot(channel_data[chan][:60])
    # plt.show()