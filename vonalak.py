import random

wordlist = (random.choice(open("countries-and-capitals.txt","r").readline().split()))

word = wordlist[random.randint(0,len(wordlist)-1)]  #az első 5sort azért hagytam benne hogy lehessen látni hogy működik

wordlength = len(word)
i = 0
wordout = ''

while i < wordlength:
    wordout = wordout + '_'
    i+=1
iguess = []
print(wordout)