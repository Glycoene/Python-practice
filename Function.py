"""
    函数的定义
    def 函数名(函数参数):
        函数体
        return 返回值
    先定义, 再调用
    参数和返回不需要可以不写
    无返回值时会返回None(空), 在if判断中相当于False, 也可以用来定义空变量
    函数也可嵌套使用, 在函数中调用另一个函数(包括函数本身)
"""
def Add(a, b):
    return a+b

a = 2
b = 3
Type_NOreturn = print(Add(a, b))
print(Type_NOreturn, type(Type_NOreturn))