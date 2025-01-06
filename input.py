"""
    从键盘获取输入
    语法：变量 = input()
    无论输入什么都看作字符串, 如果想得到其他类型请自行转换
"""
print("你是谁：")
name = input()
print(f"你是{name}")
# input()可打印括号中的内容
age = int(input("你几岁了？"))
print(f"你{age}岁")