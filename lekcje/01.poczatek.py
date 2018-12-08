from mcpi.minecraft import Minecraft
from lekcje.helpers import clear_world
mc = Minecraft.create("minecraft-py.lasyk.info", 4711)



clear_world(mc)

mc.player.setPos(0, 100, 0)