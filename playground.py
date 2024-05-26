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
x = True
print(x, type(x), x+10, False + 10) # T = 1, F = 0
print(bool(18)) # test int(18)'s bool value --> True
print(bool(0), bool(0.0)) # False, False
# Conclusion: Non-0 values' bool value are always True
print(bool('Helloworld'), bool('')) # True, False
# Conclusion: Non-empty values's bool value are always True
print(bool(False), bool(None)) # False, False for None





