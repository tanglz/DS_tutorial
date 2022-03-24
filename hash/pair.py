def findPair(nums, target):
    # create an empty dictionary
    d = {}

    # do for each element
    for i, e in enumerate(nums):

        # check if pair (e, target - e) exists

        # if the difference is seen before, print the pair
        if target - e in d:
            print('Pair found', (nums[d.get(target - e)], nums[i]))
            return

        # store index of the current element in the dictionary
        d[e] = i

    # No pair with the given sum exists in the list
    print('Pair not found')


if __name__ == '__main__':
    nums = [8, 7, 2, 5, 3, 1]
    target = 10

    findPair(nums, target)