def num_from_str(str):
    str = ''.join([el for el in str if el.isdigit()])
    try:
        str = int(str)
    except ValueError:
        return 0
    return str


my_file = open('file6.txt', 'r')
my_dict = dict()
for line in my_file:
    subject, lectures, practice, labs = line.split()
    subject = subject[:-1]
    my_dict[subject] = num_from_str(lectures) + num_from_str(practice) + num_from_str(labs)
print(f'Общее количество часов по предмету\n{my_dict}')