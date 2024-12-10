# KWEProject
Main developer: Long Vinh Thien.

This is the Keyword Extractor (KWE) of our group. It is delevoped in Python and is exclusively modified to work with the Vietnamese language.

# How it works
Our KWE operates on the principle of finding most repeated words.

First, the KWE analyzes the input text (from a text file) to extract all distinct single-length words and their # of repetitions. It saves these data in a dictionary.

Next, the KWE proceeds to find X most repeated single-length words. The variable X can be adjusted via the argument in the function 'most_repeated' by changing the argument 'num'. You can also modify the function to return words that are repeated at least Y times by changing the 'min_rep' argument in the same function.

After the KWE has found the most repeated words, it starts to link those words together to form length-two words. This job is handled by the 'link_words' function. Now, since the newly linked words may have no meanings at all, the KWE compares the words with two .txt files to select the valid words.

All words marked as valid are considered as potential keywords and are displayed in the output.

For a visual description, refer to the drawn diagram 'HowItWorks.png'.
