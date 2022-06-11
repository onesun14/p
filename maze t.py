from collections import deque

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
print(arr)

deq = deque()
deq.append([0, 0])
arrows = [[0, 1], [0, -1], [1, 0], [-1, 0]]
a = 0

while True:
    if len(deq) == 0:
        break
    x, y = deq.popleft()

    for arrow in arrows:
        a_x, a_y = arrow
        print(a_x, a_y, arrow, arrows)
        b_x = a_x + x
        b_y = a_y + y
        print(b_x, b_y)
        if b_x < 3 and b_x >= 0 and b_y < 3 and b_y >= 0:
            if arr[b_x][b_y] == 0:
                deq.append([b_x, b_y])
                break
        a += 1
        arr[b_x][b_y] = a
        print(arr)