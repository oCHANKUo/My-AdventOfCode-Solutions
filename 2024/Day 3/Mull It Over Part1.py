import re

open_file = open(r"") # Path to the input text

puzzle_input = open_file.read()

pattern = r"mul\((\d+),(\d+)\)"
total = 0

matches = re.findall( pattern, puzzle_input)

for str_num1, str_num2 in matches:
    num1 = int(str_num1)
    num2 = int(str_num2)
    product = num1*num2
    total += product

print(total)

open_file.close()
