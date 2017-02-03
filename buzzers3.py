from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
	return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
	ignore = data.readline()
	flights={}
	for line in data:
		k, v = line.strip().split(',')
		flights[k] = v

pprint.pprint(flights)
print()

fts = {}

for k, v in flights.items():
	fts[convert2ampm(k)] = v.title()

pprint.pprint(fts)
print()


when = {}
for dest in set(fts.values()):
	when[dest]=[k for k,v in fts.items() if v == dest]

pprint.pprint(when)
print()

when2 = {dest: [k for k,v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when2)

