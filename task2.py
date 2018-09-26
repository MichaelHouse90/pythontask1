# Task 2.1 Create list with 10 elements using range method.  First element is 1.  Each next  equal previous plus 3.

task_two_list = []

for i in range(1, 20, 2):
    task_two_list.append(i)

print(task_two_list)

# Task 2.2 Append to previous list elements -  1, 5, 13, 20
print("\n")

appended_list = [1, 5, 13, 20]
task_two_list.extend(appended_list)
print(task_two_list)

# Task 2.3 Create set from previous list.
print("\n")

task_four_set = set(task_two_list)
print(task_four_set)

# Task 2.4 Compare elements count in task_three_list and task_four_set
print("\n")


def compare_elements(a: list, b: set):
    if len(a) > len(b):
        print("List is bigger")
    elif len(a) == len(b):
        print ("List is equal to Set")
    else:
        print("Set is bigger")


compare_elements(task_two_list, task_four_set)