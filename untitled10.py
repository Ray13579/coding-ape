import random

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()

for i in range(20):
    r = random.randrange(1,5)
if r == 1:
    mc.setBlocks(x,y,z,x+100,y,z,152)
    x = x+100
elif r == 2:
    mc.setBlocks(x,y,z,x-100,y,z,152)
    x = x-100
elif r == 3:
    mc.setBlocks(x,y,z,x,y,z+100,152)
    z = z+100
elif r == 4:
    mc.setBlocks(x,y,z,x,y,z-100,152)
    z = z-100