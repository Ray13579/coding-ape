from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()



#x,y,z = mc.player.getT1lePos()

wallet_a = random.randrange(0,10)
wallet_b = random.randrange(0,10)

if wallet_a == 4 or wallet_a == 8:
    print("4 or 8")
    
total = wallet_a + wallet_b

if total>10:
    print("Yes")

print(wallet_a)
print(wallet_b)    

try:    
    blockType = int(input("BLock id:"))
    print("vaLid")
except:
    print("InvaLid")