def count_keyPhrases_for_pkeAlgo(keyphrases, KP):
    common_keyPhrases = KP
    for counter, (candidate, score) in enumerate(keyphrases):
    
        if common_keyPhrases.get(candidate) != None:
            common_keyPhrases[candidate] = common_keyPhrases[candidate] = common_keyPhrases[candidate]+1
        else:
            common_keyPhrases[candidate] = 1

    return common_keyPhrases


def count_keyPhrases_for_RakeAlgo(keyphrases, KP):
    common_keyPhrases = KP
    
    for counter, (score, candidate) in enumerate(keyphrases):
        if counter == 20: 
            break
        if common_keyPhrases.get(candidate) != None:
            common_keyPhrases[candidate] = common_keyPhrases[candidate] = common_keyPhrases[candidate]+1
        else:
            common_keyPhrases[candidate] = 1
            
    return common_keyPhrases
            
        