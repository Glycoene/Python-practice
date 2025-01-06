"""
    list列表
    字面量：[元素1, 元素2, ..., 元素N]
    定义变量：列表名 = [元素1, 元素2, ..., 元素N]
    定义空列表：列表名 = [] / 列表名 = list()
    可存储不同的数据类型, 支持嵌套, 允许重复数据存在
    数据是有序存储的, 可用下标索引取出列表中的数据, 从前往后, 下标索引从0开始, 依次递增; 从后往前, 下表索引从-1开始, 依次递减
    语法：变量名[下表索引1][下表索引2]...[下表索引N]
"""
list1 = ["glycoene", 666, True]
print(list1, type(list1))

list2 = ["test", list1]
print(list2)

print(list1[0], list1[1], list1[2])
print(list1[-1], list1[-2], list1[-3])

print(list2[1][0])
"""
    列表的方法
    index查询元素的下标, 找不到则报错ValueError
    语法：列表名.index(元素)
    insert在指定的下标插入指定的元素, 之后的元素下标+1
    语法：列表名.insert(下标, 元素)
    append追加指定元素到列表的末尾
    语法：列表名.append(元素)
    extend将其他数据容器中的内容依次添加到末尾
    语法：列表名.extend(数据容器名)
    del删除列表中指定下标的元素, 之后的元素下标-1
    语法：del 列表名[下标]
    pop将列表中指定下标的元素移出并返回, 之后的元素下标-1
    语法：列表名.pop(下标)
    remove从前往后删除列表中第一个与指定元素匹配的元素
    语法：列表名.remove(元素)
    clear清空列表
    语法：列表名.clear()
    count统计指定元素在列表中的数量
    语法：列表名.count(元素)
    len统计列表中所有元素的数量
    语法：len(列表名)
"""
print(list1.index(666))

list1.insert(1, 123)
print(list1, list1.index(666))

list1.append(False)
print(list1)

list2.extend(list1)
print(list2)

del list2[1]
print(list2)

list2_0 = list2.pop(0)
print(list2, list2_0)

list3 = [1, 2, 3 ,2, 1]
list3.remove(1)
print(list3)

list3.clear()
print(list3)

print(list1.count(666))

print(len(list1))


"""
    tuple元组
    字面量：(元素1, 元素2, ..., 元素N)
    定义变量：元组名 = (元素1, 元素2, ..., 元素N)
    定义空元组：元组名 = () / 元组名 = tuple()
    与list列表相似, 不同的是, 元组在定义后不可修改(只能用index、count和len方法)
    定义单个元素的元组时需要在元素后加逗号, 否则将被定义为其他类型
    语法：元组名 = (元素, )
    可修改元组中列表的元素
"""
tuple1 = (12)
tuple2 = (12, )
print(type(tuple1), type(tuple2))

tuple3 = (1, [1, 2, 3], 2)
tuple3[1][2] = 5
print(tuple3)


"""
    string字符串
    字面量："任意数量字符"
    定义变量：字符串名 = "任意数量字符"
    字符串是字符的容器, 可容纳任意数量的字符
    可通过下表索引访问字符串中的字符
    字符串是无法修改的数据容器
"""
str1 = "glycoene"
print(str1[3])
print(str1[-5])

"""
    字符串的方法
    index查找字符串中的内容, 返回起始下标
    语法：字符串名.index(字符串)
    replace将字符串中的字符串1替换为字符串2, 返回一个新的字符串, 原字符串不会更改
    语法：字符串名.replace(字符串1, 字符串2)
    split按照指定的分隔符字符串, 将字符串划分为多个字符串, 并存入列表对象中, 原字符串不会更改
    语法：字符串名.split(分隔符字符串)
    strip返回规整字符串(依次按照传入字符串中的单个字符去除前后字符, 不传参数默认为空格), 原字符串不会更改
    语法：字符串名.strip(字符串)
    count统计字符串中指定字符串出现的次数
    语法：字符串名.count(字符串)
    len统计字符串的长度
    语法：len(字符串名)
"""
print(str1.index("ene"))

str2 = str1.replace("ene", "ENE")
print(str1, str2)

str_list = str1.split("co")
print(str1, str_list, type(str_list))

str3 = str1.strip("ge")
print(str1, str3)

str4 = "gly glyco glycoene"
print(str4.count("gly"))

print(len(str4))


"""
    序列的切片
    序列指内容连续、有序、可用下标索引的一类数据容器, 列表、元组、字符串均可视为序列
    切片指从一个序列中返回一个子序列, 原序列不会更改
    语法：序列[起始下标(不写默认从头开始):结束下标(不包含, 不写默认取到结尾):步长(不写默认为1)]
    步长可以为负数, 表示反向取, 但是起始下标和结束下标也要反向标记
"""
list_cut = [1, 2, 3, 4, 5]
print(list_cut[1:4])
print(list_cut[-1:-5:-1])

tuple_cut = (1, 2, 3, 4, 5)
print(tuple_cut[1:4])
print(tuple_cut[-1:-5:-1])

str_cut = "glycoene"
print(str_cut[1:7:2])
print(str_cut[-2:-8:-2])


"""
    set集合
    不支持元素的重复, 自带去重功能
    内容无序, 所以不支持下标访问, 但是可以修改
    字面量：{元素, 元素, ..., 元素}
    定义变量：集合名 = {元素, 元素, ..., 元素}
    定义空集合：集合名 = set()
"""
set1 = {1, 2, 3, 1, 2, 3, 1, 2, 3}
print(set1, type(set1))
"""
    集合的方法
    add将指定元素添加到集合内, 原集合会被修改
    语法：集合名.add(元素)
    remove将指定元素从集合中删除, 原集合会被修改
    语法：集合名.remove(元素)
    pop从集合中随机元素移出并返回,原集合会被修改
    语法：集合名.pop()
    clear清空集合
    语法：集合名.clear()
    difference返回两个集合的差集(集合1有且集合2没有的元素的集合), 原集合不会被修改
    语法：集合1.difference(集合2)
    difference_update对比两个集合, 在集合1内, 消除集合1和集合2中相同的元素
    语法：集合1.difference_update(集合2)
    union返回集合1和集合2组成的新集合, 原集合不会被修改
    语法：集合1.union(集合2)
    len统计集合中元素的数量
    语法：len(集合名)
"""
set1.add(4)
print(set1)

set1.remove(1)
print(set1)

var1 = set1.pop()
print(var1, set1)

set1.clear()
print(set1)

set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(set1.difference(set2))

set1.difference_update(set2)
print(set1, set2)

print(set1.union(set2), set1, set2)

print(len(set1))


"""
    dict字典
    字面量：{键(key): 值(value), 键(key): 值(value), ..., 键(key): 值(value)}
    定义变量：字典名 = {键(key): 值(value), 键(key): 值(value), ..., 键(key): 值(value)}
    定义空字典：字典名 = {} / 字典名 = dict()
    不支持键的重复, 自带去重功能, 新的值会覆盖旧的值
    只能通过键获取对应的值, 所以不能使用下标索引
    字典的键和值可以为任意数据类型(键不可为字典)
    通过for循环遍历字典时, 会将字典的每个键赋值给临时变量
"""
dict1 = {"R": 255, "G": 255, "B": 255}
print(dict1["R"])

dict2 = {
    "img1": {
        "R": 255,
        "G": 0,
        "B": 0
    },
    "img2": {
        "R": 0,
        "G": 255,
        "B": 0
    },
    "img3": {
        "R": 0,
        "G": 0,
        "B": 255
    }
}
print(dict2["img1"]["R"], dict2["img2"]["G"], dict2["img3"]["B"])
"""
    字典的方法
    新增/更新元素(如果键不存在则新增键值对, 如果键存在则更新键的值)
    语法：字典名[键] = 值
    pop将字典中指定的键和对应的值移出并返回值
    语法：字典名.pop(键)
    clear清空字典
    语法：字典名.clear()
    keys返回字典中全部的键, 类型为dict_keys, 可用于遍历字典
    语法：字典名.keys()
    len统计字典中键值对的数量
    语法：len(字典名)
"""
dict1["L"] = 255
dict1["G"] = 255
print(dict1)

var2 = dict1.pop("L")
print(dict1, var2)

dict1.clear()
print(dict1)

dict1 = {"R": 255, "G": 255, "B": 255}
dict1_keys = dict1.keys()
print(dict1_keys, type(dict1_keys))

print(len(dict2))


"""
    数据容器的通用操作
    len返回元素个数
    语法：len(数据容器名)
    max返回最大元素
    语法max(数据容器名)
    min返回最小元素
    语法：min(数据容器名)
    list返回容器转成的列表, 转字符串会将每个字符转为一个元素, 转字典时会将每个键转为一个元素
    语法：list(数据容器名)
    tuple返回容器转成的元组, 转字符串会将每个字符转为一个元素, 转字典时会将每个键转为一个元素
    语法：tuple(数据容器名)
    str返回容器转成的字符串, 转其它类型数据容器时会将字面量转为字符串
    语法：str(数据容器名)
    set返回容器转成的集合, 转序列时会使数据无序并去重, 转字典时会将每个键转为一个元素
    语法：set(数据容器名)
    sorted返回将指定容器排序后的列表(reverse的值为True时会倒序排序(从大到小), 不填默认为False, 正序排序(从小到大))
    语法：sorted(数据容器名, reverse = True/Flase)
"""