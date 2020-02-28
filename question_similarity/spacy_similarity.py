import spacy
class Match:
    def __init__(self): #Load language model
        self.nlp = spacy.load("en_core_web_md")

    def compare(self, s1, s2): #Measure similarity score between two strings.
        p1 = self.nlp(s1)
        p2 = self.nlp(s2)
        return p1.similarity(p2)

