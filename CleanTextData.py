import nltk
from nltk.corpus import stopwords
from urlextract import URLExtract
import re
import contractions
from nltk.tokenize import word_tokenize
from summarizer import Summarizer


stopWords = stopwords.words('english')


def summerize_text(text, min_len, max_len, ratio):
    model = Summarizer()
    result = model(text, min_length=min_len, max_length = max_len , ratio = ratio)
    summarized_text = ''.join(result)
    return summarized_text



def removing_links(data):
    extractor = URLExtract()
    links = []
    for message in data.split():
        links.extend(extractor.find_urls(message))
    data_after_removing_links = ""
    for word in data.split():
        if word not in links:
            data_after_removing_links = data_after_removing_links + word + ' '
    return data_after_removing_links


def remove_stopwords(data):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    cleaned_sentence = ""
    
    for word in filtered_sentence:
        cleaned_sentence = cleaned_sentence + word + ' '
        
    return cleaned_sentence
    


def remove_punctations(data):
    cleaned_data = data
    cleaned_data = re.sub(r'[^\w\s.,]', '', cleaned_data)
    return cleaned_data


def lowercase_the_data(data):
    lowercase_data = data.lower()
    return lowercase_data


def remove_emails(data):
    cleaned_data = data
    cleaned_data = re.sub(r'[A-z0-9\.]+@[A-z0-9]+\.[A-z]+', '', cleaned_data)
    return cleaned_data


def apply_contraction(data):
    data_after_applying_contraction = ""
    for word in data.split():
        data_after_applying_contraction = data_after_applying_contraction + contractions.fix(word) + ' '
    return data_after_applying_contraction