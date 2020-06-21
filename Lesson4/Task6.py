from sys import argv
import itertools

count_start = int(argv[1])

# for step in itertools.count(count_start):
#     if step > count_start + 20:
#         break
#     else:
#         print(step)

for step in itertools.islice(itertools.count(count_start), 15):
    print(step)
print('-'*10)
for step in itertools.islice(itertools.cycle('HELLO'), 18):
    print(step)