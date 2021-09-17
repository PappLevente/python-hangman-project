def occurance():
    word = 'testcase'
    letter = input('Please guess a letter:')
    start = 0
    end = len(word) - 1
    list = []
    while start <= end:
        if letter == word[start]:
            list.append(start)
        start += 1    
    return(list)

run = occurance()
print(run)
