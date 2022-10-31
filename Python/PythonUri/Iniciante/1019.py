a = int(input())
hr = a // 3600
min = (a // 60) - (hr * 60)
seg = (a // 1) - (min * 60) - (hr * 3600)
print('{}:{}:{}'.format(hr, min, seg))