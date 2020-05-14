import numpy as np


def star_func():
    r = 2
    name = "entity_star"

    f = open('../drawstar.mcfunction', 'a')

    for i in range(200):
        theta = 0.02 * i * np.pi
        x = round(r * np.power(np.cos(theta), 3), 5)
        y = round(3 * np.power(np.sin(theta), 3), 5)

        mcfunc = 'execute at @e[name=' + name + '] run particle minecraft:end_rod ~' + str(x) + ' ~' + str(
            y) + ' ~ 0 0 0 0.0 1 force @p\n'

        f.write(mcfunc)

    f.close()


def roll_func():
    r = 2
    name = "entity_star"

    f = open('draw_roll.mcfunction', 'a')

    f.write("summon minecraft:armor_stand ~ ~ ~ {NoGravity:true,CustomName:\"\\\"entity_star\\\"\",Invisible:True}\n")
    for i in range(-70, 90, 1):
        theta = 0.02 * i * np.pi
        x = round(5 * np.cos(theta), 5)
        y = round(5 * np.sin(theta), 5)

        mcfunc = 'execute at @e[name=' + name + '] run tp @e[name=' + name + '] ~' + str(x) + ' ~' + str(y) + ' ~\n' \
                 + 'execute at @e[name=' + name + '] run particle minecraft:end_rod ~ ~ ~ 0 0 0 0.0 1 force @p\n'

        f.write(mcfunc)

    f.close()


def draw_circle():
    name = "entity_circle"

    f = open('../draw_circle.mcfunction', 'a')
    r = 2

    for i in range(0, 101):
        theta = i * 0.02 * np.pi

        x = round((r * np.cos(theta)), 5)
        y = round((r * np.sin(theta)), 5)

        mc_func = 'execute at @e[name=' + name + '] run ' \
                  + 'particle minecraft:end_rod ' + \
                  '~' + str(x) + ' ~ ~' + str(y) + ' 0 0 0 0.0 1 force @p\n'

        f.write(mc_func)

    f.close()


def point_to_point(dx, dy):
    name = "entity_low"

    f = open('point_to_point.mcfunction', 'a')

    r = np.abs(dy) / 2

    x1 = y1 = z1 = 0

    for i in range(dy):
        for j in range(10):
            alpha = ((i * 10 + j) / (dy * 10 - 1)) * 50 - 25
            theta_np = alpha * 0.02
            theta = theta_np * np.pi

            y = round((r + r * np.sin(theta)), 5)
            z = round((r * np.cos(theta)), 5)

            x = round((dx * (theta_np + 0.5)), 5)

            print(i, j, alpha, theta_np, x, y, z)

            tpcom = 'execute at @e[name=' + name + '] run tp @e[name=' + name + '] ~'\
                    + str(x - x1) + ' ~' + str(z - z1) + ' ~' + str(y - y1)

            next_x = j
            palce_x = 1
            if i % 2 != 0:
                next_x = 9 - j
                palce_x = -1

            mcfunc = ''
            if j != 9:
                mcfunc += 'setblock ~' + str(next_x) + ' ~ ~' + str(i) \
                          + ' minecraft:command_block[facing=down]' \
                            '{Command:\"setblock ~' + str(palce_x) + ' ~1 ~ minecraft:redstone_block\"}\n'
            else:
                mcfunc += 'setblock ~' + str(next_x) + ' ~ ~' + str(i) \
                          + ' minecraft:command_block[facing=down]' \
                            '{Command:\"setblock ~ ~1 ~1 minecraft:redstone_block\"}\n'
            mcfunc += 'setblock ~' + str(next_x) + ' ~-1 ~' + str(i) \
                      + ' minecraft:chain_command_block[facing=down]' \
                        '{Command:\"setblock ~ ~2 ~ minecraft:air\",auto:true}\n'
            mcfunc += 'setblock ~' + str(next_x) + ' ~-2 ~' + str(i) \
                      + ' minecraft:chain_command_block[facing=down]' \
                        '{Command:\"' + tpcom + '\",auto:true}\n'
            f.write(mcfunc)

            x1 = x
            y1 = y
            z1 = z


point_to_point(0, 16)
# draw_circle()
