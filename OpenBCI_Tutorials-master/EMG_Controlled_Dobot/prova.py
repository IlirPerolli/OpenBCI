import time

import Dobot
dobot = Dobot.Dobot(100,100,0)
dobot.move(150,0,0)
dobot.move(dobot.x, dobot.y, dobot.z)
dobot.setSuction(True)
time.sleep(2)
dobot.setSuction(False)
# dobot.moveHome()