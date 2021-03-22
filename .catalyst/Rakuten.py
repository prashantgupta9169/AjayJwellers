d=dict()
for i in l:
    d[i]=d.count(0,d[i]+1)
for i in d:
    if(d[i]>=2):
        return i




for i in range(len(l)):
    x=l[i+1:]
    if(l[i] in x):
        print(l[i])
    else:
        pass