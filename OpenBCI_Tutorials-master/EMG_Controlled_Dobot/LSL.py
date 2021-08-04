"""Code modified from the example program to show how to read a multi-channel time series from LSL at https://github.com/OpenBCI/OpenBCI_GUI/blob/master/Networking-Test-Kit/LSL/lslStreamTest.py."""

from pylsl import StreamInlet, resolve_stream
import Dobot
import pyautogui
import time
dobot = Dobot.Dobot(150,50,0)
# resolve an EMG stream on the lab network and notify the user
print("Duke kerkuar per streamin e EMG...")
streams = resolve_stream('type', 'EMG')
inlet = StreamInlet(streams[0])
print("Stream i EMG u gjet!")
print("Duke kerkuar per streamin e Fokusit...")
stream1 = resolve_stream('type', 'Focus')
inlet1 = StreamInlet(stream1[0])
print("Streami i Fokusit u gjet!")
# inicializo threshholdat dhe variablat per te ruajtur kohen
time_thres = 2000
prev_time = 0
blink_thres = 0.95
focus_thresh = 0.5
mode = "UP"

x = 137
y = 0
z = 0

last_x = x
last_y = y
last_z = z

modes = ['LEFT','RIGHT','FORWARD','BACKWARD', 'UP','DOWN', 'SUCTION']
count = 0
getData = False
suctionEnabled = False
while True:
    # getData = False
    if (count >6):
        count = 0
    if (x>320 or x < 160):
        x = 137
    if (y > 210 or y < -215):
        y = 0
    if (z < -68 or z > 165):
        z = 0
    sample, timestamp = inlet.pull_sample() # merr mostren e të dhenave EMG dhe vijen kohore të tyre
    print (inlet.pull_sample())
    sample1, timestamp1 = inlet1.pull_sample() # merr mostren e të dhenave Focus dhe vijen kohore të tyre
    print (inlet1.pull_sample())
    print (mode) #printo se ne cilin mod eshte programi
    print (getData)
    curr_time = int(round(time.time() * 1000)) # merre kohen me milisekonda
    if ((sample[0] >=  blink_thres) & (curr_time - time_thres > prev_time)):  # nese zbulohet nje blink dhe ka kaluar mjaft kohe qe nga pulsimi i fundit, shtypni space
        prev_time = int(round(time.time() * 1000)) # rifresko kohen
        mode = modes[count]
        count += 1

    if (sample1[0]>focus_thresh):
            if (mode == "FORWARD"):
                x+=1
            elif (mode == "BACKWARD"):
                x-=1
            elif (mode == "LEFT"):
                y+=1
            elif (mode == "RIGHT"):
                y-=1
            elif (mode == "UP"):
                z+=1
            elif (mode == "DOWN"):
                z-=1
            elif (mode == "SUCTION"):
                if (suctionEnabled):
                    dobot.move(x,y,-67) #shko merre objektin
                    dobot.setSuction(suctionEnabled) #kape
                    dobot.move(x,y,z) #leviz prap lart ku ka qene
                    suctionEnabled = False #beje gati per heren tjeter qe te fiket
                else:
                    dobot.move(x,y,-65)
                    dobot.setSuction(suctionEnabled)
                    dobot.move(x,y,z)
                    suctionEnabled = True

                # dobot.setSuction(False)
                count = 0
                mode = modes[count]



            getData = True #trego se u morren te dhenat

    elif ((getData == True) and (sample1[0]<focus_thresh)):
        if ((x > last_x+20) or (x < last_x-20) or (y > last_y+20) or (y < last_y-20) or (z>last_z+20) or (z<last_z-20)):
            dobot.move(x,y,z)
            time.sleep(3)
            getData = False
            last_x = x
            last_y = y
            last_z = z


    print ('x='+str(x),'y='+str(y),'z='+str(z))
    # pyautogui.press('space')
    # time.sleep(0.5)


