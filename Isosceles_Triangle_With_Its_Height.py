n=int(input())
print(' '*n+'*')
m=0
for i in range(n-1):
    print(' '*(n-m-1)+'*'+' '*m+'*'+' '*m+'*')
    m+=1
print('*'*n*2+'*')