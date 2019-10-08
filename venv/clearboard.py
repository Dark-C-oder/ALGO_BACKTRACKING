arr = [list(map(int,input().split(" "))) for i in range(4)]

print((arr[i][j] for i in range(4)) for j in range(4))
