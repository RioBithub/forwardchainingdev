# inference_engine.py


from rules import *

def run_forward_chaining(user_symptoms):
    exact_match = None
    possible_matches = []

    for rule in rules.values():
        rule_symptoms = set(rule['symptoms'])
        if rule_symptoms == set(user_symptoms):
            exact_match = rule['disease_code']
            break
        elif rule_symptoms.intersection(set(user_symptoms)):
            possible_matches.append(rule['disease_code'])

    if exact_match:
        return ("exact", [exact_match])
    else:
        return ("possible", list(set(possible_matches)))
