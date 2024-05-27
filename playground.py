# coding = utf-8
# python is a interpreted language (not compiled language)
# print("Hello Github")

# a = "Zhoutian Xu"
# c = "My name is"

# print(c, a)

# def Initialization():
#     return 0

# ReadMe = open("ReadMe.txt", 'w')
# print('This is a file just for fun.', file = ReadMe)
# ReadMe.close()

# print(1, 2, 3, sep = ',', end = '\n', file = None)

# print('I love', end = '-->')
# print('u')

# print('I love' + ' ' + 'u') 
# # print('I love' + 1) can only concatenate str (not "int") to str

# name = input("Who do you love:") #default input: str
# print("I love" + name) 

# num = input('Input your favorite number:')
# num = int(num)
# print('Your favorite number is:', num) # cannot use '+' b/c num is a int (not str)

'''
Copyright: Owner: Zhoutian Xu
file_name: Playground
'''

"""
Today is a good day
"""

# class student:
#     pass

# def fun():
#     pass

# db = open('db.txt', 'w')
# print('1 2 3 4 5', file = db)
# db.close()

# name = input("What's your name: ")
# age = input("What's your age: ")
# intro = input("Write a breif intro: ")
# print("---Self Introduction---")
# print("Name: " + name, "Age: " + age, "intro: " + intro, sep = "\n")

# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

'''Variable (recommended to use lowercase)'''
# true = 'true'
# True = 'true' cannot use 'True' since it's keyword

# lucky_num = 11
# my_name = 'Zhoutian Xu'
# print('Type of lucky number: ', type(lucky_num))
# print(my_name, "'s lucky number is ", lucky_num)

# '''
# We can change the type of variable dynamically when using python
# '''

# lucky_num = '11'
# print('Type of lucky number: ', type(lucky_num))

# num = number = 1024 # allowed for more than one var
# print(num, number)
# print(id(num))
# print(id(number)) # same address

'''Constant (recommended to use uppercase)'''
# PI = 3.1415926 # constant

### Type
'''Integer'''
# num = 987 # Dec
# num2 = 0b1010101 # Bin
# num3 = 0o765 # Oct
# num4 = 0x87ABF # Hec
# print(num, num2, num3, num4)

'''float (i.e. 3.1415926)'''
# height = 187.6 
# print(height, type(height))
# x = 10
# y = 10.0
# print(type(x), type(y))
# x = 1.99E1413
# print(x, type(x))
# print(0.1 + 0.2) # result = 0.30000000000000004
# print(round(0.1+0.2, 2)) # result = 0.3

'''complex number e.g. j = sqrt(-1)'''
# x = 123 + 456j
# print('real number part', x.real)
# print('imaginary number part', x.imag)

# '''str'''
# city = 'Urbana' # can also use " "
# address = '410 N Lincoln Ave'
# print(city, address)
# info = '''
# address: 410 N Lincoln Ave
# city: Urbana
# phone: xxx-xxx-xxxx
# ''' # can also use """ """
# print(info)

# print('Urbana')
# print('Champaign')
# print('Urbana\nChampaign') # \n --> change line
# print('Urbana\n\n\nChampaign')
# print('Urbana\tChampaign') # \t --> space
# print('Urabannnnn\tChampaign') # \t --> space gets large
# print('I said:\'good morning\'') # \ include ' ' in str
# print('I\nlove\nu\n')
# print(r'I\nlove\nu\n') # can also use 'R, now \n is a normal str

'''index and slice of str'''
# s = 'helloworld'
# print(s[0], s[-10]) # index 0 and index -n represent the same char
# print('helloworld'[4], 'helloworld'[-6])
# print(s[2:7]) # not include [7] asc
# print(s[-8:-3]) # not inclue [-3] desc
# print(s[:5]) # default start from [0] to [5], not include [5]
# print(s[5:]) # default to the end 

'''operations of str'''
# x = '2001 is '
# y = 'the year I born'
# print(x+y) # connect two str
# print(x*10) # copy the content of 'x' 10 times
# print(10*x) # same
# print('2001' in x) # subset of x --> True
# print('birthday' in y) # not a subset of y --> False

'''bool (True or False / 1 or 0)'''
# x = True
# print(x, type(x), x+10, False + 10) # T = 1, F = 0
# print(bool(18)) # test int(18)'s bool value --> True
# print(bool(0), bool(0.0)) # False, False
# # Conclusion: Non-0 values' bool value are always True
# print(bool('Helloworld'), bool('')) # True, False
# # Conclusion: Non-empty values's bool value are always True
# print(bool(False), bool(None)) # False, False for None

'''Data type conversion'''
# x = 10
# y = 3
# z = x/y
# print(z, type(z))
# print('float converts to int:', int(3.14), int(-3.9))
# print('int converts to float: ', float(10))
# print('str converts to int:', int('100')+int('200'))
# print('error:', int('18a')) # invalid literal for int() with base 10: '18a
# print(int('3.14')) # invalid literal for int() with base 10: '3.14'
# print(float('45a.987')) # ValueError: could not convert string to float: '45a.987'
### chr() and ord()
# print(ord('s')) # the integer value in unicode of 's'
# print(chr(115)) # the char of 115 in unicode
# print('DEC to HEX;', hex(26472))
# print('DEC to OCT:', oct(26472))
# print('DEC to BIN:', bin(26472))

'''eval() # remove the outside '' and run '''
# s = '3.14+3'
# print(s, type(s))
# x = eval(s)
# print(x,type(x))
# # eval() usually use with input()
# age = eval(input('Input your age:')) # convert str to int, same as int(age)
# print(age, type(age))
# hello = 'hello'
# print(eval('hello'))

'''Arithmetic operations'''
# print('addition:', 1+1)
# print('minus:', 1-1)
# print('multiply:', 2*3)
# print('divide:', 10/2)
# print('divisible:', 10//3)
# print('mod:', 10%3)
# print('to x times:', 2**4) #2*2*2*2 or 2^2
# print(10/0) # error, division by zero

'''assignment-operator'''
x = 20
y = 10
x = x + y # x = 20 + 10 = 30
x+=y # same as x = x + y
print(x) # x = 30 + 10
x-=y # same as x = x - y
print(x)
x*=y # same as x = x * y
print(x)
x/=y # x = x / y, type converts to float
print(x, type(x))
x%=2 # x = x % 2 
print(x)
z = 3
y//=z # y = y // z
print(y)
y**=2
print(y)
a = b = c = 100 # a = 100, b = 100, c = 100
print(a,b,c)
a,b = 10,20 # a = 10, b = 20
print(a,b)
a,b = b,a # a = b, b = a at same time
print(a,b)
c = 32
a, b, c = b, c, a
print(a, b, c)

'''relational operator'''
print('Is 98 greater than 90?', 98>90)
print('Is 98 less than 90?', 98<90)
print(98==90)
print(98!=90, 98>=90, 98<=90, 98<=98, 90>=90)

'''logic operator'''
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(8>7 and 6>5) # True
print(8>7 and 6<5) # False
print(8<7 and 10/0) # False, no error: when the first argument is False, immediately get result --> False

print(True or True)
print(True or False)
print(False or False)
print(False or True)
print(8>7 or 10/0) # True, no error

print(not True) # False
print(not False) # True
print(not(8>7)) # not True --> False



