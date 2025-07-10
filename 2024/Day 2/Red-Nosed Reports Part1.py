safe_count = 0

def is_monotonic(list):
    increasing = decreasing = True

    for i in range(len(list)-1):
        if int(list[i]) > int(list[i+1]):     
            increasing = False
        elif int(list[i]) < int(list[i+1]):
            decreasing = False
    return increasing or decreasing

print("Input")
input_list = []

while True:
    user_input = input()
    if not user_input:
        break
    input_list = user_input.split()

    if is_monotonic(input_list):
        difference = True
        for i in range(len(input_list)-1):
            difference = abs(int(input_list[i])-int(input_list[i+1]))
            if difference < 1 or difference > 3:
                difference = False
                break
        if difference:
            safe_count += 1
                    
print(safe_count)