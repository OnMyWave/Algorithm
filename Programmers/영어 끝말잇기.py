def solution(n, words):
    word_relay = []
    last_word = words[0][0]
    for word in words:
        if last_word[-1] != word[0] or word in word_relay:
            break  
        else:
            word_relay.append(word)
            last_word = word

    if len(word_relay) == len(words):
        return [0,0]
    else:
        return list((len(word_relay)%n+1,len(word_relay)//n+1))

