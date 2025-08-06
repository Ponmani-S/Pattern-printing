n=int(input())
print(' '*n+'* '*n)
m=n*2-1
for i in range(n):
    print(' '*(n-i-1)+'*'+' '*m+'*')
    m+=2
m-=2
for i in range(n-1):
    m-=2
    print(' '*(i+1)+'*'+' '*m+'*')
print(' '*n+'* '*n)