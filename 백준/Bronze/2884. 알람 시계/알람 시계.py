hour = 0
a, b = map(int, input().split())
hour = 60*a + b
hour_new = hour - 45
# h = hour_new//60
# m = hour_new%60
print(hour_new//60 if (hour_new//60) >= 0 else 23, hour_new%60)