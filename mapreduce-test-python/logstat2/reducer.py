#!/usr/bin/python
import heapq
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))

#test edit
all_values = [x[0][1:3] for x in sorted_dict_ip_count]
unique_values = set(all_values)

group_list = []
for value in unique_values:
  this_group = []
  for x in sorted_dict_ip_count:
    if x[0][1:3] == value:
      this_group.append(x)
  group_list.append(this_group)

print([heapq.nlargest(3, i) for i in group_list])
#OUTPUT
#[['A', 'C'], ['B'], ['D', 'E']]
