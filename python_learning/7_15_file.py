# r 只读
# w 覆盖写入
# a 追加写入

# f = open('C:/Users/34698/Desktop/test.txt','r',encoding='UTF-8')
# print(type(f)) 

# print(f'5字节内容：{f.fr(5)}')
# print(f'全部字节内容：{f.fr()}') # 第二次read的起点是第一次read的结尾

# line1 = f.readline()
# print(type(line1))
# print(line1)

# line2 = f.readline()
# print(type(line2))
# print(line2)

# lines = f.readlines()
# print(type(lines))
# print(lines)

# for line in f:
#     print(line) 

# f.close()

# with open('C:/Users/34698/Desktop/test.txt','r',encoding='UTF-8') as f:
#     for line in f:
#         print(line)
    
# print(open('C:/Users/34698/Desktop/test.txt','r',encoding='UTF-8').fr().count('itheima'))

# fread = open('C:/Users/34698/Desktop/test.txt','r',encoding='UTF-8').fr()
# print(type(fread))
# import time

# with open('python.txt','w',encoding='UTF-8') as f:
#     f.fw('python3')
#     # time.sleep(10000)
# f.close()
# time.sleep(1000)
# f.flush()
# # f.fw('Hello world')
# # f.flush()


fr = open('bill.txt', 'r', encoding='UTF-8')
fw = open('billout.txt','w',encoding='UTF-8')
for line in fr:
    if(line.count('测试')):
        continue
    else:
        fw.write(line)
fr.close()
fw.close()

