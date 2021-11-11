import math

w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
top_border, left_border, bottom_border, right_border = 0, 0, h, w


def calculate(top_border, left_border, bottom_border, right_border):
    return math.ceil((right_border + left_border) // 2), math.ceil((bottom_border + top_border) // 2)


# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir == "U":
        bottom_border, x = y0, x0
        y = (bottom_border + top_border) // 2
    elif bomb_dir == "D":
        top_border, x = y0, x0
        y = math.ceil((bottom_border + top_border) / 2)
    elif bomb_dir == "L":
        x = (right_border + left_border) // 2
        right_border, y = x0, y0
    elif bomb_dir == "R":
        x = math.ceil((right_border + left_border) / 2)
        left_border, y = x0, y0
    elif bomb_dir == "UR":
        left_border, bottom_border = x0, y0
        x, y = calculate(top_border, left_border, bottom_border, right_border)
    elif bomb_dir == "DR":
        left_border, top_border = x0, y0
        x, y = calculate(top_border, left_border, bottom_border, right_border)
    elif bomb_dir == "UL":
        right_border, bottom_border = x0, y0
        x, y = calculate(top_border, left_border, bottom_border, right_border)
    elif bomb_dir == "DL":
        right_border, top_border = x0, y0
        x, y = calculate(top_border, left_border, bottom_border, right_border)

    print(f"{x} {y}")
    x0, y0 = x, y
