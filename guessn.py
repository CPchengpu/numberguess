import time as tm
import random

key = 'none'
number = 0
frequency = 0
ture = 0
ture0 = 0
ture1 = 0
ture2 = 0
ture3 = 0
mangled = 0
mangled0 = 0
mangled1 = 0
mangled2 = 0
mangled3 = 0
index = "输入S以开始游戏,B以退出,H以获得帮助"


def game():
    global key
    global number
    global frequency
    global ture
    global ture0
    global ture1
    global ture2
    global ture3
    global mangled
    global mangled0
    global mangled1
    global mangled2
    global mangled3

    key = 'none'
    number = random.randint(1000, 9999)
    frequency = 8
    print (number)
    # test only
    # print(number)
    # test only

    print('游戏初始化完成!可以开始猜了。')
    for nothing in range(0, 8):
        ture = 0
        ture0 = 0
        ture1 = 0
        ture2 = 0
        ture3 = 0
        mangled = 0
        mangled0 = 0
        mangled1 = 0
        mangled2 = 0
        print('猜的次数还剩余' + str(frequency) + '次')
        key = int(input('>>>'))
        if key == number:
            if frequency == 8:
                print('老兄你真NB,一下就猜出来正确答案' + str(number) + '啊')
                tm.sleep(0.2)
                print(index)
                return

            else:
                print('你猜出来是' + str(number) + '啦')
                tm.sleep(0.2)
                print(index)
                return
        else:
            if str(key)[0] == str(number)[0]:
                ture0 = ture0 + 1
            if str(key)[1] == str(number)[1]:
                ture1 = ture1 + 1
            if str(key)[2] == str(number)[2]:
                ture2 = ture2 + 1
            if str(key)[3] == str(number)[3]:
                ture3 = ture3 + 1

            if str(key)[0] == str(number)[1]:
                mangled0 = mangled0 + 1

            if str(key)[0] == str(number)[2]:
                mangled0 = mangled0 + 1

            if str(key)[0] == str(number)[3]:
                mangled0 = mangled0 + 1

            if str(key)[1] == str(number)[0]:
                mangled1 = mangled1 + 1

            if str(key)[1] == str(number)[2]:
                mangled1 = mangled1 + 1

            if str(key)[1] == str(number)[3]:
                mangled1 = mangled1 + 1

            if str(key)[2] == str(number)[0]:
                mangled2 = mangled2 + 1

            if str(key)[2] == str(number)[1]:
                mangled2 = mangled2 + 1

            if str(key)[2] == str(number)[3]:
                mangled2 = mangled2 + 1

        ture = ture0 + ture1 + ture2 + ture3

        print(str(ture) + '正确')

        mangled = mangled0 + mangled1 + mangled2

        print(str(mangled) + '错位')

        if key < 1000 or key > 9999:
            print('Error:The number entered is too large or too small')
            print('错误：输入的数太大或太小')
            tm.sleep(0.2)
            exit(0)
        frequency = frequency - 1
        if nothing == 8:
            print("这都猜不出来？正确的答案是", str(number))
    return


print('你好，欢迎来到猜数字(Python版)')
print('Copyright(2002-2024):CPchengpu,Hongfeitang')
tm.sleep(1)
print(index)
while True:
    key = input('>>>')
    if key == 'S' or key == 's':
        game()
    else:
        if key == 'B' or key == 'b':
            key = 'none'
            exit(0)
        else:
            if key == 'H' or key == 'h':
                key = 'none'
                print('在游戏开始(输入S)时程序会随机生成一个范围在1000到9999的四位数，每局会有8次猜数字的机会，每次猜完后'
                    r'程序会给出“n正确\n错位”(n为一个可变的量,斜杠表示下一行)的提示:”n正确“是指在猜的数字中有n位是与原数相符的,'
                    '”n错位”是指在猜的数字中有n位是原数中的数字，但是位置错了。看完请重新运行程序。')
