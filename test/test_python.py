import sys
import os
import glob

solutions_path = "../solutions/python"

with open("solutions.txt", "r") as file:
    solutions_data = file.readlines()

solutions = ["NO ZEROTH SOLUTION"]
for i, line in enumerate(solutions_data):
    if (i <= 2):
        continue
    solutions.append(line.split('.', 1)[-1].strip())

files = glob.glob(solutions_path + "/*.py")

sys.path.insert(0, os.path.abspath(solutions_path))

failed = 0

for solution_file in files:
    basename = os.path.basename(solution_file)
    import_name = os.path.splitext(basename)[0]

    solution_imported = __import__(import_name)
    solution = str(solution_imported.solution())

    try:
        assert solution == solutions[int(import_name)]
    except:
        failed += 1
        print("Solution #" + import_name + " failed")

print("Python failed solutions: " + str(failed))
