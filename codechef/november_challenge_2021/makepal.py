# https://www.codechef.com/NOV21C/problems/MAKEPAL

results = []

for case in range(int(input())):
    size = int(input())
    results.append(sum(int(x) % 2 != 0 for x in input().split()) // 2)

for result in results:
    print(result)
