a, b, c = map(int, input().split())
max_mangoes = (c - b) // a
print(max(0, max_mangoes))
