# # and逻辑与判断两侧的值是否都为True
# print(True and True)
# print(True and  False)
# print(False and True)
# # print(False and False)
# print(8>7 and 8>7)
# print(8>7 and 2>3)
# print(2>3 and 8>7)
# print(2>3 and 2>3)
# # and具备“逻辑短路”的能力
# print(False and 3/0)
# print(3>9 and 3/0)
# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则:and会先看左边，如果左边是“假”就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那python会自动转为布尔值，然后再进行逻辑操作
# print(2-2 and True)
# print('米帅' and True)
# print( ' ' and True)
# print(7/3 and 3*4)
# # or用于判断两侧，是否至少有一个为True（只要有一个是True,那就返回true）
# print(False or True)
# print(True or False)
# print(False or True)
# print(False or False)
# or具备“逻辑短路”的能力
# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则:or会先看左边，如果左边是“真”就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那python会自动转为布尔值，然后再进行逻辑操作
# print(7-2 or False)
# print('你好' or '米帅')
# print(False or 8/2)
# print(2-2 or 3*4)
# not用于取反
# 备注：若参与not运算的值不是布尔值，那python会自动转为布尔值，然后再进行逻辑操作
print(not 0)
print(not 8-7)
print(not 7-7)