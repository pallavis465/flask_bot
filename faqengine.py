import random
from label_matching import *
from question_answering.bert import *


def greeting(sentence):
    GREETING_INPUTS = ("hello", "hi", "greetings", "hey",)
    GREETING_RESPONSES = ["Hi", "Hey", "Hi There", "Hello", "I am glad to help you"]
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)



def query(inputQuery):
    reply=FAQ.getsimilarity(inputQuery)
    if(reply!=None):
        return reply
    else:
        qareply=QA.ask(inputQuery)
        if(qareply!=None):
           return qareply
        else:
            return None



class FaqEngine:

    def getreply(self, user_query):
        user_query = user_query.lower()
        if (user_query != 'bye'):
            if (user_query == 'thanks' or user_query == 'thank you'):
                return "You are welcome"
            else:
                if greeting(user_query) != None:
                    return greeting(user_query)
                else:
                    return query(user_query)
        else:
            return "Bye! take care"