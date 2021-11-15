from sys import stdin, stdout

results = []

for case in range(int(stdin.readline())):
    array_len = stdin.readline()
    array = list(map(int, stdin.readline().split()))
    doubled = []

    if array.count(max(array)) > 1:
        stdout.write('-1\n')
        continue
    if array.count(max(array, key=array.count)) > 2:
        stdout.write('-1\n')
        continue
    if array.count(max(array, key=array.count)) == 1:
        array.sort(reverse=True)
        stdout.write(' '.join(map(str, array)) + "\n")
        continue
    for x in array:
        if array.count(x) == 2:
            doubled.extend([array.pop(array.index(x))])
    doubled.sort()
    array.sort(reverse=True)
    stdout.write(' '.join(map(str, doubled + array)) + "\n")
