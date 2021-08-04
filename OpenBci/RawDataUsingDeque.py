from pyOpenBCI import OpenBCICyton
import time
from collections import deque
import numpy as np
import cv2

last_print = time.time()
fps_counter = deque(maxlen=50)
sequence = np.zeros((5000,8)) #100-numri i saplave #16 eshte numri i vargut (ne rastin tone i kemi vetem 8)
counter = 0

def print_raw(sample):
    global last_print
    global sequence
    global counter

    sequence = np.roll(sequence, 1,0)
    sequence[0,...] = sample.channels_data

    fps_counter.append(time.time()-last_print)
    last_print = time.time()
    print(f'FPS: {1/(sum(fps_counter)/len(fps_counter)):.2f}, : {len(sequence)},...{counter}')

    counter +=1
    if counter == 5000:
        np.save(f"seq.npy",sequence)
board = OpenBCICyton(port='COM4', daisy=False)#daisy per pllaken e dyte

board.start_stream(print_raw)