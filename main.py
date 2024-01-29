# main.py

from rules import rules, symptoms, diseases, treatments
from inference_engine import run_forward_chaining

def display_help():
    print("\nMENU BANTUAN:")
    print("Ketik 'list symptoms' untuk menampilkan kode dan deskripsi gejala.")
    print("Ketik 'diagnose' untuk memulai proses diagnosis.")
    print("Ketik 'diagnoseadv' untuk memulai proses diagnosis lanjutan.")
    print("Ketik 'exit' untuk keluar dari program.\n")

def list_symptoms():
    for code, description in symptoms.items():
        print(f"{code}: {description}")

def diagnose_for_user():
    user_symptoms = []
    print("Silakan jawab dengan 'y' untuk ya, 'n' untuk tidak, atau 'x' untuk membatalkan dan kembali ke menu utama.")
    for index, (code, description) in enumerate(symptoms.items(), start=1):
        while True:
            response = input(f"{index}. Apakah Anda mengalami {description}? (y/n/x): ").lower().strip()
            if response == 'y':
                user_symptoms.append(code)
                break
            elif response == 'n':
                break
            elif response == 'x':
                return 'abort'  # Mengembalikan None untuk menandakan pembatalan
            else:
                print("Respons tidak valid. Silakan jawab dengan 'y', 'n', atau 'x'.")
    return user_symptoms

def get_user_input():
    print("\nMasukkan kode gejala yang dipisahkan dengan koma dan spasi (contoh: G001, G002): ")
    input_symptoms = input()
    return input_symptoms.split(', ')

def display_disease_info(disease_code):
    disease_name = diseases.get(disease_code, "Penyakit Tidak Diketahui")
    treatment_info = treatments.get(disease_code, "Informasi pengobatan tidak tersedia.")
    print(f"\nPenyakit: {disease_name}")
    print(f"Pengobatan: {treatment_info}\n")

def main():
    print("""
***************************************************
* Selamat Datang di Sistem Pakar Forward Chaining!*
* Disajikan oleh: Alvin & The Chipmunks           *
***************************************************

Sistem ini membantu Anda mengidentifikasi penyakit berdasarkan gejala.
Ikuti saja petunjuknya, dan mari kita mulai!
""")
    print("Ketik 'help' untuk opsi atau 'exit' untuk keluar dari program.")

    while True:
        command = input("\nBagaimana kami bisa membantu Anda? ").lower().strip()

        if command == 'help':
            display_help()
        
        elif command == 'list symptoms':
            list_symptoms()

        elif command == 'diagnose':
            user_symptoms = diagnose_for_user()
            match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)
            if user_symptoms is 'abort':
                continue
            if match_type == "exact":
                print("\nDiagnosis penyakit yang mungkin berdasarkan gejala yang dimasukkan:")
                for disease_code in diagnosed_diseases:
                    display_disease_info(disease_code)
            else:
                print("\nTidak ada kecocokan yang pasti dengan gejala yang diberikan.")
                show_possible = input("Apakah Anda ingin melihat penyakit yang mungkin berdasarkan gejala? (y/n): ").lower()
                if show_possible == 'y':
                    print("\nPenyakit yang mungkin berdasarkan gejala:")
                    for disease_code in diagnosed_diseases:
                        display_disease_info(disease_code)
                else:
                    print("Diagnosis berdasarkan gejala telah selesai.")

        elif command == 'diagnoseadv':
            user_symptoms = get_user_input()
            match_type, diagnosed_diseases = run_forward_chaining(user_symptoms)
            if match_type == "exact":
                print("\nDiagnosis penyakit yang mungkin berdasarkan gejala yang dimasukkan:")
                for disease_code in diagnosed_diseases:
                    display_disease_info(disease_code)
            else:
                print("\nTidak ada kecocokan yang pasti dengan gejala yang diberikan.")
                show_possible = input("Apakah Anda ingin melihat penyakit yang mungkin berdasarkan gejala? (y/n): ").lower()
                if show_possible == 'y':
                    print("\nPenyakit yang mungkin berdasarkan gejala:")
                    for disease_code in diagnosed_diseases:
                        display_disease_info(disease_code)
                else:
                    print("Diagnosis berdasarkan gejala telah selesai.")

        elif command == 'exit':
            print("Keluar dari sistem. Selamat tinggal!")
            break
        else:
            print("Perintah tidak dikenal. Ketik 'help' untuk daftar perintah yang valid.")

if __name__ == "__main__":
    main()
