n, m, k = map(int, input().split())
# * n -> 배열의 크기, m -> 숫자가 더해지는 횟수, k -> 연속해서 k번 초과 금지

data = list(map(int, input().split()))

data.sort()  # * 입력받을 수들 정렬하기
first = data[n - 1]  # * 가장 큰 수
second = data[n - 2]  # * 두번째로 가장 큰수

result = 0

# * 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k  # * 세트(k+1개) 안에서 가장 큰 수가 더해지는 횟수
count += m % (k + 1)  # * 세트를 못 채운 나머지도 가장 큰 수


result += (count) * first
result += (m - count) * second

# while True:
#     for i in range(k):  # * 가장 큰 수를 k번 더하기
#         if m == 0:  # * m 이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1  # * 더할 때마다 1씩 빼가
#     if m == 0:  # * m이 0이라면 반복문 탈출
#         break
#     result += second
#     m -= 1

print(result)
