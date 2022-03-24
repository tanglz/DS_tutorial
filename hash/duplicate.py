# Function to find a duplicate element in a limited range list
def find_duplicate(nums):
    # create a dictionary as a visited list
    visited = {}

    # for each element in the list, mark it as visited and return it if seen before
    for i in nums:

        # if the element is seen before
        if visited.get(i):
            return i

        # mark element as visited
        visited[i] = True

    # no duplicate found
    return -1


if __name__ == '__main__':
    # input list contains `n` numbers between 1 and `n-1` with one duplicate, where `n = len(nums)`
    nums = [1, 2, 3, 4, 3]

    print('The duplicate element is', find_duplicate(nums))
