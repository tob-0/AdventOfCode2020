from toblibz.lib import *
with open("./input") as f:
    v=0
    for i in f:
        t,e=[],findc(i.split(' ')[2],i.split(' ')[1][:-1])[1]
        k=diffi(e,map(dec, list(map(int, i.split(' ')[0].split('-')))))
        for j in e:
            t.append(j in k)
        if t.count(True) == 1:
            v+=1
    print(v)