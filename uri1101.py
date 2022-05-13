while True:
    M, N = input('').split(" ")
    M = int(M)
    N = int(N)
    sum1 = sum2 = sum3 = 0
    if M == 0 or N == 0 or M < 0 or N < 0:
        break
    elif M > N:
        for i in range(N, M + 1):
            print(i, end=' ')
            sum1 += i
        print(f'Sum={sum1}')
    elif M < N:
        for j in range(M, N + 1):
            print(j, end=' ')
            sum2 += j
        print(f'Sum={sum2}')
    elif M == N and M != 0 and N != 0 and M > 0 and N > 0:
        for m in range(M, N + 1):
            print(m, end=' ')
            sum3 += m
        print(f'Sum={sum3}')
