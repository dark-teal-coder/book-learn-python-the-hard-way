from sys import argv

script, filename = argv

file = open(filename, "w")

print("Write your code when you are prompted with >")
print("Enter '-1' to end")

while True:
    line = input("> ")
    if line == "-1":
        break
    file.write(line + "\n")

file.close()