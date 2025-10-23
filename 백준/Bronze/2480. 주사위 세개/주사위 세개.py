a, b, c = map(int, input().split())

inp = list((a, b, c))

if len(set(inp)) == 3:
    print(sorted(inp, reverse=True)[0]*100)
elif len(set(inp)) == 2:
    print(sorted(inp)[1]*100 + 1000)
else:
    print(inp[0]*1000 + 10000)