# a=10
# print(a)
# if u print get out put is 10
# a=b=c=10
# print(a,b,c)
# if u print this get out put is 10,10,10

# multiple values passing.
# a,b,c=1,2,3
# print(a,b,c)
# if u print this u get out put 1,2,3
# a,b,c=1,2,3
# print('a is',a)
# print('b is',b)
# print('c is',c)
# if u print this a is 1 b is 2 c is 3
# a=10
# b=40
# c=a+b
# print(c)
# if u print this u get out put is 50
# data types

# a=10
# b=2.9
# c="chandra"
# d=3+7j
# f=True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(f))

# output
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'complex'>
# <class 'bool'>

# type conversion
# num=20
# d=str(num)
# print(d)
# print(type(d))

# output
# 10
# <class 'str'>
# num='20'
# d=str(num)
# print(d)
# print(type(d))

# output
# 20
# <class 'str'>

# num="chandra"
# d=int(num)
# print(d)
# print(type(d))
# string is not possible to convert int.
# int is possible to convert string.

# if statement
# if True:
#     print('this is if')
    # output is  this is if

# if False:
#     print('this is if')
# else:
#     print("this is else")
    # output is this is else

# a==b
# a!=b
# a<=b
# a>=b

# a=1
# b=3
# if a<b:
#     print("a is smaller than b")
# else:
#         print("b is smaller than a")

# a=1
# b=3
# if a>b:
#     print("a is smaller than b")
# elif a<b:
#     print("a is smaller than b")    
# else:
#         print("b is smaller than a")

# out put is a is smallar than b

# this is short hand if
# a=1
# b=22
# if a<b: print('this is short hand if')

# out put this is short hand if 

# a=1
# b=22
# print('this is short hand if') if a<b else print('this is short hand if else')

# out put this is short hand if


# a=200
# b=33
# c=500
# if a>b and c>b:
#     print("and")

# else:
#     print('else')

# output is and

# a=200
# b=33
# c=500
# if a>b and c>b:
#     print('or')
# else:
#     print('else')

# output is or

# chandra=[]
# print(chandra)

# output is []

# chandra=[1,2.3,"chandra",True]
# print(chandra)

# output is [1, 2.3, 'chandra', True]

# apend means adding

# chandra=[1,2.5,'chandra',True]
# chandra.append(2)
# print(chandra)

# output is [1, 2.5, 'chandra', True, 2] why because 2 come means we will given append (2)

# chandra=[1,2.3,'chandra',True]
# chandra.extend([1,4,6,7,8,])
# print(chandra)

# output is [1, 2.3, 'chandra', True, 1, 4, 6, 7, 8] why this add means will given extend like that [1,4,6,7,8]

# chandra=[0,2.3,'chandra',True]
# chandra.insert(1,'python')
# print(chandra)

# output is [0, 'python', 2.3, 'chandra', True] why this add means will given insert (1.'python')

# chandra=[1,1,2.2,'chandra',True]
# print(chandra.count(1))
# output is 3 because 1 is two times true also count for 1 time.that's what u get output is 3
# chandra=[1,1,2.2,'chandra',False]
# print(chandra.count(1))
# output is 2 because 1 is two times false count is 0 here.that's what u get output is 2
# chandra=[1,1,2.2,'chandra',False]
# print(len(chandra))
# output is 5 how much length is define this.

# chandra=[1,1,2.2,'chandra',True]
# chandra.pop(1)
# print(chandra)
# output is [1, 2.2, 'chandra', True] because 1 is remove here why means pop means delete.

# chandra=[1,1,2.2,'chandra',True]
# chandra.reverse()
# print(chandra)

# output is [True, 'chandra', 2.2, 1, 1] get list is reverse print.

# chandra=[1,1,2.2,4,6,7,98,7]
# chandra.sort()
# print(chandra)
# output is [1, 1, 2.2, 4, 6, 7, 7, 98] get small values is first print.big values is last ptint.

chandra=[1,1,2.2,4,6,7,98,5,6]
for i in chandra:
    print(i)
