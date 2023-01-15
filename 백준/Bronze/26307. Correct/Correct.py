from datetime import datetime
h, m = map(int, input().split())
st = datetime(year=2022, month=1, day=1, hour=9)
end = datetime(year=2022, month=1, day=1, hour=h, minute=m)
c = end - st
print(c.seconds // 60)