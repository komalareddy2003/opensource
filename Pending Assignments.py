a, b, c = map(int, input().split())
total_time_required = a * b
total_available_time = c * 1440
if total_time_required <= total_available_time:
    print("YES")
else:
    print("NO")
