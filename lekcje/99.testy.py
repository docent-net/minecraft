from mcpi.minecraft import Minecraft
from time import sleep
from random import randint
mc = Minecraft.create("minecraft-py.lasyk.info", 4711)


for y in range(100):
    mc.setBlock(0,y,0,35, randint(0,14))

mc.player.setPos(0,100,0)

# mc.setBlock(1,0,0, 22)
# mc.setBlock(2,0,0, 22)
# przywitanie:
# mc.postToChat('Wstawaj !')
# sleep(1)
# mc.postToChat('sniadanie')
# sleep(1)
# mc.postToChat('Czemu jeszcze spisz?!')

# poczekaj sekunde:
# sleep(1)

# twoje znane pozycje:
# poz_wioska = '65.82360752112524,-1.0,858.8716994053934'
# poz_podziemie = '-23.375359242214977,-2.0,865.9616117251703'
# poz_wyspa = '101.56125505883963,0.0,937.3434381390505'
# poz_drzewo = '-0.3808890595406922,27.0,837.5358270181052'
# poz_staw = '-8.24515447371219,20.0,793.5029418193224'
# poz_wzgorze = '102.66017128521236,31.0,765.1232361425429'

# # pokaz mi obecna pozycje:
print(mc.player.getPos())

# wycieczka:
# mc.postToChat('Czesc witaj w wiosce!')
# mc.player.setPos(poz_wioska)
# sleep(3)
#
# mc.postToChat('Czesc witaj w podziemiu!')
# mc.player.setPos(poz_podziemie)
# sleep(3)
#
# mc.postToChat('Czesc witaj na wyspie!')
# mc.player.setPos(poz_wyspa)
# sleep(3)
#
# mc.postToChat('Czesc witaj na drzewie!')
# mc.player.setPos(poz_drzewo)
# sleep(3)
#
# mc.postToChat('Czesc witaj nad stawem!')
# mc.player.setPos(poz_staw)
# sleep(3)
#
# mc.postToChat('Czesc witaj na wzgorzu!')
# mc.player.setPos(poz_wzgorze)
# sleep(3)
#
# mc.postToChat('koniec wycieczki')