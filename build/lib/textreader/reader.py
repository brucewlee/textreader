import re, string
import warnings
# erase first textreader. for package distribution
import textreader.coefs as coefs



"""
remove non ascii

Params:
- self

Output:
- string : only ascii
"""
def remove_non_ascii_helper(text: str) -> str:
    return text.encode("ascii", "ignore").decode()



"""
add space after sentence
currently, this program is only robust against double spaces
e.g. "text.text" fails but "text.  text" works

Params:
- self

Output:
- string : added space
"""
def add_space(text: str) -> str:
    return re.sub(r'(?<=[.!?])(?=[^\s])', r' ', text)



"""
count syllable per word

Params:
- string : a word

Output:
- int : number of syllables
"""
def syllable_helper(word: str) -> int:
    counter = 0
    vowels = "aeiouyAEIOUY"
    if word[0] in vowels:
        counter += 1
    for idx in range(1, len(word)):
        if word[idx] in vowels and word[idx - 1] not in vowels:
            counter += 1
            if word.endswith("e"):
                counter -= 1
    if counter == 0:
        counter += 1
    return counter



class request:
    """
    initiate

    Params:
    - self
    - text : user-input
    - remove_space : remove space by default (for related functions)

    Output:

    """
    def __init__(self, text: str, remove_space: bool = True):
        self.text = add_space(remove_non_ascii_helper(text))
        self.remove_space = remove_space
        


    """
    count characters (includes punctuation)

    Params:
    - self
    - space : remove space by default

    Output:
    - int : total number of characters
    """
    def count_character(self) -> int:
        if self.remove_space:
            counter = len(self.text.translate(str.maketrans('', '', ' ')))
        else:
            counter = len(self.text)
        if counter == 0:
            warnings.warn(
            "0 character detected. Defaulted to 1"
            )
            counter += 1
        return counter



    """
    count letters (excludes punctuation)

    Params:
    - self

    Output:
    - int : total number of letters
    """
    def count_letter(self) -> int:
        text_no_space = self.text.translate(str.maketrans('', '', ' '))
        counter = len(text_no_space.translate(str.maketrans('', '', string.punctuation)))
        if counter == 0:
            warnings.warn(
            "0 letter detected. Defaulted to 1"
            )
            counter += 1
        return counter

    

    """
    count word

    Params:
    - self

    Output:
    - int : total number of word
    """
    def count_word(self) -> int:
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        counter = len(text_no_punc.split())
        if counter == 0:
            warnings.warn(
            "0 word detected. Defaulted to 1"
            )
            counter += 1
        return counter



    """
    count syllable

    Params:
    - self

    Output:
    - int : total number of syllables
    """
    def count_syllable(self) -> int:
        counter = 0
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        for item in text_no_punc.split():
            counter += syllable_helper(item)
        if counter == 0:
            warnings.warn(
            "0 syllable detected. Defaulted to 1"
            )
            counter += 1
        return counter



    """
    count sentence

    Params:
    - self

    Output:
    - int: total number of sentences
    """
    def count_sentence(self) -> int:
        counter = 0
        sentence_list = re.findall(r'\b[^.!?]+[.!?]*', self.text, re.UNICODE)
        for item in sentence_list:
            if len(item.split()) > 2:
                counter += 1
        if counter == 0:
            warnings.warn(
            "0 sentence detected. Defaulted to 1"
            )
            counter += 1
        return counter
    


    """
    count easy and difficult words seperately

    Params:
    - self

    Output:
    - int: counts easy and difficult words
    """
    def count_easy_diff_word(self) -> int:
        easy_counter = 0
        diff_counter = 0
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        word_list = text_no_punc.split()
        for item in word_list:
            if syllable_helper(item) < 3:
                easy_counter += 1
            else:
                diff_counter += 1
        if easy_counter == 0:
            warnings.warn(
            "0 easy word detected. Defaulted to 1"
            )
            easy_counter += 1
        if diff_counter == 0:
            warnings.warn(
            "0 difficult word detected. Defaulted to 1"
            )
            diff_counter += 1
        return easy_counter, diff_counter



    """
    count polysyllable words

    Params:
    - self

    Output:
    - int: counts easy and difficult words
    """
    def count_poly_word(self) -> int:
        poly_counter = 0
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        word_list = text_no_punc.split()
        for item in word_list:
            if syllable_helper(item) > 3:
                poly_counter += 1
        if poly_counter == 0:
            warnings.warn(
            "0 polysyllablic word detected. Defaulted to 1"
            )
            poly_counter += 1
        return poly_counter



    """
    Flesch-Kincaid Grade Level

    Citation: Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel <https://apps.dtic.mil/sti/pdfs/ADA006655.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version
    - texttype: default to story, choose text type (story, poetry, informational, or drama)

    Output:
    - float : calculation result

    a * (# of word / # of sentence) + b * (# of syllable / # of word) + c
    """
    def flesch_kincaid_grade_level(self, adjusted = True, texttype = 'story') -> float:
        word_count = self.count_word()
        a, b, c = coefs.coefs_flesch_kincaid_grade_level(adjusted, texttype)
        result = a * (word_count / self.count_sentence()) + b * (self.count_syllable() / word_count) + c
        return result



    """
    Fog Count

    Citation: Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel <https://apps.dtic.mil/sti/pdfs/ADA006655.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version
    - texttype: default to story, choose text type (story, poetry, informational, or drama)

    Output:
    - float : calculation result

    a * (data[0] + b * data[1]) + c
    """
    def fog_count(self, adjusted = True, texttype = 'story') -> float:
        easy_word_count, diff_word_count = self.count_easy_diff_word()
        word_count = self.count_word()
        sent_count = self.count_sentence()
        a, b, c = coefs.coefs_fog_count(adjusted, texttype)
        result = a * (word_count / sent_count + b * (diff_word_count / word_count)) + c
        return result
    


    """
    Smog Index

    Citation: SMOG grading-a new readability formula <https://www.jstor.org/stable/40011226>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version
    - texttype: default to story, choose text type (story, poetry, informational, or drama)

    Output:
    - float : calculation result

    a * ((b * data) ** 0.5) + c
    """
    def smog_index(self, adjusted = True, texttype = 'story') -> float:
        a, b, c = coefs.coefs_smog_index(adjusted, texttype)
        result = a * ((b * (self.count_poly_word() / self.count_sentence())) ** 0.5) + c
        return result


    
    """
    Coleman Liau Index

    Citation: A computer readability formula designed for machine scoring <https://psycnet.apa.org/record/1975-22007-001>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version
    - texttype: default to story, choose text type (story, poetry, informational, or drama)

    Output:
    - float : calculation result

    a * ((data[0]) * 100.0) + b * ((data[1]) * 100.0) + c
    """
    def coleman_liau_index(self, adjusted = True, texttype = 'story') -> float:
        word_count = self.count_word()
        a, b, c = coefs.coefs_coleman_liau_index(adjusted, texttype)
        result = a * ((self.count_letter() / word_count) * 100.0) + b * ((self.count_sentence() / word_count) * 100.0) + c
        return result


    
    """
    Automated Readability Index

    Citation: Automated Readability Index <https://apps.dtic.mil/sti/pdfs/AD0667273.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version
    - texttype: default to story, choose text type (story, poetry, informational, or drama)

    Output:
    - float : calculation result

    a * (data[0]) + b * (data[1]) + c
    """
    def automated_readability_index(self, adjusted = True, texttype = 'story') -> float:
        word_count = self.count_word()
        a, b, c = coefs.coefs_automated_readability_index(adjusted, texttype)
        result = a * (self.count_letter() / word_count) + b * (word_count / self.count_sentence() ) + c
        return result



    """shortcut names to functions"""
    def FKGL(self, adjusted = True, texttype = 'story') -> object: 
        return self.flesch_kincaid_grade_level(adjusted, texttype)
    def FOGC(self, adjusted = True, texttype = 'story') -> object: 
        return self.fog_count(adjusted, texttype)
    def SMOG(self, adjusted = True, texttype = 'story') -> object: 
        return self.smog_index(adjusted, texttype)
    def COLE(self, adjusted = True, texttype = 'story') -> object: 
        return self.coleman_liau_index(adjusted, texttype)
    def AUTO(self, adjusted = True, texttype = 'story') -> object: 
        return self.automated_readability_index(adjusted, texttype)