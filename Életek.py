game = True     #ez a kód legelejére hogy letudjon állni a végén
                ##életek-belekell épiteni majd mert igy használhatatlan
while game:
    if i == wordlength and not find: # életvesztés hiba esetén, ezt az új kódba kell majd módositani
            life-=1                
life = 10  
    print(life)  
    if life==0:
        print('lose')
        game = False
    if guess == wordlength:
        print('Win')
        game = False