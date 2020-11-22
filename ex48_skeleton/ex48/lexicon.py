# goes through user input and returns a list of tuples. If word isnt part of lexicon, still returns the word, but sets the toke to an error token, which tells the user they messed up. 
# breaks up a user sentance to figure out the types of words
user_input = input("> ")
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'up': 'direction',
    'down': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
    1234: 'number',
    3: 'number',
    91234: 'number',
    41: 'number',
    927: 'number',
    29340519032487: 'number',
    00000000000: 'number',
    'ASDFADFASDF': 'error',
    'IAS': 'error'
}


def scan(sentence):
    sentance = sentence.lower()
    result = []
    words = sentence.split()
    for word in words:
        try:
            word = int(word)
        except:
            pass
        if word in lexicon:
            word_type = lexicon.get(word)
            result.append((word_type, word))
        else:
            unknown_word = word
            new_pair = ('error', unknown_word)
            result.append(new_pair)
    return result

print(scan(user_input))