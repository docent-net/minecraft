def clear_world(mc):
    for x in range(100):
        for y in range(100):
            for z in range(100):
                mc.setBlock(x, y, z, 0)

    return 0