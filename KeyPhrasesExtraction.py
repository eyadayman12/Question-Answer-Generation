import pke
from rake_nltk import Rake

def extractor(algorithm, data, count):
    algorithm.load_document(input=data)              
    algorithm.candidate_selection()                     
    algorithm.candidate_weighting()                     
    algorithm_keyPhrases = algorithm.get_n_best(n=count, stemming=False)
    return algorithm_keyPhrases


def tfIdfExtractorKeyPhrases(data, count):
    tfIdf_extractor = pke.unsupervised.TfIdf() 
    tfIdf_keyPhrases = extractor(tfIdf_extractor, data, count)
    return tfIdf_keyPhrases


def topicalPageRankExtractorKeyPhrases(data, count):
    topicalPageRank_extractor = pke.unsupervised.TopicalPageRank() 
    topicalPageRank_keyPhrases = extractor(topicalPageRank_extractor, data, count)
    return topicalPageRank_keyPhrases



def positionRankExtractorKeyPhrases(data, count):
    PositionRank_extractor = pke.unsupervised.PositionRank() 
    PositionRank_keyPhrases = extractor(PositionRank_extractor, data, count)
    return PositionRank_keyPhrases


def textRankExtractorKeyPhrases(data, count):
    textRank_extractor = pke.unsupervised.TextRank() 
    textRank_keyPhrases = extractor(textRank_extractor, data, count)
    return textRank_keyPhrases



def topicRankExtractorKeyPhrases(data, count):
    topicRank_extractor = pke.unsupervised.TopicRank() 
    topicRank_keyPhrases = extractor(topicRank_extractor, data, count)
    return topicRank_keyPhrases


def firstPhrasesExtractorKeyPhrases(data, count):
    firstPhrases_extractor = pke.unsupervised.FirstPhrases() 
    firstPhrases_keyPhrases = extractor(firstPhrases_extractor, data, count)
    return firstPhrases_keyPhrases


def YakeExtractorKeyPhrases(data, count):
    yake_extractor = pke.unsupervised.YAKE() 
    yake_keyPhrases = extractor(yake_extractor, data, count)
    return yake_keyPhrases


def rakeExtractorKeyPhrases(data):
    rakeExtractor = Rake()
    rakeExtractor.extract_keywords_from_text(data)
    rakeKeyPhrases = rakeExtractor.get_ranked_phrases_with_scores()
    return rakeKeyPhrases