def reverse(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
n=int(input())
if n<0:
    num=-n
else:
    num=n
result=reverse(num)
if n<0:
    print(-result)
else:
    print(result)                    