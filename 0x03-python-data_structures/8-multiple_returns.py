#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence[0] == 0:
        return (len(sentence), None)
    else:
        my_tuple = (len(sentence), sentence[0])
        return my_tuple
