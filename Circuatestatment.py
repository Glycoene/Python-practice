"""
   while语句
   语法：while 条件判断表达式:
            N条语句
"""
time = 5
i = 1
while i <= time:
    print(f"这是第{i}次循环")
    i += 1

"""
   for语句
   语法：for 临时变量 in 序列类型:
            N个语句
   按顺序遍历序列中的数据并赋值给临时变量
"""
name = "Glycoene"
for char in name:
    print(char)

"""
    range语句
    语法：range(num1, num2, step)
    获取一个从num1(可不写, 默认为0)开始到num2结束的数字序列(不包含num2), step为步长(可不写, 默认为1)
"""
for x in range(5):
    print(x)
for x in range(5, 10, 2):
    print(x)

"""
    continue语句
    中断本次循环, 直接进入下一次循环
"""
for i in range(10):
    if i == 5:
        continue
    print(i)

"""
    break语句
    直接结束循环
"""
for i in range(10):
    if i == 5:
        break
    print(i)