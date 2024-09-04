# try:
#     open('abc.txt','r',encoding='UTF-8')
# except:
#     print('an error appears')
#     open('abc.txt','w',encoding='UTF-8')

# try:
#     print(name)
#     1/0
# except ZeroDivisionError as a:
#     print('零')
#     print(a)
# except NameError as b:
#     print('name')
#     print(b)

# try:
#     print(name)
#     1 / 0
# except (ZeroDivisionError,NameError) as e:
#     print('test')

# 捕获全部异常
# try:
#     print(name)
# except:
#     print('test1')

# try: 
#     print(1/0)
# except Exception as e:
#     print('error')

# try:
#     print(1)
# except ZeroDivisionError as e:
#     print('Error')
# else:
#     print('Hello world')

# try:
#     open('123.txt','r',encoding='UTF-8')
# except:
#     print('Error')
#     f = open('123.txt','w',encoding='UTF-8')
# else:
#     print('pass')
# finally:
#     print('always called')
#     f.close()