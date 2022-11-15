
n = int(input())
arr = map(int, input().split())
print(arr)
runner_up = arr[0]
for i in arr:
    if runner_up < i and i != max(arr):
     runner_up = i
print(runner_up)