# 定义变量语法：变量名 = 变量值
money = 50
print("有", money, "元")

# 花了10元
print("花了10元")
money = money - 10
# 等价于money -= 10

print("还有", money, "元")

# 重复花10元
time = 1
print("花了", time, "次 还剩", money - time * 10, "元")
time += 1
print("花了", time, "次 还剩", money - time * 10, "元")
time += 1
print("花了", time, "次 还剩", money - time * 10, "元")