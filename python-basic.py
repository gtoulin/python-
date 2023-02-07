#2001010221 20软件技术3-5班 林晓斌

# 注释
# 单行注释
'''
这是多行注释，使用三个单引号
这是多行注释，使用三个单引号
这是多行注释，使用三个单引号
'''
"""
这是多行注释，使用三个双引号
这是多行注释，使用三个双引号
这是多行注释，使用三个双引号
"""

import math
print("20软件技术3-5班 林晓斌")

# 标识符的用法
_name = "林晓斌"
my_name = "林晓斌"

# 多变量赋值
a = b = c = 1
print(a, b, c)
a, b, c = 1, True, '林晓斌'
print(a, b, c)


# 函数的定义与使用

'''
定义：
def function_name(param1,param2,...):
    函数体
    [return 返回值]
调用:function_name(arg1,arg2,...)
'''
# 计算1+2+3+。。。n


def sum(n):
    sum_value = 0
    i = 1
    while i <= n:
        sum_value += i
        i = i+1
        return sum_value


print("1+2+3+...1000=", sum(100))

# 函数打印

'''
print用法:print(*object,sep='',end='\n',file=sys.studout,flush=False)

objects --复数，表示可以一次输出多个对象，输出多个对象时，需要用，分隔。
sep --用来间隔多个对象，默认值是一个空格。
end --用来设定以什么结尾，默认值是换行符\n,我们可以换成其他字符串。
file --要写入的文件对象。
flush --输出是否被缓存通常决定于flie,但如果flush 关键字参数为True,流会被强制刷新

'''


def print_test():
    print("www", "pytorch", "org")
    print("www", "pytorch", "org")
    print("www", "pytorch", "org", sep=".", end='-------')
    print("www", "pytorch", "org", sep=".")


print_test()

# 数据类型
# Number( int float bool complex)
# string (ste,单引号,双引号,'''多行字符串''',""""多行字符串""")
# List(list,[])
# Tuple(tuple,())
# Set(set,{})
# Dictionary(dict,{键1：值1，键2：值2，})


def datatype():
    a, b, c, d, e, f, g, h, i = 20, 5.5, True, 4 + \
        3j, 'hello', ['1', 2, False], (1, '2', [1, 2]), {1, 2, '3'}, {
            'name': '林晓斌', 'age': 35}
    print(type(a), type(b), type(c), type(d), type(
        e), type(f), type(g), type(h), type(i))
    print('c is bool:', isinstance(c, bool), 'd is str:', isinstance(d, str))


datatype()


def alg_operation():
    print('1k:', 2**10, '1M:', 2**20, '1G', 2**30, '1T:', 2**40)


alg_operation()
# 1）单引号或双引号
# 2）°或”用来表示多行字符串，
# 3）转义符\，r表示不转义
# 4）拼接字符申+复制当前字符申*
# 5）Fython中的学符申有两种索引方式，从左往右以0开始，从右往左以-1开始索引从0开始-1为衣图位置
# 6）python中的字符审不能改
# 7）子申被取：strvariablelfist:end：step]
word = '123456中国人民'
print(word)
print(word[0:])
print(word[0:7])
print(word[0:-1])
print(word[1:-1])
print("<ul>"+('<li>'+word[6:]+'</1i>')*3+"</ul>")

addr = '''
广东省
深圳市
龙岗区
龙翔大道2188号
'''
print("信息学院地址：", addr)

# 拼接字符串+复制当前字符串*
str = "she's our teacher"
print(str, str[0:-1], str[0], str*2, str+'teaching pytorch',
      '\nhel1o \nworld', r'\nhel1o \nworld')

# 字符串的格式化：使用format方法，为占位符（顺序占位，命名参数占位）
# 在括号中的数字用于指向传入对象在format（）中的位置（无数字表示顺序占位）
# 如果在format（）中使用了关键字参数，那么它们的值会指向使用该名字的参数。
# 位置及关键字参数可以任意的结合
# ：05.3f）表示保留3为小数格式化数字
print('{1}和{0}'.format('world', 'hello'))
print('{name}网址:{site}'.format(name='pytorch', site='https://pytorch.org/'))
print('站点列表{0},{1},和fother。'.format('Google', 'Baidu', other='Taobao'))
name, age = 'jeniifer', 27
print('hey! her name is {},so you ar {} aged'.format(name, age))
html = "<hi>welcome {}</h1>".format('liuzhijun')
print(html)
print('7/3=', '{:05.2f}'.format(7/3))

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号{}
for i in range(1, 10):
    for j in range(i, 10):
        print(i, '*', j, '=', i*j, end='\t')
        print('')

# 同一行显示多条语句
# Python 可以在同一行中使用多条语句 语句之间使用分号 分割， 以下是- 一 个简单的实例：
X = 5
y = 2
print(X, '+', y, '==', X+y)

# Python通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠\来实现多行语句。在【】}（）中的多行语句不需使用\:
list = [
    'item-one', 1, [1, 2]
]
print(list)

'''
if流程语句
if cond1:
    # do cond1
[
    elif cond2:
    # do cond2
    elif cond3:
    # do cond3
    else:
    # do others
]'''

'''
for循环
for iter_var in list_obj:
# do iteratation
for index,iter_var in enumerate(list_obj):
# do iteration
'''

'''
while循环
while condition:
# do iteration
[else:
# do else
]
'''
# 流程控制语句，计算1+2+3+...100
sum = 0
for i in range(1, 101):
    sum += i
print("1+2+3...+100=", sum)

sum = 0
i = 1
while i <= 100:
    sum += i
    i = i+1
print("1+2+3...+100=", sum)

# 列表操作示例


def list_operation():
    things = ['a', 1, 'b']
    print(things)


list_operation()

# 元组操作示例


def tuple_operation():
    t = 1, 2, 3, 4
    print(t)
    print(t[1])
    for i in t:
        print(i)
    for index, element in enumerate(t):
        print(index, element)


tuple_operation()

# 字典操作示例


def dict_operation():
    # 定义字典
    stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
    print(stuff)

    # 添加元素
    stuff['others'] = '...'
    print(stuff)
    # 删除字典元素
    del stuff['others']
    print(stuff)
    # 访问字典元素
    print("name:", stuff['name'], 'age:',
          stuff['age'], 'height:', stuff['height'])
    # 遍历字典
    for k, v in stuff.items():
        print(k, v)


dict_operation()


'''
面向对象的编程
class class_name:
    # 私有属性
    _private_attrib=初始值
    # 保护属性
    _protected_attrib=初始值
    # 公有属性
    pub_attrib =初始值
    # 构造函数
    def _init_(self, attribl, attrib2, ..):
        self.attribl = attribl
        self.attrib2 = attrib2
def method1(self):
    ..
def method2(self):
    ..
'''

'''
子类继承父类的属性和方法
class deribed_class_name(base_class_name1,base_class_name2,...)
        _init_(self,attribl,attrib2,..):
#先调用父类的构造方法初始化，然后初始化自有属性
base_class_namel.init_(attrib..)
base_class_name2.init_(attrib..)
'''

'''
方法重写（覆盖）
class base class:#定义父类
    def method(self):
        print('调用父类方法')

c1ass my_class(base_class):#定义子类
    def method(self)
        print('调用子类方法')

c=my_class()#子类实例
c.method()#子类调用重写方法
super(my_class,c).method()#用子类对象调用父类已被覆盖的方法
'''


class Complex:
    __real = 0
    __imag = 0

    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag
#print("contructing complex...")
    def __del__(self):
        print(" ")

    @property
    def norm(self):
        return math.sqrt(self.__real**2+self.__imag**2)

    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

    @property
    def real(self):
        return self.__real

    @property
    def imag(self):
        return self.__imag
    def __add__(self, other):
        return Complex(self.__real+other.real, self.__imag+other.imag)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Complex(self.real*other, self.imag*other)
        else:
            return Complex(self.__real*other.real-self.__imag*other.imag,
                           self.__real*other.__imag+self.__imag*other.real)

    def __repr__(self):
        return "real:{},imag:{},norm:{}".format(self.real, self.imag, self.norm)


complex1 = Complex(3, 4)
complex2 = Complex(1, 2)
complex3 = complex1+complex2
complex4 = complex1*complex2
complex5 = complex1*2
print("real:", complex1.get_real(), "imag:",complex1.get_imag(), "norm:", complex1.norm)
print(complex1)
print(complex2)
print(complex3)
print(complex4)
print(complex5)


class base_class:
    def say(self):
        print("i 'm parent'")


class child(base_class):
    def say(self):
        print("i 'm child'")


c = child()
c.say()
super(child, c).say()