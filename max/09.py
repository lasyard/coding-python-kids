import random

num = random.randint(1, 100)
print("我已经想好一个 1-100 之间的整数，你要猜是多少。")
i = 10
while i > 0:
    print("你只有"+str(i)+"次机会")
    guess = int(input("输你猜的数："))
    if guess < num:
        print("小了，再来一次。")
    elif guess > num:
        print("大了，再来一次。")
    else:
        print("恭喜你，猜对了！")
        break;
    i = i-1
if i == 0:
    print("很遗憾，机会用完了。")
