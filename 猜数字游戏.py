import time,sys
from random import*
def pr(a):
    for i in a:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)
pr('猜数字游戏')
print()
pr('请输入猜数字最小范围：')
snum = input()
pr('请输入猜数字最大范围：')
bnum = input()
num  = randint(int(snum),int(bnum))
num = str(num)
t = 0
while True:
    pr('请输入你猜的数字：')
    cnum = input()
    if cnum != num:
        if cnum > num:
            pr('猜大了')
            print()
            t = t + 1
        if cnum < num:
            pr('猜小了')
            print()
            t = t + 1
    if cnum == num:
        pr('猜对了，你猜了'+str(t)+"次")
        break
#By HYH
#2022.10.23
