TREE='#'
FREE='.'
i,j=0,0
with open("./input") as f:
    lines = list(f.readlines()).remove('\n')
    while i < len(lines):
        print(lines[i])
        i+=1
