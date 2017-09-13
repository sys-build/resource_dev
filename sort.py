#!/usr/bin/python

f = open('vmlinux_fun_filename.txt', 'r')
fw = open('vmlinux_sym_sorted.txt', 'w')
i = 0
my_dict = {}

for line in f:
	line = line.strip('\n')
	if i % 2 == 0:
		fun_name = line
	else:
		dir_name = line
		my_dict[fun_name] = dir_name
	i = i+1

f.closed

keys = my_dict.keys()
keys.sort()
for key in keys:
	fw.write(key)
	fw.write(' ')
	fw.write(my_dict[key])
	fw.write('\n')

fw.closed

