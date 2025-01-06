"""
   if语句
   语法：if 条件表达式:
            N条语句
"""
age = int(input("请输入年龄:"))
if age >= 18:
    print("成年")
if age < 18:
    print("未成年")

"""
   if else语句
   语法：if 条件表达式:
            N条语句
        else:
            N条语句
"""
if age >= 18:
    print("成年")
else:
    print("未成年")

"""
   if elif else语句
   语法：if 条件判断表达式1:
            N条语句
        elif 条件判断表达式2:
            N条语句
        ......
        elif 条件判断表达式N:
            N条语句
        else:
            N条语句
   else语句可省略
"""
if age >= 60:
    print("老年")
elif age >= 35:
    print("中年")
elif age >= 18:
    print("青年")
elif age >= 12:
    print("青少年")
else:
    print("儿童")

# 从上到下进行判断, 条件一旦满足就忽略之后的判断