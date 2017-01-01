# coding=utf-8
#!/usr/bin/env python3

""" Script to perform booking validation
"""

import sys, getopt
from utils import (get_list,
				   reorder_sequence,
				   recursive_sort,
				   export_list)
		   
def validate(argv):
	file = ''
	iterations = 500
	usage = 'usage: python validate.py -f <inputfile> -i <iterations>\n\n arguments:\n -h, --help		show this help message and exit \n -f, --file 		path to the input json file\n -i, --iterations 	number of iterations (default: 500)'

	try:
		opts, args = getopt.getopt(argv, 'hf:i:', ["help", "file=", "iterations="])
	except getopt.GetoptError:
		print(usage)
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print(usage)
			sys.exit()
		elif opt in ("-f", "--file"):
			file = arg
		elif opt in ("-i", "--iterations"):
			iterations = arg
	
	bookings = get_list(file)
	validated_bookings = reorder_sequence(sequence = bookings,
	                                      method = recursive_sort,
										  iterations = int(iterations))
	export_list(validated_bookings, 'output.json')	
	
if __name__ == '__main__':
	validate(sys.argv[1:])