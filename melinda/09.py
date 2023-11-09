import random as r

num = r.randint(1, 100)
print('我已经想好了一个 1 到 100 之间的整数，猜猜是多少。')
i = 10
while i > 0:
    print('你只有'+str(i)+'次机会')
    guess = int(input('请输入一个数:'))
    if num > guess:
        print('太小了')
    elif num < guess:
        print('太大了')
    else:
        print('猜对了！')
        break
    i = i-1
if i == 0:
    print('失败了，数是'+str(num))
