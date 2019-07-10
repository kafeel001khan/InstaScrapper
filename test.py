class Test: 
  

    def __init__(self, limit): 
        self.limit = limit 
  
    def __iter__(self): 
        self.x = 0
        print ('in iter')
        return self
   
    def __next__(self): 
  
        x = self.x 
  
        if x > self.limit: 
            raise StopIteration 
  
        self.x = x + 1; 
        return x 

test_obj  = Test(10)
test_iter = test_obj.__iter__()
print(test_iter.__next__())
print(test_iter.__next__())
print(test_iter.__next__())

for i in test_obj: 
    print(i)