#加密代码
# text = input('请输入密码：')
# secret=''
# for m in text:
#     secret+=chr(ord(m)+1)
# print(f'这是加密后的密码:{secret}')


#解密代码
secret=input('请输入需要解密的密码：')
text=''
for n in secret:
    text+=chr(ord(n)-1)
print(f'这是解密后的密码：{text}')