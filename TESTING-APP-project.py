import json

def add_question(test, question, keywords):
    test.append({"question": question, "keywords": keywords})

def save_to_file(test, filename):
    with open(filename, 'w') as file:
        json.dump({"questions": test}, file)

def load_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data["questions"]

def conduct_test(test):
    score = 0
    total_questions = len(test)
    for idx, question_data in enumerate(test, 1):
        print(f"Otázka {idx}: {question_data['question']}")
        user_answer = input("Your answer: ").strip().lower()
        for keyword in question_data['keywords']:
            if keyword.lower() in user_answer:
                score += 1
                break
    print(f"\nYour score: {score}/{total_questions}")

def main():
    while True:
        print("\nMenu:")
        print("1. Vytvořit test")
        print("2. Načíst test")
        print("3. Spustit test")
        print("4. Ukončit")

        choice = input("Volba: ")

        if choice == "1":
            test = []
            num_questions = int(input("Zadej počet otázek: "))

            for _ in range(num_questions):
                question = input("Zadej otázku: ")
                keywords = input("Zadej klíčová slova (oddělena čárkou): ").split(',')
                add_question(test, question, keywords)

            filename = input("Zadej název souboru: ")
            save_to_file(test, filename)

        elif choice == "2":
            filename = input("Zadej název souboru: ")
            test = load_from_file(filename)

        elif choice == "3":
            try:
                conduct_test(test)
            except:
                print("Nejprve načtěte test!")
        elif choice == "4":
            break
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()
