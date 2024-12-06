#Goal: Find keywords based on analysis of word frequencies
#Main dev.: Long Thien

def words(file_name):
    '''
    Input (string) file_name.

    Returns a list of strings from file.
    '''

    in_file = open(file_name, 'r', encoding = 'utf8')
    wordlist = []
    for line in in_file:
        line = line.rstrip()
        if not (len(line) == 0): #If not an empty line, then is a word
            wordlist.append(line)

    return wordlist

def process(text):
    '''
    Input (string) text.

    Returns an ideally formatted string for further use.
    '''

    text = text.lower()
    for c in text:
        if not c.isalpha():
            text = text.replace(c, ' ') #Mark special chars as spaces

    mod_text = []
    for w in text.split(' '):
        if w != '': #Exclude spaces (marked chars + spacing)
            mod_text.append(w)

    return ' '.join(mod_text)

def freq_analyzer(text):
    '''
    Input (string) text.

    Returns a list of tuples (freq, word) in ascending order of freq.
    '''

    text = process(text)
    words = {}
    freq_word = []
    text_len = 0

    for w in text.split(' '):
        for l in w:
            if not l.isalpha():
                w = w.replace(l, '') #Delete all nonalphabetic chars
        words[w] = words.get(w, 0) + 1

    for w, f in words.items():
        freq_word.append((f, w))
        text_len += 1
    freq_word.sort() #Sort the list in ascending order of freq

    print(f'\nYour text contains {text_len} distinct words.')
    return freq_word


def most_repeated(wordlist, num = 4, min_rep = 3):
    '''
    Input (list) wordlist of tuples (freq, word);
    (int) num defaulted to 4;
    (int) min_rep defaulted to 3.

    Returns a list of tuples (freq, word) of top num most repeated words.
    Only add words repeated at least min_rep times.
    If # distinct freqs < num, return at max len(wordlist) words.
    '''

    most_rep = [] #List of top most repeated words
    pos = len(wordlist) - 1

    while num > 0 and pos >= 0:
        if wordlist[pos][0] >= min_rep:
            #wordlist[pos][0] = freq of pos-th word in wordlist

            most_rep.append(wordlist[pos])
        pos -= 1

        if pos > 0 and wordlist[pos][0] > wordlist[pos - 1][0]:
            num -= 1

            #To debug, uncomment the two lines below:
            #print(num)
            #print(pos)

    return most_rep


def link_words(wordlist):
    '''
    Input (list) wordlist of tuples (freq, word).

    Returns a list of (string) length-two concatenated/linked words.
    '''

    linked = []
    for first in wordlist:
        for second in wordlist:
            linked.append(first[1] + ' ' + second[1]) 
            #first & second are tuples (freq, word)

    return linked


def words_to_check(single, linked):
    '''
    Input (list) single of tuples (freq, word) of length-one most repeated words;
    (list) linked of length-two concatenations of most repeated words.

    Returns a list of strings to check for keyword potentials.
    '''

    check = []
    for len_one in single:
        check.append(len_one[1])
    for len_two in linked:
        check.append(len_two)

    return check


def potential_keyword(text, wordlist):
    '''
    Input (string) text;
    (list) wordlist to check;
    (list) not_keyword of non-keywords.

    Prints out potential keywords based on frequencies.
    Returns a list of potential keywords for further use.
    '''

    text = process(text)
    potential = []
    not_kw = set(words('notkw.txt')) #Convert to set for faster look-ups
    vietnamese = set(words('Viet74K.txt')) #License is included in folder, many thanks

    for word in wordlist:
        if word in vietnamese and word in text and word not in not_kw:
            potential.append(word)

    print('\nPotential keywords are: ', end = '')
    print(', '.join(word for word in potential) + '.')

    return potential


def advanced_search(potential):
    '''
    Utilize advanced Google search techniques.

    Input (list) potential of potential keywords.

    Prints out a formatted string for advanced Google search.
    '''

    print('\nFor advanced Google search, copy this text: ', end = '')
    print(' AND '.join(f'"{word}"' for word in potential))


if __name__ == '__main__':
    file_address = 'C:\\Users\\longt\\source\\repos\\word_frequency_analyzer\\test_data\\'
    file_name = '.txt'

    for n in range(1, 28):
        print(f'File T{n}.txt:')

        tmp = file_name
        tmp = f'T{n}' + file_name
        
        text = ' '.join(words(file_address + tmp))

        most_rep = most_repeated(freq_analyzer(text))
        to_check = words_to_check(most_rep, link_words(most_rep))

        potential = potential_keyword(text, to_check)
        advanced_search(potential)

        print('\n') #Empty line