'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    target = 'th'

    if len(word) < 2:
        return 0
    # check to see if the word starts with 'th'
    if word[:2] == target:
        return count_th(word[1:]) + 1
    # if the word does not start with 'th' we want to iterate to the next letter in the word until it finds 'th'
    return count_th(word[1:])
