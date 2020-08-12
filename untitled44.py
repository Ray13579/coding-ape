from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()
def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
for i in range(10):
    plantTree (324 + i,66,450)

