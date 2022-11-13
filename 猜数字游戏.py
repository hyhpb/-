import time,sys,os
from random import*
def pr(a):
    for i in a:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)
pr('请输入猜数字的最小范围：')
small = int(input())
pr('请输入猜数字的最大范围：')
big = int(input())
num = randint(small,big)
t = 0
while True:
    pr('请输入你猜的数字：')
    gnum = int(input())
    if gnum == num:
        t += 1
        pr('猜对了，你猜了'+str(t)+'次')
        break
    if gnum < num:
        t += 1
        pr('猜小了')
        time.sleep(1)
        os.system('cls')
    if gnum > num:
        t +=1
        pr('猜大了')
        time.sleep(1)
        os.system('cls')
#2022/11/13
#by hyh
#版本号：1.5
