import sys

if len(sys.argv) != 2:
    print("Program needs exactly 1 argument - the input file's path.")
    exit(1)

with open(sys.argv[1],"r") as f:
    prev = -1
    curr = -1
    count = 0
    for line in f:
        curr = int(line)
        if prev == -1:
            prev = int(line)
            continue
        if prev < curr:
            count += 1
        prev = curr

print("Measurements larger than the previous: ", count)