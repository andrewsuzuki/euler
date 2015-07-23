import sys
import os
import glob

solutions_path = "../solutions/python"

# Add python solutions dir to the python path
sys.path.insert(0, os.path.abspath(solutions_path))

# Grab correct solutions from solutions.txt
with open("solutions.txt", "r") as file:
    solutions_data = file.readlines()
solutions = [""]
for i, line in enumerate(solutions_data):
    if (i <= 2):
        continue
    solutions.append(line.split('.', 1)[-1].strip())

# Glob all python solution filesk
files = glob.glob(solutions_path + "/*.py")

# Keep track of # of failed solutions
failed = 0

for solution_file in files:
    basename = os.path.basename(solution_file)
    import_name = os.path.splitext(basename)[0]

    # Import python solution file
    solution_imported = __import__(import_name)
    # Determine solution and cast to string
    solution = str(solution_imported.solution())

    # Check against correct solution
    try:
        assert solution == solutions[int(import_name)]
    except:
        failed += 1
        print("Solution #" + import_name + " failed")

print("Python - failed solutions: " + str(failed))
