timestr = input("请输入时间hh:mm:ss")
times = timestr.split(":")
hh = int(times[0])
mm = int(times[1])
ss = int(times[2])
if ss == 59:
    mm += 1
    ss = 0
    if mm == 60:
        hh += 1
        mm = 0
        if hh == 24:
            hh = 0
print("%.2d:%.2d:%.2d"%(hh,mm,ss))
timestr.splitlines()
