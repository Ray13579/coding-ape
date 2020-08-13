from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
"""
while True:
    mc.executeCommand("weather clear")
    time.sleep(5)
    mc.executeCommand("weather rain")
    time.sleep(5)
"""
import random

"""
string = "我在外層"

def func():
    string = "我在內層"
    print(string)
    
chatting()
print(string)
"""
for i in range(10):
    x,y,z = mc.player.getTilePos()
    y = y + i
    
    for j in range(10):
        r = random.randrange(0,16)
        z = z + 1
        mc.setBlock(x,y,z,r)