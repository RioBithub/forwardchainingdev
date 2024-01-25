# inference_engine.py

# Complete dictionary buat memetakan kode aturan ke gejala dan kode penyakit yang sesuai
rules = {
    'R1': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G005'], 'disease_code': 'P001'},
    'R2': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G006', 'G007', 'G008', 'G009', 'G010', 'G011', 'G012', 'G013'], 'disease_code': 'P002'},
    'R3': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G006', 'G014', 'G015', 'G016'], 'disease_code': 'P003'},
    'R4': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G006', 'G017', 'G018', 'G019', 'G020'], 'disease_code': 'P004'},
    'R5': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G025', 'G026', 'G027', 'G028', 'G029'], 'disease_code': 'P005'},
    'R6': {'symptoms': ['G001', 'G002', 'G003', 'G004', 'G025', 'G026', 'G027', 'G028', 'G029'], 'disease_code': 'P006'},
    'R7': {'symptoms': ['G001', 'G030', 'G031', 'G032', 'G033', 'G034', 'G035', 'G036', 'G037'], 'disease_code': 'P007'},
    'R8': {'symptoms': ['G001', 'G030', 'G031', 'G032', 'G041', 'G043', 'G044', 'G045', 'G046'], 'disease_code': 'P008'},
    'R9': {'symptoms': ['G001', 'G030', 'G031', 'G047', 'G048', 'G049', 'G050'], 'disease_code': 'P010'},
    'R10': {'symptoms': ['G001', 'G006', 'G030', 'G049', 'G050'], 'disease_code': 'P010'},
  
}

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
