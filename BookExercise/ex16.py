from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("if you dont want that, hit ctrl-c (^c).")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1, "\n", line2, "\n", line3, "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("and finally, we close it.")
target.close()
