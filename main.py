# main.py

from inference_engine import *

# Dictionary buat disease sama kode disease nya
symptoms = {
    'G001': 'High fever',
    'G002': 'Runny and stuffy',
    'G003': 'No appetite and nausea',
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
    'P008': 'Ko lera',
    'P009': 'Hepatitis A',
    'P010': 'Typhoid',
    'P011': 'Rubella (German Measles)',
}

# Dictionary dari kode penyakit dan solusinya
treatments = {
    'P001': 'Isolate children with influenza, ensure rest, hydration, acetaminophen as advised. If symptoms worsen, consult a doctor.help',
    'P002': 'For pneumonia, provide hydration, rest, and antibiotics. Monitor symptoms and seek medical advice if no improvement within 48 hours.',
    'P003': 'Singapore Flu treatment includes pain relief and cold drinks to soothe the throat, avoiding aspirin for young children.',
    'P004': 'Rubella requires medical consultation. Manage fever with paracetamol, and protect the skin with Vaseline.',
    'P005': 'Isolate for whooping cough, assist with phlegm expulsion, and administer antibiotics as the main treatment.',
    'P006': 'Consult a doctor immediately for symptoms of diphtheria, which is highly contagious and potentially life-threatening.',
    'P007': 'For vomiting, provide ORS and breast milk or lactose-free formula for infants. Seek medical care for persistent symptoms.',
    'P008': 'Cholera treatment involves ORS and antibiotics. Administer fluids and electrolytes for mild symptoms.'
}

def display_help():
    print("\nHELP MENU:")
    print("Type 'list symptoms' to display symptom codes and descriptions.")
    print("Type 'diagnose' to start the diagnosis process.")
    print("Type 'diagnoseadv' to start advanced diagnosis process.")
    print("Type 'exit' to quit the program.\n")

def list_symptoms():
    for code, description in symptoms.items():
        print(f"{code}: {description}")
def diagnose_for_user():
    user_symptoms = []
    print("Please answer with 'y' for yes or 'n' for no for the following symptoms:")

    for index, (code, description) in enumerate(symptoms.items(), start=1):
        while True:
            response = input(f"{index}. Do you have {description}? (y/n): ").lower().strip()
            if response in ['y', 'n']:
                if response == 'y':
                    user_symptoms.append(code)
                break 
            else:
                print("Invalid response. Please answer with 'y' or 'n'.")

    return user_symptoms

def get_user_input():
    print("\nEnter the symptom codes separated by commas and space (e.g., G001, G002): ")
    input_symptoms = input()
    return input_symptoms.split(', ')

def display_disease_info(disease_code):
    disease_name = diseases.get(disease_code, "Unknown Disease")
    treatment_info = treatments.get(disease_code, "No treatment information available.")
    print(f"\nDisease: {disease_name}")
    print(f"Treatment: {treatment_info}\n")

def main():
    print("Welcome to the Pediatric Disease Diagnosis System. \n Code developed by Kelompok 3 Kebut!!!")
    print("Type 'help' for options or 'exit' to quit.")

    while True:
        command = input("\nAda yang bisa kami bantu? ").lower().strip()

        if command == 'help':
            display_help()
        elif command == 'list symptoms':
            list_symptoms()
        elif command == 'diagnose':
            user_symptoms = diagnose_for_user()
            match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)

            if match_type == "exact":
                 print("\nDiagnosis kemungkinan besar penyakit berdasarkan gejala yang dimasukkan:")
            for disease_code in diagnosed_diseases:
                 display_disease_info(disease_code)
            else:
                 print("\nTidak ada kecocokan yang pasti dengan gejala yang diberikan.")
                 show_possible = input("Apakah Anda ingin melihat kemungkinan penyakit berdasarkan gejala? (y/n): ").lower()
            if show_possible == 'y':
                  print("\nPenyakit yang mungkin berdasarkan gejala:")
                  for disease_code in diagnosed_diseases:
                      display_disease_info(disease_code)
            else:
                print("Diagnosis berdasarkan gejala selesai.")
        elif command == 'diagnoseadv':
             user_symptoms = get_user_input()
             match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)
             if match_type == "exact":
                 print("\nDiagnosis kemungkinan besar penyakit berdasarkan gejala yang dimasukkan:")
             for disease_code in diagnosed_diseases:
                display_disease_info(disease_code)
             else:
                print("\nTidak ada kecocokan yang pasti dengan gejala yang diberikan.")
                show_possible = input("Apakah Anda ingin melihat kemungkinan penyakit berdasarkan gejala? (y/n): ").lower()
             if show_possible == 'y':
               print("\nPenyakit yang mungkin berdasarkan gejala:")
               for disease_code in diagnosed_diseases:
                    display_disease_info(disease_code)
               else:
                print("Diagnosis berdasarkan gejala selesai.")
        elif command == 'exit':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for a list of valid commands.")

if __name__ == "__main__":
    main()