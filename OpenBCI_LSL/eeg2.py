## Code
from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt
streams = resolve_stream('type', 'EMG')
inlet = StreamInlet(streams[0], max_buflen=1)
samples = 500
channels = 8
data = [[] for i in range(8)]
for sample in range(samples):
    for channel in range(channels):
        rec, timestamp = inlet.pull_sample()
        data[channel].append(rec[channel])
plt.plot(data[0])
plt.show()