a = int(input("please entre the number:"))
def n(a):
    a //= 10
    if a:
        n(a)
    else:
        return
n(a)
print(a % 10, end=' ')