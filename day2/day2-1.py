import sys

f = open(sys.argv[1],"r")
depth = 0
horiz = 0

for line in f:
    if line[0] == 'f':
        horiz += int(line[8])
    elif line[0] == 'd':
        depth += int(line[5])
    elif line[0] == 'u':
        depth -= int(line[3])

f.close()
print(f"Depth: {depth}\nHorizontal displacement: {horiz}\nProduct: {depth*horiz}")
