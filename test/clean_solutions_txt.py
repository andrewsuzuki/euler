# Opens up solutions.txt and cleans it up by
# removing n. and spaces from both sides of each line

solutions_file = 'solutions.txt'

with open(solutions_file, 'r') as file:
    data = file.readlines()

for i, line in enumerate(data):
    data[i] = line.split('.', 1)[-1].strip(' ') if i >= 3 else line

with open(solutions_file, 'w') as file:
    file.writelines(data)
