# x = 2
# y = 10
# print(x, 'minutes', 'and', y, 'seconds')

x = int(input("input seconds: "))
y = x//60
cal= x - y * 60
print(y, 'minutes', 'and', cal, 'seconds')