def remove_duplicates(nums):
    return list(set(nums))

def only_duplicates(nums):
    get_duplicates = [num for num in nums if nums.count(num) > 1]
    return list(set(get_duplicates))