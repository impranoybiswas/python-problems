def flatten_list(array):
    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result