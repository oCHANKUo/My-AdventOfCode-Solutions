import re

open_file = open(r"") # Path to the input text

puzzle_input = open_file.read()

pattern = r"mul\((\d+),(\d+)\)|\b(do|don\'t)\(\)"
total = 0
do_mode = True

matches = re.finditer( pattern, puzzle_input)

for match in matches:
    if match.group(3): #if theres a match in group 3. Not if match in group 3 is this
        if match.group(3) == "do":
            do_mode = True
        else:
            do_mode = False

    elif match.group(1) and match.group(2):
        if do_mode:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            total += num1 * num2

print(total)

open_file.close()