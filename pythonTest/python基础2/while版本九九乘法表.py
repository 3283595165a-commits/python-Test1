# 1. 初始化外层循环变量（行）
row = 1

while row <= 9:
    # 2. 初始化内层循环变量（列）
    # 关键：每一行开始时，列都要从 1 重新开始
    item = 1
    
    while item <= row:  # 【核心】列数不超过当前的行数，形成三角形
        print(f"{item}*{row}={item*row}", end="\t")
        item += 1  # 内层变量自增
    
    # 3. 换行
    print()
    
    # 4. 外层变量自增
    row += 1