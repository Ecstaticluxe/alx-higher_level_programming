#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        sentence = None
    return sen_len, sentence
