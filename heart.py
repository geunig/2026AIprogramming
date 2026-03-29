for y in range(12):
    line = ''
    for x in range(25):
        top_left  = (x-7)**2  + (y-3)**2 < 10
        top_right = (x-17)**2 + (y-3)**2 < 10
        bottom = (y > 3) and (abs(x-12) < 12-y)

        if top_left or top_right or bottom:
            line += '+'
        else:
            line += ' '

    print(line)
