#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == None:
        sentence[0] = None
    my_tuple = (len(sentence), sentence[0])
    return my_tuple
