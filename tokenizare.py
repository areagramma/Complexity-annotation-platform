import spacy
nlp = spacy.load("ro_core_news_sm")

def tokenize(propozitie):
    doc = nlp(propozitie)
    tokens = [t.text for t in doc]
    return tokens