
import itertools

s, k = str(raw_input()).strip().split()

results = []

for i in range(int(k)):
    results = [sorted(c) for c in itertools.combinations(s, i + 1)]
    for result in sorted(results):
        print(''.join(result))
