left_list = []
right_list = []

print("Enter each of your values seperated by a blank space")

while True:
    user_input = input()
    if not user_input.strip():
        break
    inputParts = user_input.split()
    left_list.append(int(inputParts[0]))

print (left_list)
