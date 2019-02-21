#1.用python语句判断所输入的手机号，是否正确
#要对手机号的号段进行判断，
# 号段任意给出6个作为模拟号段即可.判断手机号码是否是由数字组成的
print("请输入手机号")
phone=input()
num=['131','132','133','134','135','136']
a=0
try:
    num1=int(phone)
except:
    a+=1
    print("请输入数字形式的手机号")
if a==0:
        if len(phone)==11 and phone[:3] in num:
            print("输入正确")
        else:
            print("请输入正确的手机号")


