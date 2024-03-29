# rules.py

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

symptoms = {
    'G001': 'High fever',
    'G002': 'Runny and stuffy nose',
    'G003': 'Loss of appetite and nausea',
    'G004': 'Sore throat and cough',
    'G005': 'Aches and pains',
    'G006': 'Vomiting',
    'G007': 'Difficulty breathing or rapid breathing',
    'G008': 'Chills',
    'G009': 'Chest pain',
    'G010': 'Breathing sounds by a ringing sound',
    'G011': 'Difficulty breathing',
    'G012': 'Stomach pain due to persistent coughing',
    'G013': 'Brownish-colored',
    'G014': 'Red rash',
    'G015': 'Have watery spots and sores around the mouth, hands, and feet',
    'G016': 'Red blisters on tongue',
    'G017': 'Sneezing',
    'G018': 'Watery eyes',
    'G019': 'Difficulty seeing bright light',
    'G020': 'A reddish-brown rash appears on the third day',
    'G021': 'The spots will be red and more intense, but not itchy',
    'G022': 'Flu symptoms subside but cough worse',
    'G023': 'Persistent hard cough',
    'G024': 'Choking or vomiting',
    'G025': 'Formation of a grayish white membrane',
    'G026': 'Swollen lymph glands in the ears and behind the neck',
    'G027': 'Runny nose',
    'G028': 'Weakness and tiredness',
    'G029': 'Hoarseness',
    'G030': 'Diarrhea',
    'G031': 'Urine Dark',
    'G032': 'Dehydration',
    'G033': 'Irritable and irritable',
    'G034': 'Severe weight loss',
    'G035': 'Infrequent urination',
    'G036': 'Heart beats faster',
    'G037': 'Difficulty shedding tears',
    'G038': 'Sunken eyes',
    'G039': 'Wrinkles and dryness',
    'G040': 'Face is thinner than usual',
    'G041': 'Arrhythmia (heart rhythm disturbance)',
    'G042': 'Low blood pressure',
    'G043': 'Lethargy',
    'G044': 'U only a small amount of',
    'G045': 'Seizures',
    'G046': 'Severe diarrhea symptoms',
    'G047': 'Pale stools',
    'G048': 'Jaundice',
    'G049': 'Itchy rash',
    'G050': 'Upper right abdominal area will feel pain especially'
}

diseases = {
    'P001': 'Influenza',
    'P002': 'Pneumonia (Acute Respiratory Infection)',
    'P003': 'Singapore Flu (Foot, Hand and Mouth Disease)',
    'P004': 'Rubeola (Measles, Measles 9 Days, Measles)',
    'P005': 'Pertussis (Whooping Cough)',
    'P006': 'Diphtheria',
    'P007': 'Muntaber',
    'P008': 'Cholera',
    'P009': 'Hepatitis A',
    'P010': 'Typhoid',
    'P011': 'Rubella (German Measles)',
}

# Dictionary for disease codes and their treatments
treatments = {
    'P001': 'Isolate children with influenza, ensure rest, hydration, acetaminophen as advised. If symptoms worsen, consult a doctor.',
    'P002': 'For pneumonia, provide hydration, rest, and antibiotics. Monitor symptoms and seek medical advice if no improvement within 48 hours.',
    'P003': 'Singapore Flu treatment includes pain relief and cold drinks to soothe the throat, avoiding aspirin for young children.',
    'P004': 'Rubella requires medical consultation. Manage fever with paracetamol, and protect the skin with Vaseline.',
    'P005': 'Isolate for whooping cough, assist with phlegm expulsion, and administer antibiotics as the main treatment.',
    'P006': 'Consult a doctor immediately for symptoms of diphtheria, which is highly contagious and potentially life-threatening.',
    'P007': 'For vomiting, provide ORS and breast milk or lactose-free formula for infants. Seek medical care for persistent symptoms.',
    'P008': 'Cholera treatment involves ORS and antibiotics. Administer fluids and electrolytes for mild symptoms.'
}

warnings = {
    "P001": "If your child's symptoms worsen and do not improve over a long period, see a doctor immediately.",
    "P002": "If pneumonia symptoms do not improve at all within 48 hours, you are advised to contact your doctor again.",
    "P003": "Do not give aspirin to children and adolescents under 16 years of age.",
    "P004": "It is not necessary to take the child to the doctor as it may infect other children.",
    "P005": "The main treatment given is antibiotics to fight the infection-causing bacteria. Provide your child with easy-to-swallow food and plenty of fluids.",
    "P006": "This disease is highly contagious and includes serious infections that can be life-threatening, so it must be treated as soon as possible to prevent complications.",
    "P007": "Immediately take to the doctor if the child has persistent vomiting and diarrhea. Children should also be taken to the doctor or hospital immediately if they are significantly dehydrated, as there may be serious underlying causes. In cases of persistent vomiting, the doctor may perform an endoscopic examination to check the gastrointestinal tract.",
    "P008": "Administer antibiotics to reduce the number of bacteria, while shortening diarrhea due to cholera."
}