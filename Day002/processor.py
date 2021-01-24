import re
from toblibz.lib import findc
with open("./input") as f:
    v=0
    for i in f:
        splt=i.split(' ')
        p=r"".join(["^",splt[1].strip(':'),"{",splt[0].split('-')[0],",",splt[0].split('-')[1],"}","$"])
        pasw=list(splt[2])
        pasw.sort()
        if re.search(p,findc("".join(pasw),splt[1].strip(':'))[0]):
            v+=1
    print(v)