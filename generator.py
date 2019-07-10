def fib(limit):  
    a, b = 0, 1
    while a < limit: 
        yield a 
        a, b = b, a + b 
    # return ''
    

# x = fib(6) 
  
# print(x.__next__()) 
# print(x.__next__()) 
# print(x.__next__()) 
# print(x.__next__()) 
# print(x.__next__()) 
    
for i in fib(6):  
    print(i) 