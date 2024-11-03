#Goal: Analyze how many times each word has been said
def speech_analyzer(speech):
    mod_speech = speech.lower().split()
    words = {}
    let = []
    freq = []
    speech_len = 0

    for w in mod_speech:
        for l in w:
            if not l.isalpha(): #For example, 'hello' in 'hello,' isalpha but not ','
                w = w.replace(l, '')
        words[w] = words.get(w, 0) + 1

    for w, f in words.items():
        let.append(w)
        freq.append(f)
        speech_len += 1

    max_pos = freq.index(max(freq)) #Position of most common word
    min_pos = freq.index(min(freq)) #Position of least common word

    print(f'\nYour speech contains {speech_len} words.')
    print(f"Word most used: '{let[max_pos]}', number of times: {max(freq)}")
    print(f"Word least used: '{let[min_pos]}', number of times: {min(freq)}")

speech = input('Start your speech: ')
speech_analyzer(speech)