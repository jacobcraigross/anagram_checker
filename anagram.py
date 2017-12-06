# anagram checker
# simple but very pythonistic.
def anagram(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    return sorted(str1) == sorted(str2)

print anagram('Jake', 'Ross')
print anagram('god', 'dog')
print anagram('clint eastwood', 'old west action')


# a more manual approach.
def anagram_two(str1, str2):

    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    if len(str1) != len(str2):
        return False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

print anagram_two('Jake', 'Ross')
print anagram_two('god', 'dog')
print anagram_two('clint eastwood', 'old west action')
