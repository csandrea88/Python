def CoinToss():

    
    import random
    headtosses = 0
    tailtosses = 0

    for x in range(5):
        toss = random.randint(1, 2)
        #print toss
        if toss == 1:
            headtosses += 1 
            print "Attempt #{} Throwing a coin. Its heads. Got {} head(s) so far and {} tail(s) so far".format(x,headtosses,tailtosses)
        elif toss == 2:
            tailtosses += 1 
            print "Attempt #{} Throwing a coin. Its tails. Got {} tail(s) so far and {} head(s) so far".format(x,tailtosses,headtosses)
    

CoinToss()