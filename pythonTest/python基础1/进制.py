# 0b开头表示二进制
num1 = 0b11001
# 0o表示八进制
num2=0o1034
# 0x表示十六进制
num3=0x1cf
print(num1,num2,num3)
# 使用bin()将十进制转换为二进制
result1= bin(25)
# 使用bin()将十进制转换为八进制
result2= oct(540)
# 使用bin()将十进制转换为十六进制
result3= hex(463)
# 注意bin(),oct(),hex()他们返回的都是字符串
print(result1,result2,result3)
print(type(result1,),type(result2,),type(result3,))
# 使用int()将指定进制的书，转为十进制的数字
value1=int('0b11001',2)
value2=int('0o1034',8)
value3=int('0x1cf',16)
print(value1,value2,value3)
print(type(value3),type(value2),type(value1))