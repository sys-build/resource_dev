#!/usr/bin/python

f = open('vmlinux_fun_filename.txt', 'r')
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

sorted(my_dict.keys())
for k, v in my_dict.items():
	print k, v

