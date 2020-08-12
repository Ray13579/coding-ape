# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:27:27 2020

@author: USER
"""

from mpci.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos
mc.setBlocks(x+25,y-1,z-25,1)

