def avg (nums) :
    return sum(nums) / len(nums)

def calculation (nums) :

    total = print("Total :", sum(nums))
    avarage = print("Average :", avg(nums))
    maximum = print("Maximum :", max(nums))
    minimum = print("Min :", min(nums))

    return (total, avarage, maximum, minimum)