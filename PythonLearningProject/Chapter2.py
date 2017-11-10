
# 主提示符（>>>）
# 次提示符（...）

# 输出
print "Hello, World!"

# 算术运算求绝对值
abs(-4)

# 定义字符串变量并输出
myString = "Hello Python"
print myString

# 单引号和双引号内字符串一样
"""
注意:在仅用变量名时，输出的字符串是被用单引号括起来了的。这是为了让非字符串对 象也能以字符串的方式显示在屏幕上--即它显示的是该对象的字符串表示，而不仅仅是字符 串本身。
引号表示你刚刚输入的变量的值是一个字符串。等你对 Python 有了较深入的了解之后， 你就知道 print 语句调用 str()函数显示对象，而交互式解释器则调用 repr()函数来显示对象。
"""

# 下划线(_)在解释器中有特别的含义，表示最后一个表达式的值。

"""
%s 表示由一个字符串来替换，而%d 表示由一个整数来替换，另外一个很常用的就是%f， 它 表示由一个浮点数来替换。
Print 语句也支持将输出重定向到文件。这个特性是从 Python2.0 开始新增的。符号 >> 用来重定向输出，下面这个例子将输出重定向到标准错误输
出:

"""
print "%s is Number %d!" % ("Python", 1)

# 从用户那里得到数据输入的最容易的方法是使用 raw_input()内建函数。它读取标准输入，并将读取到的数据赋值给指定的变量。
user = raw_input("Enter login name:")

'''
从用户那里得到数据输入的最容易的方法是使用 raw_input()内建函数。它读取标准输入，
并将读取到的数据赋值给指定的变量。 你可以使用 int() 内建函数将用户输入的字符串转换 为整数。
'''

"""
    >>> num = raw_input('Now enter a number: ')
    Now enter a number: 1024
    >>> print 'Doubling your number: %d' % (int(num) * 2)
    Doubling your number: 2048
"""

# 从标准输入读取一个字符串并自动删除串尾的换行字符。

"""
将函数分为两大类，一类只做事，不 需要返回值(比如与用户交互或设置变量的值)， 另一类则执行一些运算，最后返回结果。
如 果输出就是函数的目的，那么在函数体内使用 print 语句也是可以接受的选择。
"""

# Python 有两种除法运算符，单斜杠用作传统除法， 双斜杠用作浮点除法(对结果进行四舍五入)。
# 传统除法是指如果两个操作数都是整数的话， 它将执行是地板除(取比商小的最大整数)
# 而浮 点除法是真正的除法，不管操作数是什么类型，浮点除法总是执行真正的除法。
# 还有一个乘方运算符， 双星号(**)。 3**4(3的4次方)
# +(加法) -（减法） *（乘法） /（传统除法） //（浮点除法） %（取余运算） **（乘方运算） -2*4+3**2

"""
+ 和 - 优先级最低， *, /, //， % 优先级较高， 单目运算符 + 和 - 优先级更高， 乘方的优先级最高。(3 ** 2) 首先求值， 然 后是 (-2 * 4)， 然后是对两个结果进行求和。
"""

# 比较运算符
# < <= > >= == != <>
# Python 目前支持两种“不等于”比较运算符， != 和 <> ， 分别是 C 风格和 ABC/Pascal 风格。目前后者慢慢地被淘汰了，

# 逻辑运算符 and or not

"""
核心风格: 合理使用括号增强代码的可读性，在很多场合使用括号都是一个好主意，而没 用括号的话，会使程序得到错误结果，或使代码可读性降低，引起阅读者困惑。。
括号在 Python 语言中不是必须存在的， 不过为了可读性， 使用括号总是值得的。
"""

"""
# 变量和赋值
# Python 中变量名规则与其它大多数高级语言一样， 都是受 C 语言影响(或者说这门语言 本身就是 C 语言写成的)。
# 变量名仅仅是一些字母开头的标识符--所谓字母开头--意指大
# 写或小写字母，另外还包括下划线( _ ). 其它的字符可以是数字，字母， 或下划线。
# Python 变量名是大小写敏感的， 也就是说变量 "cAsE" 与 "CaSe" 是两个不同的变量。

# Python 是动态类型语言， 也就是说不需要预先声明变量的类型。 变量的类型和值在赋值 那一刻被初始化。变量赋值通过等号来执行。

"""

# 算术运算
"""
n = n * 10 <===> n*=10

Python 不支持 C 语言中的自增 1 和自减 1 运算符， 这是因为 + 和 - 也是单目运算符， Python 会将 --n 解释为-(-n) 从而得到 n , 同样 ++n 的结果也是 n.
"""

# 数字
"""
Python 支持五中基本数字类型，其中有三种是整形
  int (有符号整数)
  long (长整数)   
  bool (布尔值)
  float (浮点值)   
  complex (复数)
"""

"""
Python 中有两种有趣的类型是 Python 的长整型和复数类型。
Python 的长整数所能表达的范围远远超过 C 语言的长整数， 事实上， Python 长整数仅受限于用户计算机的虚拟内存总数。
从 Python2.3 开始，再也不会 报整型溢出错误， 结果会自动的被转换为长整数。在未来版本的 Python 中， 两种整数类型将 会无缝结合， 长整数后缀 “L”也会变得可有可无。

布尔值是特殊的整数。 尽管布尔值由常量 True 和 False 来表示， 如果将布尔值放到一 个数值上下文环境中(比方将 True 与一个数字相加)， True 会被当成整数值 1， 而 False 则会被当成整数值 0。
复数(包括-1 的平方根, 即所谓的虚数)在其它语言中通常不被直接 支持(一般通过类来实现)。

# 其实还有第六种数字类型， decimal， 用于十进制浮点数。不过它并不是内建类型， 你 必须先导入 decimal 模块才可以使用这种数值类型。 
由于在二进制表示中有一个无限循环片段，数字 1.1 无法用二进制浮 点数精确表示。因此， 数字 1.1 实际上会被表示成:
    >>> 1.1
    1.1000000000000001
    >>> print decimal.Decimal('1.1')
    1.1

"""

# 字符串
"""
# Python 中字符串被定义为引号之间的字符集合。

Python 支持使用成对的单引号或双引号， 三引号(三个连续的单引号或者双引号)可以用来包含特殊字符。
使用索引运算符( [ ] )和切 片运算符( [ : ] )可以得到子字符串。
字符串有其特有的索引规则:第一个字符的索引是 0， 最后一个字符的索引是 -1

加号( + )用于字符串连接运算，星号( * )则用于字符串重复。
    >>> print 'Hello'+'World!'
    HelloWorld!
    >>> print 'Hello'*4
    HelloHelloHelloHello

"""

# 列表和元组
"""
可以将列表和元组当成普通的“数组”，它能保存任意数量任意类型的 Python 对象。
和数 组一样，通过从 0 开始的数字索引访问元素，但是列表和元组可以存储不同类型的对象。

列表和元组有几处重要的区别。
列表元素用中括号( [ ])包裹，元素的个数及元素的值可 以改变。
元组元素用小括号(( ))包裹，不可以更改(尽管他们的内容可以)。
元组可以看成是 只读的列表。通过切片运算( [ ] 和 [ : ] )可以得到子集，这一点与字符串的使用方法一样。
    
    >>> pystr = 'Python!'
    >>> pystr[1]
    'y'
    >>> pystr[2:5]  # 从index=2 到 index=5
    'tho' 
    >>> pystr[:2]   # index=2 之前的
    >>> pystr[2:]   # index=2 之后的
    
元组也可以进行切片运算，得到的结果也是元组(不能被修改):
    >>> aTuple = ('robots', 77, 93, 'try')
    >>> aTuple
    ('robots', 77, 93, 'try')
字典是 Python 中的映射数据类型，工作原理类似 Perl 中的关联数组或者哈希表，由键- 值(key-value)对构
    >>> aTuple[:3]
    ('robots', 77, 93)
    >>> aTuplep[1]
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        NameError: name 'aTuplep' is not defined
    >>> aTuple[1]
    77

"""

# 字典
"""成。
几乎所有类型的 Python 对象都可以用作键，不过一般还是以数字或者 字符串最为常用。
值可以是任意类型的 Python 对象，字典元素用大括号({ })包裹。

    >>> aDict = {'host': 'earth'} 
    >>> aDict['port'] = 80 # add to dict
    >>> aDict
    {'host': 'earth', 'port': 80}
    >>> aDict['host']
    'earth'   

"""

# if 语句
"""
Python 与其它语言不同， 条件条达式并不需要用括号括起来

"""
























