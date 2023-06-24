def fib(n):
    if n<0 or int(n) != n:
        return "not  defined"
    elif n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n=int(input('enter the number:\n'))
print("fibonacci series:",end = " ")
for i in range(0,n):
    print(fib(i),end = " ")
      
