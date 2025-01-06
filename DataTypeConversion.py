# 数据类型转换语法：要转换成的数据类型(要转换的数据)
int_str = str(11)
print(type(int_str), int_str)

float_str = str(3.1415926)
print(type(float_str), float_str)

# 要将字符串转化为数字,必须要求字符串内的内容都是数字
str_int = int("12345")
print(type(str_int), str_int)

str_float = float("3.1415926")
print(type(str_float), str_float)

int_float = float(123)# 在数字后加.0
print(type(int_float), int_float)

float_int = int(3.14)# 将小数点后所有数字去除
print(type(float_int), float_int)