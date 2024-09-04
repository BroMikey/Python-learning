## 字符串操作

|      名称      |               功能                | 备注           |
| :------------: | :-------------------------------: | -------------- |
|      [i]       |                                   |                |
|     [i:j]      |                                   |                |
|    [i:j:k]     |                                   |                |
|    format()    |                                   |                |
|  capitalize()  |          第一个字母大写           |                |
|    count()     |         返回某字串的个数          |                |
|   endswith()   |       是否以某一字符串结尾        |                |
|  startwith()   |              ……开始               |                |
|  expandtabs()  |         将Tabs替换为展开          |                |
|     find()     |       该字符串的第一个索引        |                |
|    rfind()     |      从后往前第一个出现索引       |                |
|    index()     |          字串的最小索引           |                |
|    rindex()    |             最大索引              |                |
|   isalnum()    | 是否只有字母和数字(空格也为False) |                |
|   isalpha()    |           是否是纯字母            |                |
|  isdecimal()   |        是否是纯十进位数字         |                |
|   isdigit()    |           是否为纯数字            |                |
|  isnumeric()   |          是否跟数字有关           |                |
| isidentifier() |      是否是一个合法的变量名       |                |
|   islower()    |         字符是否为纯小写          |                |
|   isupper()    |       字符是否为纯大写字母        |                |
|     join()     |         将字符串连接起来          |                |
|    split()     |      将字符用某一字符串分隔       |                |
|    strip()     |        去除两边的某一字符         | 默认为空白字符 |
|    replace     |    将某一字串替换为另一字符串     |                |
|    title()     |      将字符串转换为标题格式       |                |
|   swapcase()   |           将大小写互换            |                |


```python
# 常用的有join、split、strip

# join() 函数用于将序列（如列表、元组或集合）中的元素连接成一个字符串。它接收两个参数：一个序列和一个分隔符。分隔符用于在序列中的元素之间插入。
# 将一个列表中的元素连接成一个字符串，用逗号和空格作为分隔符
words = ['apple', 'banana', 'cherry']
separated = ', '.join(words)
print(separated)  # 输出：apple, banana, cherry
# 单个字符也可以作为分隔符
numbers = [1, 2, 3]
number_string = '!'.join(map(str, numbers))
print(number_string)  # 输出：1!2!3


# split() 函数用于将字符串按照分隔符拆分成多个部分，并返回一个列表。默认情况下，它使用空格作为分隔符。

# 将字符串按照空格拆分
sentence = "Hello World! How are you?"
words = sentence.split()
print(words)  # 输出：['Hello', 'World!', 'How', 'are', 'you?']
# 指定不同的分隔符
email = "john.doe@example.com"
split_email = email.split('@')
print(split_email)  # 输出：['john.doe', 'example.com']


# strip() 函数用于删除字符串左右两端的空白字符（包括空格、制表符、换行符等）。如果提供参数，则删除指定字符。

# 删除字符串两端的空白字符
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # 输出：Hello, World!
# 删除指定字符
text_with_punctuation = "Hello, World! How's it going?"
stripped_text_with_punctuation = text_with_punctuation.strip("!?")
print(stripped_text_with_punctuation)  # 输出：Hello, World Hows it going
```



## list



```python
# 创建列表
test = list()
test2 = []

# 打印列表
company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
print(company) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 增删改查
# 增
company.append('Tecent') # 向当前列表增加元素
company.extend(['Meta','Huawei']) # 增加另一个列表
# 删
company.remove('Tecent') # 删除元素
company.pop() # 删除列表最后一个元素
company.pop(1) # 删除索引为1的元素
del company[1] # 同上
# 改
company[0] = 'X'# 修改某一元素可以直接使用下标索引
company.reverse() # 不返回值，直接修改执行操作的list
company.sort()
company.sort(reverse = True)
sorted(company) # 返回一个排序后的list
tuple(company) # 转换为tuple
set(company) # 转换为set，可快捷去重
# 查
company.count('X') # 查找某一元素的个数


```



## tuple

不可更改数据成员

1. 长度
2. 正负索引
3. slice切片
4. 连接
5. in
```python
```

## set

数据成员中不可有重复元素，具有集合的性质（无序性，唯一性）

1. pop()
2. add()
3. clear()
4. intersection()
5. union()
6. issubset()
7. issuperset()
8. difference()
9. symmetric_difference()
10. disjoint()
```python
```


## loop

range()使用较为频繁

### while

### for

```python
```



## 函数

### 定义

### 参数

### 返回值

返回多个返回值

### 说明文档

### Lambda

```python
```



## 文件

编码、读取、写入、写出、追加写入

```python
```



## 异常

捕获的三种写法、异常的传递性

```python
```



## 模块

如何自定义包、导入第三方包的操作

```python
```



## 包

```python

```



## Json数据

json数据格式是什么、json如何操作、pyecharts

```python
```



## 数据可视化

折线图、柱状图、疫情地图、动态GDP柱状图（挖个坑，以后学完爬虫后结合做个网站）主要是pyechart的使用

```python

```



## 类

类的成员与方法，构造方法，魔术方法str、le<=、lt<，封装，继承，多态，还有抽象类

## 类型注解

变量类型注解两种方式，函数和方法的返回值类型注解，Union联合类型注解

## Mysql

