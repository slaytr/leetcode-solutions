numbers = [5,2,3,1,9]

def third_smallest(nums):
    values = [min(nums)-1]*3
    for integer in nums:
        if integer > values[0]:
            if integer > values[1]:
                if integer > values[2]:
                    values[0] = values[1]
                    values[1] = values[2]
                    values[2] = integer
                else:
                    values[0] = values[1]
                    values[1] = integer
            else:
                values[0] = integer
    return values[0]

print(third_smallest(numbers))