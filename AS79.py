def make_it_laugh(string):
    vowels = ('a','e','i','o','u')
    newWord = []
    for i in string:
        if i in vowels:
            newWord.append('haha')
        else:
            newWord.append(i)
    return ''.join(newWord)

print(make_it_laugh('Pear'))


