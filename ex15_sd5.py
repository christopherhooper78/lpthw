from sys import argv

script = argv

filename = input("Type the filename:")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
