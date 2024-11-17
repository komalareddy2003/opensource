T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().strip().split())
    points_per_test_case = A // 10
    score = points_per_test_case * B
    print(score)
