#随机生成一个包含1000个字母的字符串，
# 然后统计该字符串中每个字母的数量，
# 并输出结果（要求结果以字典方式存储）
import random
str="abcdefg"
str1=""
d={}
for i in range(1000):
    str1+=random.choice(str)
for i in str:
    d[i] = str1.count(i)
print(d)