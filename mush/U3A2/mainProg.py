import csv
from pathlib import Path

from myLib import isHarshad, isSiete, Hodges

dir_path = Path('/Users/asifhossain/workspace/whatever/verbose-octo-broccoli/mush/U3A2/')

with open(dir_path / 'Rumbers.txt', 'r') as f:
    reader = csv.reader(f, delimiter="\t")
    rumbers_list = [int(item) for sublist in reader for item in sublist]

all_harshad = [i for i in rumbers_list if isHarshad(i)]
sum_of_harshad = sum(all_harshad)

# 1
print(f"sum of harshad numbers: {sum_of_harshad}")

# 2
harshad_seven = [i for i in all_harshad if isSiete(i)]
with open(dir_path / 'HarshOut.txt', 'w') as f:
    f.write('\n'.join(map(str, harshad_seven)))

# 3
for i in harshad_seven:
    if i % Hodges == 0:
        print(i)
