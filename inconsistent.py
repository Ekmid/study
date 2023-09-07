def find_special_indices(arr):
    special_indices = []
    
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            special_indices.append(i)
    
    if not special_indices:
        return "Не найдено"
    elif len(special_indices) == 1:
        return special_indices[0]
    else:
        return special_indices