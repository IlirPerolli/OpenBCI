from pyOpenBCI import OpenBCICyton
import openbci_stream  ## openBCIStream already imports Brainflow
import matplotlib.pyplot as plt
import pandas as pd
import time
def print_raw(sample):
    print(sample.channels_data)
## The dongle for Cyton is plugged in at the serial port
## "/dev/ttyUSB0" in the Ubuntu OS
board = OpenBCICyton(port='COM4')
board.start_stream(print_raw)
ecg = [] ## List to store ECG values
n = 250
plt.style.use("ggplot")
fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot()
fig.show()
while True:
    df_ecg = board.poll(250)  ## Polling for 250 samples
    ecg.extend(df_ecg.iloc[:, 0].values)  ## extracting ECG values
    ## Making the plot dynamic with autoscaling and x-axis shifter
    plt.autoscale(enable=True, axis="y", tight=True)
    ax.plot(ecg, color="r")
    fig.canvas.draw()
    ax.set_xlim(left=n - 250, right=n)
    n = n + 250
    time.sleep(1)  ## Updating the window in every one second
    plt.show()
    board.stop_stream()