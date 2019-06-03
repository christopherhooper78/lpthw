from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename)

print(f"Reading the file {filename}")
print(target.read())

print("And finally, we close it.")
target.close()
