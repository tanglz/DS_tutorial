# Function to print all words that follows the same order of characters as the given pattern
def patternMatch(words, pattern):
    # invalid input
    if not words or not pattern:
        return

    # check each word in the input list
    for word in words:

        # dict1 the stores mapping from word to pattern
        dict1 = {}

        # dict2 the stores mapping from pattern to word
        dict2 = {}

        # proceed only when the length of the pattern and word is the same
        if len(word) == len(pattern):

            # process each character in both word and pattern
            i = 0
            while i < len(pattern):
                # `w` stores the current character of the current word
                w = word[i]

                # `p` stores the current character of the pattern
                p = pattern[i]

                ''' check mapping from the current word to the given pattern '''

                # if `w` is seen for the first time, store its mapping to `p` in `dict1`
                if w not in dict1:
                    dict1[w] = p
                else:
                    # if `w` is seen before, its mapped character should be `p`
                    if dict1[w] != p:
                        break

                ''' check mapping from the given pattern to the current word '''

                # if `p` is seen for the first time, store its mapping to `w` in `dict2`
                if p not in dict2:
                    dict2[p] = w
                else:
                    # if `p` is seen before, its mapped character should be `w`
                    if dict2[p] != w:
                        break

                i = i + 1

            # if the current word matches the pattern, print it
            if i == len(pattern):
                print(word, end=' ')


if __name__ == '__main__':
    # a list of words
    words = ['leet', 'abcd', 'loot', 'geek', 'cool', 'for', 'peer', 'dear', 'seed',
             'meet', 'noon', 'otto', 'mess', 'loss']

    # given pattern
    pattern = 'moon'

    patternMatch(words, pattern)