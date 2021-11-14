width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
array = [list(input()) for y in range(height)]

for y in range(height):
    for x in range(width):
        if array[y][x] != "0":
            continue
        result = f"{x} {y} "

        # look for neighbour to the right
        for c in range(x + 1, width):
            if array[y][c] == "0":
                result += f"{c} {y} "
                break
        else:
            result += "-1 -1 "

        # look for neighbour down
        for c in range(y + 1, height):
            if array[c][x] == "0":
                print(f"{result} {x} {c}")
                break
        else:
            print(f"{result} -1 -1")
