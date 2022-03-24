# Function to find the majority element present in a given list
def findMajorityElement(nums):
    # create a dictionary to store each element's frequency
    d = {}

    for i in nums:
        if d.get(i):
            d[i] = d.get(i)+1
        else:
            d[i] = 1

        # d[i] = d.get(i, 0) + 1

    # return the element if its count is more than `n/2`
    for key, value in d.items():
        if value > len(nums) / 2:
            return key

    # no majority element is present
    return -1


if __name__ == '__main__':

    # assumption: valid input (majority element is present)
    nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]

    result = findMajorityElement(nums)
    if result != -1:
        print('The majority element is', result)
    else:
        print('The majority element doesn\'t exist')