#!/usr/bin/python3


def multiple_returns(sentence):
    ch = None if len(sentence) == 0 else sentence[0]
    return (len(sentence), ch)
