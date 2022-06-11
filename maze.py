from collections import deque

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
print(arr)

deq = deque()
deq.append([0,0])
x, y = deq.popleft()
arr[x][y] = 0
a = 1
'''
0 0 0
[0,0] [0,1] [0,2]
0 0 0
[1,0] [1,1] [1,2]
0 0 0
[2,0] [2,1] [2,2]
0 0 0
0 0 0
0 0 0
'''
print(len(arr))
while True:
    if arr[x][len(arr[x])-1] == 0:
        deq.append([x,y])
        x, y = deq.popleft()
        arr[x][y] = a
        a += 1
        y += 1
        print(arr, a, x, y, arr[x][len(arr[x])-1])
    elif arr[x][len(arr[x])-1] != 0 and len(arr) >= x and arr[x][0] != 0:
        x += 1
        if x % 2 == 0 or x == 1:
            y = len(arr[x])-1
        else:
            y = 0
        print(arr, a, x, y, arr[x][len(arr[x])-1])

    elif arr[x][0] == 0 and (x % 2 == 0 or x == 1):
        deq.append([x,y])
        x, y = deq.popleft()
        arr[x][y] = a
        a += 1
        y -= 1
        print(arr, a, x, y, arr[x][len(arr[x])-1])

    elif x > len(arr):
        break