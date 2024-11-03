#Goal: Analyze how many times each word has been said
def freq_analyzer(text):
    text = text.lower()
    words = {}
    let = []
    freq = []
    text_len = 0

    for c in text:
        if not c.isalpha():
            text = text.replace(c, ' ') #Mark special chars as spaces

    mod_text = []
    for w in text.split(' '):
        if w != '': #Exclude spaces (marked chars + spacing)
            mod_text.append(w)

    for w in mod_text:
        for l in w:
            if not l.isalpha():
                w = w.replace(l, '') #Delete all nonalphabetic chars
        words[w] = words.get(w, 0) + 1

    for w, f in words.items():
        let.append(w)
        freq.append(f)
        text_len += 1

    max_pos = freq.index(max(freq)) #Position of most common word
    min_pos = freq.index(min(freq)) #Position of least common word

    print(f'\nYour text contains {text_len} words.')
    print(f"Word most used: '{let[max_pos]}', number of times: {max(freq)}")
    print(f"Word least used: '{let[min_pos]}', number of times: {min(freq)}")

text = input('Paste your text here: ')
freq_analyzer(text)
