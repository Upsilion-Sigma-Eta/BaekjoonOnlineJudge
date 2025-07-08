T = int(input())

for test_case in range(T):
    k = (int)(input())
    n = (int)(input())

    apartment = list(list(0 for i in range(n + 1)) for j in range(k + 1))

    for i in range(n + 1):
        apartment[0][i] = i;

    for floor in range(1, k + 1, 1):
        for room in range(n + 1):
            apartment[floor][room] += apartment[floor - 1][room] + apartment[floor][room - 1]

    print(apartment[k][n])
