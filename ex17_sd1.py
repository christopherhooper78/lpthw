from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

print("All done.")

out_file.close()
in_file.close()
