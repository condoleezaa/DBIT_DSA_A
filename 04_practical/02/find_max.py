def find_max(list):
    if len(list) == 0:
        return None
    max_value = list[0]
    for item in list[1:]:
        if item > max_value:
            max_value = item
    return max_value

print(find_max([78, 92, 85, 61]))  
print(find_max([]))
