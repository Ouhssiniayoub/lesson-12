n = int(input("please entre the number:"))
print(((lambda n,f:n%10+f(n//10,f) 
        if n>0 else 0) \
               (n ,(lambda n,f:n%10+f(n//10,f) if n>0 else 0))))