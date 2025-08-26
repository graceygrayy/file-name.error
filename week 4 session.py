file = open(",/WEEK4/grace_ contact.pdf", "w")
file.write("grace1, grace2, grace3")

# Reading content from a file

file = open(",/WEEK4/grace_ contact.pdf", "r")
content = file.read()
print(content)

print(file.read())