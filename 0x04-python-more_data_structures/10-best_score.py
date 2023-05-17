#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score = None
    best_student = None
    for key in a_dictionary:
        if best_score is None or best_score < a_dictionary[key]:
            best_score = a_dictionary[key]
            best_student = key
    return best_student
