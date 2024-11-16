#Goal: Find keywords based on analysis of word frequencies
#Main dev.: Long Thien

def words(file_name):
    '''
    Input (string) file_name.

    Returns a set of words from file.
    '''

    in_file = open(file_name, 'r', encoding = 'utf8')
    wordlist = []
    for line in in_file:
        line = line.rstrip()
        if not (len(line) == 0): #If not an empty line, then is a word
            wordlist.append(line)

    return set(wordlist)


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
    not_kw = words('notkw.txt')
    vietnamese = words('Viet74K.txt') #License is included in folder, many thanks

    for word in wordlist:
        if word in vietnamese and word in text and word not in not_kw:
            potential.append(word)

    print('\nPotential keywords are: ', end = '')
    print(', '.join(word for word in potential) + '.')

    return potential


def advanced_search(potential): #Could import to second algo file
    '''
    Utilize advanced Google search techniques.

    Input (list) potential of potential keywords.

    Prints out a formatted string for advanced Google search.
    '''

    print('\nFor advanced Google search, copy this text: ', end = '')
    print(' AND '.join(f'"{word}"' for word in potential))


if __name__ == '__main__':

    text = input('Paste your text here: ')

    most_rep = most_repeated(freq_analyzer(text))
    to_check = words_to_check(most_rep, link_words(most_rep))

    potential = potential_keyword(text, to_check)
    advanced_search(potential)


#Test case 1: một.HaI_hai+ hi hi ba-bA*BA BỐN bỐn Bốn,bốn!@#$%^&*()-=năm;nam~năm;nam~năm;nam~năm;nam~năm;NAM!
#Test case 2: Trong cuộc sống hiện đại, công nghệ đóng vai trò vô cùng quan trọng. Công nghệ không chỉ giúp kết nối con người mà còn mở ra nhiều cơ hội phát triển kinh tế, giáo dục và y tế. Ở Việt Nam, sự phát triển của công nghệ thông tin đã thay đổi cách chúng ta làm việc, học tập và giao tiếp. Việc áp dụng các công nghệ mới như trí tuệ nhân tạo, dữ liệu lớn và Internet vạn vật đang thúc đẩy nền kinh tế và tạo ra nhiều ngành nghề mới. Tuy nhiên, bên cạnh những lợi ích to lớn, công nghệ cũng đặt ra nhiều thách thức về bảo mật thông tin và quyền riêng tư. Để phát triển bền vững, chúng ta cần phải tận dụng công nghệ một cách có trách nhiệm và hiệu quả.
#Test case 3: Lý thuyết tổ hợp là một phần quan trọng của toán học rời rạc chuyên nghiên cứu sự phân bố các phần tử vào các tập hợp. Thông thường các phần tử này là hữu hạn và việc phân bố chúng phải thoả mãn những điều kiện nhất định nào đó, tùy theo yêu cầu của bài toán cần nghiên cứu. Mỗi cách phân bố như vậy gọi là một cấu hình tổ hợp. Chủ đề này đã được nghiên cứu từ thế kỷ 17, khi những câu hỏi về tổ hợp được nêu ra trong những công trình nghiên cứu các trò chơi may rủi. Liệt kê, đếm các đối tượng có những tính chất nào đó là một phần quan trọng của lý thuyết tổ hợp. Chúng ta cần phải đếm các đối tượng để giải nhiều bài toán khác nhau. Hơn nữa các kỹ thuật đếm được dùng rất nhiều khi tính xác suất của các biến cố.

#BEFORE running test case 4, change line 174 to most_rep = most_repeated(freq_analyzer(text), num = 6).
#Test case 4: Trong toán học, ánh xạ (Tiếng Anh: mapping/Tiếng Hán: 映射) là một khái niệm chỉ quan hệ hai ngôi giữa hai tập hợp liên kết mỗi phần tử của tập hợp đầu tiên (được gọi là tập nguồn) với đúng một phần tử của tập hợp thứ hai (được gọi là tập đích). Tập nguồn và tập đích không nhất thiết phải là tập số thực hay tập con của tập số thực mà hoàn toàn có thể là tập hợp của các vector, hàm giải tích, biến ngẫu nhiên, ... Nói cách khác, một ánh xạ biểu hiện một quy tắc hay thao tác biến đổi toán học nhất định từ một phần tử trên một không gian (tập hợp) sang đúng một phần tử (thường được gọi là ảnh) trên không gian (tập hợp) thứ hai. Các ánh xạ có thể là toàn ánh, đơn ánh hoặc song ánh phụ thuộc vào tính chất của ảnh trên tập hợp thứ hai, và có thể được thể hiện bởi các toán tử, ký hiệu toán học hoặc các phép toán từ sơ cấp tới cao cấp. Chẳng hạn, phép biến đổi Laplace là một ánh xạ từ tập chứa các hàm trên miền thời gian sang tập chứa các hàm trên miền tần số phức thông qua một phép biến đổi bằng tích phân. Hay một ma trận thường được sử dụng để thể hiện một ánh xạ tuyến tính giữa hai không gian Euclide. Khi hai tập hợp là hai tập số thực hoặc tập con của số thực, ánh xạ giữa hai tập này thường được gọi là hàm số. Điều đó có nghĩa là hàm số được coi như một trường hợp đặc biệt của ánh xạ.