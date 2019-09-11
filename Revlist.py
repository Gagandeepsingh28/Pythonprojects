l=[]
i=1
while i==1:
    ch=input( "select 1 for append 5 for sort asc 6 for sort desc 7 for n highest value 8 for n lowest value")
if ch=='1':
    d=input("enter")
    l.append(d)
elif ch=='5':
    s=l.sort()
    print(s)
elif ch=='6':
    r=l.sort(reverse=True)
    print(r)
