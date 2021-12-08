import sys

if len(sys.argv) != 2:
    print("Program needs exactly 1 argument - the input file's path.")
    exit(1)

with open(sys.argv[1],"r") as f:
    depths = f.readlines()
    # map(int,depths)
    f.close()

# Each sliding sum includes two numbers used in the previous sliding sum
# So only the earliest and latest depths are of value in each comparison
count = 0;
for i in range(len(depths)-3):
    # if(depths[i] < depths[i+3]):
    #     count += 1
    if(int(depths[i]) < int(depths[i+3])):
        count += 1


print("Measurements larger than the previous: ",count)