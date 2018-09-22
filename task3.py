# Task 3. Create method that returned value from list based on index. If list does not contain such index, than return None value

def get_value_from_list(data:list, index:int):

    try:
      return print(data[index])
    except IndexError:
      return print(None)

get_value_from_list([1,2,3], 2)
get_value_from_list([1,2,3], 16)