AllEmployment = {
    "王力宏": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

for keys in AllEmployment:
    if AllEmployment[keys]["级别"] == 1:
        AllEmployment[keys]["级别"] += 1
        AllEmployment[keys]["工资"] += 1000

print(AllEmployment)