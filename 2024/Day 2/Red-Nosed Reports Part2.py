
# difference = True

def is_monotonic(lst):
    increasing = decreasing = True

    for i in range(len(lst)-1):
        if int(lst[i]) > int(lst[i+1]):     
            increasing = False
        elif int(lst[i]) < int(lst[i+1]):
            decreasing = False
    return increasing or decreasing

# def is_monotonic_if_removed_one(lst):
#     for i in range(len(lst)-1):
#         new_list = lst[:i] + lst[i+1:]
#         if is_monotonic(new_list):
#             return True
#     return False

def is_difference_valid(lst):
    for i in range(len(lst)-1):
        difference = abs(int(lst[i])-int(lst[i+1]))
        if difference < 1 or difference > 3:
            return False
    return True

# def is_skip_difference_valid(lst):
#     for i in range(len(lst)-1):
#         new_list = lst[:i] + lst[i+1:]
#         if is_difference_valid(new_list):
#             return True
#     return False

def check_conditions(lst):
    return is_monotonic(lst) and is_difference_valid(lst)

def can_fix_by_removal(lst):
    for i in range(len(lst)):
        new_list = lst[:i] + lst[i+1:]
        if check_conditions(new_list):
            return True
    return False

print("Input")
input_list = []
safe_count = 0

while True:
    user_input = input()
    if not user_input:
        break
    input_list = user_input.split()

    if check_conditions(input_list):
        safe_count += 1
    elif can_fix_by_removal(input_list):
        safe_count += 1
                
                    
print(safe_count)