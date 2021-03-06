# -*- coding:utf-8 -*-
import functools

__author__ ='djj'

#1.var Change pythonic\
a = 1
b = 2

a,b=b,a
print a,b

#2.For list
for i in [0,1,2,3,4,5]:
    print i
# or
for i in range(6):
    print i

# pythonic
for i in xrange(6):
    print i

# 3.For list with index
colors = ['red','green','blue','yellow']

for i in range(len(colors)):
    print i,'---->',colors[i]

# pythonic
for i,color in enumerate(colors):
    print i,'---->',color

# 4.Character string
# 字符串连接时，普通的方式可以用 + 操作

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s+=','+name

# pythonic
print (','.join(names))

# 5.open/close file
# ordinary
f = open('data')
try:
    data = f.read()
finally:
    f.close()

# pythonic
with open('data') as f:
    data2 = f.read()


# 6.list derivation
# Ordinary
result = []
for i in range(10):
    s = i*2
    result.append(s)

# pythonic
print [i*2 for i in xrange(10)]

# 7.decorator
import urllib
def web_lookup(url,saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

# pythonic

def cache(func):
    saved = {}
    # @functools.wraps(func)
    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
    return wrapper

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

# 8.reasonable use list

names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
names.pop(0)
names.insert(0,'mark')

# pythonic
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])
names.popleft()
names.appendleft('mark')

# 9.sequence unpacking
# ordinary
p = 'vttalk','female',30,'python@qq.com'
name = p[0]
gender=p[1]
age = p[2]
email=p[3]

# pythonic
name1,gender1,age1,email1=p

# 10.dictionary traversal key and value
# ordinary
# method:1
d = {}
for k in d:
    print k,'---->',d[k]
# method:2
for k,v in d.items():
    print k,'--->',v


# pythonic
for k,v in d.iteritems():
    print k,'--->',v

# iteritems 返回迭代器对象，可节省更多的内存，
# 不过在 python3 中没有该方法了，只有 items 方法，等值于 iteritems。


# 代码这样写更优雅
# 1.chain comparison operation
# ordinary
age2 = 18
if age2 > 18 and age<60:
    print "young man"

# pythonic
if 18 < age < 60:
    print "young man"


# 2.if/else 三目运算
# ordinary
if gender == 'male':
    text = '男'
else:
    text = '女'

# pythonic
text2 = '男' if gender =='male' else '女'

# Pythonic has a word：
# “There should be one-- and preferably only one --obvious way to do it. ”。

# 3.Truth value judgment
# ordinary
attr = ''
values = []
def do_something():
    pass

if attr == True:
    do_something()

if len(values)!=0:
    do_something()


# pythonic
if attr:
    do_something()
if values:
    do_something()


# 4.for/else :
# ordinary
mylist =[1,2,3]
theflag=1
def process(n):
    print n
flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(1)

if not flagfound:
    raise ValueError('List argument missing terminal flag.')

# pythonic
for i in mylist:
    if i==theflag:
        break
    process(i)
else:
    raise ValueError('List argument missing terminal flag')


# 5.Character String format
# ordinary
s1 = 'foofish.net'
s2 = 'vttalk'
s3 = 'welcom to %s and following %s' % (s1,s2)

# pythonic
s4 = 'welcom to {blog} and following {wechat}'.format(blog='foofish.net',wechat='vttalk')

# 6 list slice
# ordinary
items = range(10)

# odd
odd_items = []
for i in items:
    if i%2 != 0:
        odd_items.append(i)

#Copy
copy_items = []
for i in items:
    copy_items.append(i)

# pythonic
# A range of first to fourth elements
sub_items = items[1:4]
# odd
odd_items = items[1::2]
# copy
copy_items = items[::]
# or
copy_items = items[:]
# 列表元素的下标不仅可以用正数表示，还是用负数表示，
# 最后一个元素的位置是 -1，从右往左，依次递减。
"""
--------------------------
 | P | y | t | h | o | n |
--------------------------
   0   1   2   3   4   5 
  -6  -5  -4  -3  -2  -1
--------------------------
"""

# 7.be good at yield
# ordinary
def fib(n):
    a,b = 0,1
    result = []
    while b < n:
        result.append(b)
        a,b = b,a+b
    return result

# pythonic
def fib_new(n):
    a,b=0,1
    while a < n:
        yield b
        a,b=b,a+b


print fib(4)

a = fib_new(4)
print next(a)
print next(a)
print next(a)

L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
print next(g)



# 8.get dict element
# ordinary
d = {'name':'foo'}
if d.has_key('name'):
    print (d['name'])
else:
    print 'unkonw'

# pythonic
print d.get('name','unkonw')


# 9. Default dictionary defaults
#通过 key 分组的时候，不得不每次检查 key 是否已经存在于字典中。
# ordinary
data3 = [('foo',10),('bar',20),('foo',39),('bar',49)]
groups = {}
for (key,value) in data3:
    if key in groups:
        groups[key].append(value)
    else:
        groups[key] = [value]

# pythonic
# method 1
groups = {}
for (key,value) in data3:
    groups.setdefault(key,[]).append(value)

# method 2
from collections import defaultdict
# groups = defaultdict(lambda :[1])
groups = defaultdict(list)
for (key,value) in data3:
    groups[key].append(value)
groups['k']
print groups


# 10.dict deduction
# before python 2.7
numbers = [1,2,3]
my_dict = dict([(number,number*2) for number in numbers])
print (my_dict) #{1:2,2:4,3:6}

# pythonic
numbers = [1,2,3]
my_dict = {number:number*2 for number in numbers}
print my_dict #{1:2,2:4,3:6}

#and fiter
my_dict = {number:number*2 for number in numbers if number > 1}
print my_dict


# pythonic for dict object
# 0.Use'in'or'not in' to check whether 'key' exists in the dictionary

# ordinary
dictionary = {}
key = 'key'
keys =  dictionary.keys()
for k in keys:
    if key == k:
        print True
        break

# pythonic
if key in dictionary:
    print True
else:
    print False

# 1.Initialize dictionary key using 'setDefault()'
if 'key' not in dictionary:
    dictionary['key'] = []
dictionary['key'].append("list_item")

# pythonic
dictionary.setdefault('key',[]).append("list_item")

# 2.Initialize dictionary using 'defaultdict'
d={}
if 'a' not in d:
    d['a'] = 100
d['a'] +=10

# pythonic
from collections import defaultdict
d=defaultdict(lambda :100)
d['a']+=10

# 3.Iterating large data with 'iteritems ()'
# The following code makes up about 1.6G of memory

# d = {i:i*2 for i in xrange(10000000)}
# for key,value in d.items():
#     print "{0}={1}".format(key,value)

# Replace items () with the iteritem () method
#Reduced memory consumption by 50%
# iteritem() back a iterator(iterators)

# for key,value in d.iteritems():
#     print "{0}={1}".format(key,value)


# 4.Efficient merge dictionary
# ordinary
x = {'a':1,'b':2}
y = {'b':3,'c':4}
z = dict(x.items()+y.items())
#The following code  in python 3.X
z1 = dict(list(x.items())+list(y.items()))

# pythonic
# in python3.5
# z2 = {**x,**y}
# in python2.X
z2 = x.copy()
z2.update(y)

# Of course, you can wrap it as a function:
def merge_dicts(*dict_args):
    '''
    可以接收一个或者多个字典参数
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

# z3 = merge_dicts(a,b,c,d,e,f,g)

# other ways but not best
# py2.7
dicts = [{'a':3,'x':4},{},x,y]
{k:v for d in dicts for k,v in d.items()}
# <2.6
dict((k,v) for d in dicts for k,v in d.items())
# 直接使用python3.5中的{**x, **y}是最快的，使用update次之，用字典推导式相对来说是最慢的。




































































































