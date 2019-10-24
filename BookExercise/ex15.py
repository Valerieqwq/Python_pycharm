from sys import argv

script, filename = argv

txt = open(filename)

print(f"here's you file {filename}:")
print(txt.read())

# file_again = input("type the filename again:\n> ")
# print("type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)

print(open(input("type the filename again:\n> ")).read())
