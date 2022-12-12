n = int(input("please enter the number:"))
x = int(input("please enter the number:"))
def h(x,n):
    def h(n):
        if n<1:
            return 1
        else:
            return n * h(n-1)
    return x**n/h(n)
print(h(4,5))