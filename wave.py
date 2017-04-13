def wave(r,l):
    n = []
    m = ''
    p = []
    hx = '0123456789ABCDEF'
    for a in range(l):
        a+=1
        v= int((r*1j**(4*a/l)).imag)
        n+=[ -v ]
        s=hx[(v+r)%16]
        t='   '
        for a in range(v+r):
            if (a+1)%16: t+='.'
            else: t+='|'
        t+= ' '+hx[v%16]
        m+=s
        p+=[t]
    return [m, p]

def info(data):
    print()
    print()
    for a in range(len(data[1])):
        print( data[1][a] )
    print()
    print( '   '+data[0] )
    print()
    print()

d = wave(32,32)
info(d)
