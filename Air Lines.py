import math 
A, B = map(int, input().split())
required_planes = (B + 99) // 100
new_planes = max(0, required_planes - A)
print(new_planes)
