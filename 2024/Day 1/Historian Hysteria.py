#Ultimate Goal: 2 sorted lists. Find the total sum of the differences between elements at each matching indexes.

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

left_list.sort()
right_list.sort()

total_sum = 0
difference = 0

for i in range (len(left_list)):
    difference = abs(left_list[i] - right_list[i])
    total_sum = total_sum + difference


print(total_sum)
