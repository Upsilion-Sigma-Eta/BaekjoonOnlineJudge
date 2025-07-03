n = int(input())

metal_bars = list(map(int, input().split(" ")))
metal_bars.sort()

remaining_length = sum(metal_bars)

total_cost = 0
for i in range(n - 1):
    total_cost += metal_bars[i] * (remaining_length - metal_bars[i])
    remaining_length -= metal_bars[i]

print(total_cost)