import hashlib 
import sys 

with open(sys.argv[1],'r') as my_file:
	for line in my_file:
		print(line+','+hashlib.sha256(line).hexdigest())
