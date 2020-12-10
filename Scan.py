# horizontal scan
def h_scan(points, settings, map_list):
    """
    Take the two lines of p1 and p2 as the reference line,
    and then scan the map with a vertical line.
    if p1 and p2 can be connected, return true.
    """
    column = settings.game_col
    # first image clicked
    point1_x = int(points[0].number % column)
    point1_y = int(points[0].number / column)
    # second
    point2_x = int(points[1].number % column)
    point2_y = int(points[1].number / column)

    # p1 and p2 are in the same line
    if point1_y == point2_y:
        return False

    # create two horizontal baselines
    # hLineUp: up baseline hLineDown: down baseline
    if point1_y < point2_y:
        hLineUp = point1_y
        hLineDown = point2_y
    else:
        hLineUp = point2_y
        hLineDown = point1_y

    # find left boundary

    i = point1_x
    # first scan
    while i > 0:
        # if left point is not empty
        if map_list[point1_y * column + i - 1] != 0:
            break
        # if it's empty, scan the next left point
        i -= 1
    leftBoundary = i

    # 2nd scan
    i = point2_x
    while i > 0:
        if map_list[point2_y * column + i - 1] != 0:
            break
        i -= 1

    # leftBoundary
    if i > leftBoundary:
        leftBoundary = i

    # If leftBoundary = 0, p1 and P2 have been connected
    if leftBoundary == 0:
        return True

    # rightBoundary
    i = point1_x
    while i < column - 1:
        if map_list[point1_y * column + i + 1] != 0:
            break
        i += 1
    rightBoundary = i

    i = point2_x
    while i < column - 1:
        if map_list[point2_y * column + i + 1] != 0:
            break
        i += 1

    if i < rightBoundary:
        rightBoundary = i

    # If leftBoundary = column-1 , p1 and P2 have been connected
    if rightBoundary == column - 1:
        return True

    # If the left boundary exceeds the right boundary, the connection cannot be made
    if leftBoundary > rightBoundary:
        return False
    else:
        # scan from left to right
        for i in range(leftBoundary, rightBoundary + 1):
            j = hLineUp + 1
            for j in range(hLineUp + 1, hLineDown):
                print(" j=%d" % j)
                # if there're other images between point1 and point2, can't be connected
                if map_list[j * column + i] != 0:
                    break
                j += 1
            if j == hLineDown:
                return True
        return False


# vertical scan
def v_scan(points, settings, map_list):
    """
    Take the two columns of p1 and p2 as the reference column,
    and then scan the map with a horizontal line.
    if p1 and p2 can be connected, return true.
    """

    row = settings.game_row
    column = settings.game_col
    # first image clicked
    point1_x = int(points[0].number % column)
    point1_y = int(points[0].number / column)
    # second
    point2_x = int(points[1].number % column)
    point2_y = int(points[1].number / column)

    # p1 and p2 are in the same column
    if point1_x == point2_x:
        return False

    # create two vertical baselines
    # vLineLeft: left baseline vLineRight: right baseline
    if point1_x < point2_x:
        vLineLeft = point1_x  
        vLineRight = point2_x  
    else:
        vLineLeft = point2_x
        vLineRight = point1_x

    # find up boundary
    i = point1_y
    # first scan (same as horizontal scan)
    while i > 0:
        if map_list[point1_x + (i - 1) * column] != 0:
            break
        i -= 1
    upBoundary = i

    # 2nd scan
    i = point2_y
    while i > 0:
        if map_list[point2_x + (i - 1) * column] != 0:
            break
        i -= 1

    # upBoundary
    if i > upBoundary:
        upBoundary = i

    # if upBoundary = 0，p1 and P2 have been connected
    if upBoundary == 0:
        return True

    # find down boundary
    i = point1_y
    while i < row - 1:
        if map_list[point1_x + (i + 1) * column] != 0:
            break
        i += 1
    downBoundary = i

    i = point2_y
    while i < row - 1:
        if map_list[point2_x + (i + 1) * column] != 0:
            break
        i += 1

    if i < downBoundary:
        downBoundary = i

    if downBoundary == row - 1:
        return True

    # If the up boundary exceeds the down boundary, the connection cannot be made
    if upBoundary > downBoundary:

        return False
    else:
        # scan from up to down
        for i in range(upBoundary, downBoundary + 1):
            j = vLineLeft + 1
            for j in range(vLineLeft + 1, vLineRight):
                # if there're other images between point1 and point2, can't be connected
                if map_list[i * column + j] != 0:
                    break
                j += 1
            if j == vLineRight:
                return True
        return False
