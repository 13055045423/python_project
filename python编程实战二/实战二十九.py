a = 0
b = 0 
while  a <= 30 and b <= 30:
    if a + b == 30:
         print("鸡%d+兔%d=30"%(a,b))
#    a += 1
#    b = 30 -a
        if a + 2 * b == 45:
            print("有鸡%d只，有兔%d只"%(a,b))
            break
    a += 1
    b = 30 - a
#print(a,b)
    
        
      
