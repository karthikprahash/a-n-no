# a-n-no
i=input()
l=len(i)
d=0
p=0
for x in range(l):
    if(i[x].isalpha()):
        d=d+1
    if(i[x].isnumeric()):
        p=p+1
if(d==0 or p==0):
        print('no')
else:
        print('yes')
    
        
