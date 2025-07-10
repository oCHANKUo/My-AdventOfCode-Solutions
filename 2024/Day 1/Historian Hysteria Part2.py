#Goal: Find the similarity score. Calculate, value * number of times it appears on the right_list. Then calculate the total sum of those calculated values

left_list = []
right_list = []

print("Enter each of your values seperated by a blank space")

while True:
    user_input = input()
    if not user_input:
        break
    inputParts = user_input.split()
    left_list.append(int(inputParts[0]))
    right_list.append(int(inputParts[1]))

# frequency = 0 - Realised you dont need a frequency, and only made it more complicated. Puzzle is meant to trick you.
similarity_score = 0

for i in range(len(left_list)):
    for j in range(len(right_list)):
        if left_list[i] == right_list[j]:
            similarity_score = similarity_score + left_list[i]
            continue

print(similarity_score)