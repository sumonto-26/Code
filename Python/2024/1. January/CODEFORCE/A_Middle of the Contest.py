# DATE --> 3 January 2024
# TIME -->  6:35 - 7:30
# TIME COMPLEXITY --> 93ms 
# ACCEPTED in 2nd try
# RATING --> 1000
# my logic
a,b = list(map(int,input().split(":")))
h,m = list(map(int,input().split(":")))
minute1= a*60 + b
minute2 = h*60 + m
avarage = (minute1 + minute2)//2
hour = int(((minute1+minute2)/2)/60)
minute = int(avarage % 60)
if hour < 10:   hour = "0"+str(hour)
if minute < 10: minute = "0"+str(minute)
print(f"{hour}:{minute}")


# aljipa"s logic
# TIME COMPLEXITY --> 31ms
''' 
s, e = (input() for _ in range(2))
h1, m1 = (int(i.lstrip("0") or 0) for i in s.split(":"))
h2, m2 = (int(i.lstrip("0") or 0) for i in e.split(":"))
time = (60 * (h2 + h1) + (m2 + m1)) // 2
res = divmod(time, 60)
res = f"{res[0]:02d}:{res[1]:02d}"
print(res)'''