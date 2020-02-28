import torch
from transformers import BertTokenizer, BertForQuestionAnswering


def findans(question):
    text_file = "../faqs/label-text.txt"
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    with open(text_file, 'r') as file:
        passage = file.read().replace('\n', ' ')
    input_text = "[CLS] " + question + " [SEP] " + passage + " [SEP]"
    input_ids = tokenizer.encode(input_text)
    token_type_ids = [0 if i <= input_ids.index(102) else 1 for i in range(len(input_ids))]
    start_scores, end_scores = model(torch.tensor([input_ids]), token_type_ids=torch.tensor([token_type_ids]))
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    score = compute_score(start_scores, end_scores)
    answer = ' '.join(all_tokens[torch.argmax(start_scores): torch.argmax(end_scores) + 1])
    return score, answer


def compute_score(start_scores, end_scores):
    start_scores = torch.nn.functional.softmax(start_scores, dim=1)
    end_scores = torch.nn.functional.softmax(end_scores, dim=1)
    score = torch.max(start_scores) + torch.max(end_scores)
    return round(score.item(), 3)


class QA:

    def ask(question, threshold=0):
        score, answer = findans(question)
        if score > threshold:
            return answer
        else:
            return None