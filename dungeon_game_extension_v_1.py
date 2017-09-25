# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    xd, yd = direction

    if xd == -1:
        if x == 0:
            hp -= 5
            xd = 0
        else:
            x -= 1

    if xd == 1:
        if x == 9:
            hp -= 5
            xd = 0
        else:
            x += 1

    if yd == -1:
        if y == 0:
            hp -= 5
            yd = 0
        else:
            y -= 1

    if yd == 1:
        if y == 9:
            hp -= 5
            yd = 0
        else:
            y += 1

    return x, y, hp
