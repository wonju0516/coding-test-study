n, m = map(int, input().split())
# * n, m을 공백으로 구분하여 입력받기 (n -> 행, m -> 열)

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # ! 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # * min(리스트): 리스트에서 가장 작은 값을 반환 (원본은 그대로)
    result = max(result, min_value)
    # * max(a, b): 두 값 중 큰 값을 반환 (max(리스트)도 가능)

print(result)
