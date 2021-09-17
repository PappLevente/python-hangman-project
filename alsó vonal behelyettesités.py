game=True

while game:                                      #ez konkrétan a vonalak behelyettesitése, nemtudtam leegyszerűsiteni
    read = input('Kérek egy tippet: ')[0]
    i = 0
    word_in_iguess = False
    find = False 
    for letter in iguess:
        if read == letter :
            word_in_iguess = True
    iguess.append(read)
    if not word_in_iguess:
        for letter in word:
            if read == letter :
                string_list = list(wordout)    #felülirja az alsó vonalat, lecleareli a wordout-ot
                string_list[i] = read
                del wordout
                wordout = "".join(string_list)
                guessd+=1
                find = True
            i+=1
    print(wordout)         