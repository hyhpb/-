import time,os
from random import*
def pr(a, enter: bool = False):
    for i in a:
        print(i,end="")
        time.sleep(0.08)
    if enter:
        print()
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
        pr('猜对了，你猜了'+str(t)+'次', True)
        break
    if gnum < num:
        t += 1
        pr('猜小了', True)
        time.sleep(1)
        os.system('cls')
    if gnum > num:
        t +=1
        pr('猜大了', True)
        time.sleep(1)
        os.system('cls')
#2022/11/13
#by hyh,ikun-lychee
#版本号：1.6
