import pandas as pd
from question_similarity.malstm import Match

class FAQ:
    def getsimilarity(inputQuery):
        threshold=0.5
        df = pd.read_csv("faqs/question-answer.csv")
        match = Match()
        max_score = 0
        question_idx = 0
        for i, q in enumerate(df['Question']):
            s = match.compare(inputQuery, q)
            if s > max_score:
                max_score = s
                question_idx = i

        print("FAQ similarity score:", max_score)
        if max_score > threshold:
            return df['Text'][question_idx]
        else:
            return None


