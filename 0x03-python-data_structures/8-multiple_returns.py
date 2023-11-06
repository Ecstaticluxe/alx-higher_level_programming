#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
        sen_len = 0
    else:
        sen_len = len(sentence)
    return (sen_len, sentence[:1] if sentence else None)
