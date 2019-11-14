my_file = open('file4-1.txt', 'r')
num_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = open('file4-2.txt', 'w')
for line in my_file:
    content = line.split()
    content[0] = num_translate[content[0]]
    new_file.write(' '.join(content) + '\n')

my_file.close()
new_file.close()