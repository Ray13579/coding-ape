from mcpi.minecraft import Minecraft
import time
while True:
    mc = Minecraft.create()
    x,y,z, = mc.player.getTilePos()
    mc.executeCommand("weather rain")
    time.sleep(5)
    mc.executeCommand("weather clear")
    time.sleep(5)