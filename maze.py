from collections import deque
arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
queue = deque()
queue.append([1,0])#위치 정하기
x, y = queue.popleft()#부분 가져오고 지우는 것
arr[x][y] = 1
print(arr)
while