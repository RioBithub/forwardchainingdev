# main.py

from rules import rules, symptoms, diseases, treatments, warnings
from inference_engine import run_forward_chaining

def display_help():
    print("\nHELP MENU:")
    print("Type 'list symptoms' to display codes and descriptions of symptoms.")
    print("Type 'diagnose' to start the diagnosis process.")
    print("Type 'diagnoseadv' to start the advanced diagnosis process.")
    print("Type 'exit' to exit the program.\n")

def list_symptoms():
    for code, description in symptoms.items():
        print(f"{code}: {description}")

def diagnose_for_user():
    user_symptoms = []
    print("Please answer with 'y' for yes, 'n' for no, or 'x' to cancel and return to the main menu.")
    for index, (code, description) in enumerate(symptoms.items(), start=1):
        while True:
            response = input(f"{index}. Are you experiencing {description}? (y/n): ").lower().strip()
            if response == 'y':
                user_symptoms.append(code)
                break
            elif response == 'n':
                break
            elif response == 'x':
                print("\nReturning to the main menu...")
                return 'abort'  # Returns None to signify cancellation
            else:
                print("Invalid response. Please answer with 'y', 'n', or 'x'.")
    return user_symptoms

def get_user_input():
    print("\nEnter symptom codes separated by a comma and space (example: G001, G002): ")
    input_symptoms = input()
    return input_symptoms.split(', ')

def display_disease_info(disease_code):
    disease_name = diseases.get(disease_code, "Unknown Disease")
    treatment_info = treatments.get(disease_code, "Treatment information not available.")
    warning_info = warnings.get(disease_code, "No specific warnings.")
    print(f"\nDisease: {disease_name}")
    print(f"Treatment: {treatment_info}")
    print(f"Warning: {warning_info}\n")

def main():
    print("""
***************************************************
* Welcome to the Forward Chaining Expert System! *
* Presented by: Alvin & The Chipmunks            *
***************************************************

This system helps you identify diseases based on symptoms.
Just follow the instructions, and let's get started!
""")
    print("Type 'help' for options or 'exit' to exit the program.")

    while True:
        command = input("\nHow can we assist you? ").lower().strip()

        if command == 'help':
            display_help()
        
        elif command == 'list symptoms':
            list_symptoms()

        elif command == 'diagnose':
            user_symptoms = diagnose_for_user()
            if user_symptoms == 'abort':
                continue
            match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)
            if match_type == "exact":
                print("\nPossible disease diagnosis based on the entered symptoms:")
                for disease_code in diagnosed_diseases:
                    display_disease_info(disease_code)
            else:
                print("\nNo exact match found with the given symptoms.")
                show_possible = input("Would you like to see possible diseases based on the symptoms? (y/n): ").lower()
                if show_possible == 'y':
                    print("\nPossible diseases based on symptoms:")
                    for disease_code in diagnosed_diseases:
                        display_disease_info(disease_code)
                else:
                    print("Symptom-based diagnosis completed.")

        elif command == 'diagnoseadv':
            user_symptoms = get_user_input()
            match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)
            if match_type == "exact":
                print("\nPossible disease diagnosis based on the entered symptoms:")
                for disease_code in diagnosed_diseases:
                    display_disease_info(disease_code)
            else:
                print("\nNo exact match found with the given symptoms.")
                show_possible = input("Would you like to see possible diseases based on the symptoms? (y/n): ").lower()
                if show_possible == 'y':
                    print("\nPossible diseases based on symptoms:")
                    for disease_code in diagnosed_diseases:
                        display_disease_info(disease_code)
                else:
                    print("Symptom-based diagnosis completed.")

        elif command == 'exit':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for a list of valid commands.")

if __name__ == "__main__":
    main()
