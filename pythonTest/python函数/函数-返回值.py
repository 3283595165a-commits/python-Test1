#函数返回值：函数执行完毕后，会把执行结果交给调用者，这个执行结果就是返回值。
#return关键字：return会结束函数执行，并把return后的值，作为函数的返回值
def add(n1,n2):
    print(f'我收到了：{n1},{n2},二者相加是{n1+n2}')
    return n1+n2
result= add(100, 200)
print(result)