from pyOpenBCI import OpenBCICyton
import time
def print_raw(sample):
    print(sample.channels_data)
    # time.sleep(2)

board = OpenBCICyton(port='COM4', daisy=False)#daisy per pllaken e dyte

board.start_stream(print_raw)