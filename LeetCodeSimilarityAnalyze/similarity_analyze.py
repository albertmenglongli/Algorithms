import os
from collections import defaultdict
import itertools
from collections import Counter
txts = os.listdir('.')
companies_files = [(e.replace('_leetcode.txt', ''), e) for e in txts if e.endswith('leetcode.txt')]
data = defaultdict(list)
for company, file in companies_files:
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            data[company].append(int(line))


def compute_jaccard_index(set_1, set_2):
    n = len(set_1.intersection(set_2))
    return n / float(len(set_1) + len(set_2) - n)

data = {k: set(v) for k, v in data.items()}

companies = data.keys()

for p1, p2 in itertools.combinations(companies, 2):
    print(p1, p2, ':')
    print(compute_jaccard_index(data[p1], data[p2]))
    print()

numbers = []
for k, v in data.items():
    numbers.extend(list(v))
print(Counter(numbers))
