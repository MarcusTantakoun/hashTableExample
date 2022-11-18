"""This function returns the first recurring letter in a given string in O(n) notation"""


def first_recurring(given_string):
    count = {}  # empty dictionary/hashtable to record all letters
    for char in given_string:
        if char in count:
            return char
        else:
            count[char] = 1  # we want to assign a key value as the letter:val (ex: a is assigned 1)
    return None


def rec_steps(n):
    if n == 2:
        return 2
    if n == 1 or n == 0:
        return 1
    total = rec_steps(n - 1) + rec_steps(n - 2)

    return total


def addTwoNum(l1, l2, ):
    l1.reverse()
    l2.reverse()
    list1 = ''
    list2 = ''
    for i in l1:
        list1 = list1 + str(i)
    for j in l2:
        list2 = list2 + str(j)

    total = int(list1) + int(list2)

    rev = 0

    while total > 0:
        rem = total % 10
        rev = (rev * 10) + rem
        total = total // 10

    string = str(rev)
    li = string.split()
    return li


l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(addTwoNum(l1, l2))
