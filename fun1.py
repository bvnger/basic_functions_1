#1
def a():
    return 5 #function will return 5
print(a()) # a = a(5)

#2
def a():
    return 5 #function will return10
print(a()+a())# a = a(5) +  a(5)=10

#3
def a():
    return 5
    return 10 # function will return 5 and stop
print(a()) # 10 is not returned because return stops the function

#4
def a():
    return 5 
    print(10)# function will return 5 and stop
print(a()) # even though 10 is now a print statement, 5 return will still return and  stop function

#5
def a():
    print(5) # function will print 5 and then return none 
x = a() # x was defined but not returned, console will return none for the value of x 
print(x)

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) #returns 25, not sure why 

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5 # function will print 100
    else:
        return 10 #then return 10
    return 7 #but not seven, as first return statement stopped function
print(a())

#8
def a():
    b = 100 
    print(b) # function will print 5
    if b < 10:
        return 5 #b is not less than 5, so this will be skipped over
    else:
        return 10 #then we return 10 and fall out of function
    return 7
print(a())

#10
def a(b,c):
    return b+c #function will add b and c (3,5) 
    return 10 # not returned as first return statement will break func
print(a(3,5))

#11
b = 500
print(b) # function will print 500  
def a():
    b = 300 # a has been defined, b is now redefined as 300
    print(b) # b(500) will be printed
print(b) # we move back outside the function where b will revert to new val of 300 
a()
print(b) # and  then print former val of 500

#12
b = 500
print(b) # function defined and printed 500
def a():
    b = 300 
    print(b) # a is defined as b = 300 and set up to print b
    return b 
print(b) # function prints "current" b ( 500)
a() # will be printed from inside function
print(b) # function will print prior val of b

#13
b = 500
print(b) # function will define and print b (500)
def a():
    b = 300 
    print(b) # function will define a as b @ 300 
    return b # 500 will be returned
print(b) # function will print 300
b=a() # b is defined s 300 
print(b) # b will be printed as 300

#14
def a():
    print(1) # a will be defined as 1 and printed
    b() # b is called, because it is called here, 3 will be printed
    print(2) # 2 will be printed here 
def b(): # THIS IS ONLY DEFINING THE FUNCTION, but function is called up above
    print(3)
a() # not printed, outside of function and not returned or printed

#15
def a():
    print(1) #a is defined and printed as 1
    x = b() # x is defined as calling b
    print(x) # x is now called to be printed 3 will be printed, 5 will be returned
    return 10 # 10 will be returned
def b(): # this is only the definition of b (init)
    print(3)
    return 5
y = a() #falls outside of function, will not be returned
print(y)
