# https://www.codechef.com/NOV21C/problems/CHEAPFUEL

results = []

for case in range(int(input())):
    petrol, diesel, petrol_inc, diesel_inc, months = map(int, input().split())
    if petrol + petrol_inc * months < diesel + diesel_inc * months:
        results.append("PETROL")
    elif petrol + petrol_inc * months > diesel + diesel_inc * months:
        results.append("DIESEL")
    else:
        results.append("SAME PRICE")

for result in results:
    print(result)
