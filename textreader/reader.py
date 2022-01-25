import re, string
import warnings
import pandas as pd
import os
import math
from supar import Parser
import spacy
from spacy.tokens import Doc, Span
import nltk

import textreader.coefs as coefs

dir_path = os.path.dirname(os.path.realpath(__file__))

SPACY = spacy.load(dir_path+'/data/en_core_web_sm-3.0.0')
SUPAR = Parser.load('crf-con-en')

Span.set_extension("con_tree", getter=lambda x: SUPAR.predict([i.text for i in x],verbose=False)[0])


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
    - remove_space : remove space by default (when counting character)
    - parser : use parser by default

    Output:

    """
    def __init__(self, text: str, remove_space: bool = True, parser: bool = True):
        self.text = add_space(remove_non_ascii_helper(text.lower()))
        self.remove_space = remove_space
        if parser == True:
            self.spacy_doc = SPACY(self.text)


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
    - int : total number of unique word
    """
    def count_word(self) -> int:
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        word_list = text_no_punc.split()
        counter = len(word_list)
        counter_unique = len(list(dict.fromkeys(word_list)))
        if counter == 0:
            warnings.warn(
            "0 word detected. Defaulted to 1"
            )
            counter += 1
        return counter,counter_unique



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
    - int: counts number of polysyllable words
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
    calculate total Kuperman's Age-of-Acquisition

    Params:
    - self

    Output:
    - int: counts total Kuperman AoA
    """
    def calculate_Kuperman_AoA(self):
        text_no_punc = self.text.translate(str.maketrans('', '', string.punctuation + string.digits))
        word_list = text_no_punc.split()
        to_AAKuL_C = 0
        DB = pd.read_csv(dir_path+'/data/AoAKuperman.csv')
        DB.set_index('Word', inplace=True, drop=True)
        for word in word_list:
            if word in DB.index:
                scores_for_this_word = list(DB.loc[word, :])
                for i, score in enumerate(scores_for_this_word):
                    scores_for_this_word[i] = 0 if str(score) == 'none' else   scores_for_this_word[i]
                to_AAKuL_C += float(scores_for_this_word[9])
        return to_AAKuL_C   



    """
    calculate total tree height

    Params:
    - self

    Output:
    - int: count total height of trees
    """
    def calculate_tree_height(self):
        to_TreeH_C = 0
        for sent in self.spacy_doc.sents:
            try:
                nltk_tree = nltk.Tree.fromstring(str(sent._.con_tree))
                to_TreeH_C += int(nltk_tree.height())
            except:
                pass
        return to_TreeH_C


    
    """
    count content word

    Params:
    - self

    Output:
    - int: count total number of content words
    """
    def count_content_word(self):
        to_ContW_C = 0
        for token in self.spacy_doc:
            if token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "NUM" or token.pos_ == "ADJ" or token.pos_ == "ADV":
                to_ContW_C += 1
        return to_ContW_C



    """
    count noun phrases

    Params:
    - self

    Output:
    - int: count total number of noun phrases
    """
    def count_noun_phrases(self):
        to_NoPhr_C = 0
        for sent in self.spacy_doc.sents:
            try:
                to_NoPhr_C += str(sent._.con_tree).count("NP")
            except:
                pass
        return to_NoPhr_C



    """
    calculate word familiarity

    Params:
    - self

    Output:
    - int: count sum of SubtlexUS word familiarity in 
    """
    def count_word_familiarity(self):
        to_SbL1C_C = 0
        DB = pd.read_csv(dir_path+'/data/SUBTLEXus.csv')
        DB.set_index('Word_lowercased', inplace=True, drop=True)
        for token in self.spacy_doc:
            if token.text in DB.index:
                scores_for_this_token = list(DB.loc[token.text, :])
                for i, score in enumerate(scores_for_this_token):
                    scores_for_this_token[i] = 0 if str(score) == 'none' else scores_for_this_token[i]
                to_SbL1C_C += float(scores_for_this_token[8])
        return to_SbL1C_C


    """
    Flesch-Kincaid Grade Level

    Citation: Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel <https://apps.dtic.mil/sti/pdfs/ADA006655.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version

    Output:
    - float : calculation result

    a * (# word / # sentence) + b * (# syllable / # word) + c
    """
    def flesch_kincaid_grade_level(self, adjusted = True) -> float:
        word_count = self.count_word()[0]
        a, b, c = coefs.coefs_flesch_kincaid_grade_level(adjusted)
        result = a * (word_count / self.count_sentence()) + b * (self.count_syllable() / word_count) + c
        return result



    """
    Fog Count

    Citation: Derivation of New Readability Formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy Enlisted Personnel <https://apps.dtic.mil/sti/pdfs/ADA006655.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version

    Output:
    - float : calculation result

    a * (# word / # sentence + b * # difficult word / # word) + c
    """
    def fog_index(self, adjusted = True) -> float:
        easy_word_count, diff_word_count = self.count_easy_diff_word()
        word_count = self.count_word()[0]
        sent_count = self.count_sentence()
        a, b, c = coefs.coefs_fog_index(adjusted)
        result = a * (word_count / sent_count + b * (diff_word_count / word_count)) + c
        return result
    


    """
    Smog Index

    Citation: SMOG grading-a new readability formula <https://www.jstor.org/stable/40011226>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version

    Output:
    - float : calculation result

    a * ((b * # polysyllables word / # sentence) ** 0.5) + c
    """
    def smog_index(self, adjusted = True) -> float:
        a, b, c = coefs.coefs_smog_index(adjusted)
        result = a * ((b * (self.count_poly_word() / self.count_sentence())) ** 0.5) + c
        return result


    
    """
    Coleman Liau Index

    Citation: A computer readability formula designed for machine scoring <https://psycnet.apa.org/record/1975-22007-001>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version

    Output:
    - float : calculation result

    a * ((# letter / # word) * 100.0) + b * ((# sentence / # word) * 100.0) + c
    """
    def coleman_liau_index(self, adjusted = True) -> float:
        word_count = self.count_word()[0]
        a, b, c = coefs.coefs_coleman_liau_index(adjusted)
        result = a * ((self.count_letter() / word_count) * 100.0) + b * ((self.count_sentence() / word_count) * 100.0) + c
        return result


    
    """
    Automated Readability Index

    Citation: Automated Readability Index <https://apps.dtic.mil/sti/pdfs/AD0667273.pdf>

    Params:
    - self
    - adjusted : default to True, choose whether to use adjusted version

    Output:
    - float : calculation result

    a * (# letter / # word) + b * (# word / # sentence) + c
    """
    def automated_readability_index(self, adjusted = True) -> float:
        word_count = self.count_word()[0]
        a, b, c = coefs.coefs_automated_readability_index(adjusted)
        result = a * (self.count_letter() / word_count) + b * (word_count / self.count_sentence() ) + c
        return result



    """
    Common Readability Formula

    Params:
    - self

    Output:
    - float : calculation result

    a * (sum Kuperman AoA / # sentence) + b * (sum word frequency / # sentence) + c * (# content word / # sentence) + d * (# noun phrase / # sentence) + e * (sum tree height / # sentence) + f * (# unique word /math.sqrt(2 * # word)) + g
    """
    def common_readability_formula(self) -> float:
        word_count,unique_word_count = self.count_word()
        sent_count = self.count_sentence()
        to_AAKuL_C = self.calculate_Kuperman_AoA()
        to_TreeH_C = self.calculate_tree_height()
        to_ContW_C = self.count_content_word()
        to_NoPhr_C = self.count_noun_phrases()
        to_SbL1C_C = self.count_word_familiarity()
        a, b, c, d, e, f, g = coefs.coefs_common_readability_formula()
        result = a * (to_AAKuL_C/sent_count) + b * (to_SbL1C_C/sent_count) + c * (to_ContW_C/sent_count) + d * (to_NoPhr_C/sent_count) + e * (to_TreeH_C/sent_count) + f * (unique_word_count/math.sqrt(2*word_count)) + g
        return result



    """
    Average Reading Time

    Params:
    - self
    - speed : default to average, (fast, slow are other options)

    Output:
    - float : calculation result

    """
    def read_time(self, speed: str = "average") -> float:
        word_count,unique_word_count = self.count_word()
        if speed == "average":
            result = word_count/240.0
        elif speed == "fast":
            result = word_count/300.0
        elif speed == "slow":
            result = word_count/175.0
        else:
            result = 0
            warnings.warn(
            "TEXTREADER's MESSAGE-> wrong speed (str) parameter entered. Speed can be average (default), fast, or slow."
            )
        return result



    """shortcut names to functions"""
    def FKGL(self, adjusted: bool = True) -> object: 
        return self.flesch_kincaid_grade_level(adjusted)
    def FOGI(self, adjusted: bool = True) -> object: 
        return self.fog_index(adjusted)
    def SMOG(self, adjusted: bool = True) -> object: 
        return self.smog_index(adjusted)
    def COLE(self, adjusted: bool = True) -> object: 
        return self.coleman_liau_index(adjusted)
    def AUTO(self, adjusted: bool = True) -> object: 
        return self.automated_readability_index(adjusted)
    def CoRF(self) -> object: 
        return self.common_readability_formula()
    def RT(self, speed: str = "average") -> object: 
        return self.read_time(speed)