user_choice = -1
tasks = []
tasks.append("Pierwsze zadanie")
tasks.append("Drugie zadanie")
tasks.append("Trzecie  zadanie")
tasks.append("Czwarte zadanie")
def show_tasks():
    for task in tasks:
        print(task)
print()
print("Witamy w aplikacji To Do List")
print()
while user_choice != 4:
    if user_choice == 1:
        show_tasks()
    elif user_choice == 2:
        print("Dodaj zadania")
    elif user_choice == 3:
        print("Usuń zadanie")
    else:
        print("Błędna pozycja w menu")

    print("1. Wyświtl wszytkie zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")
    print()
    user_choice = int(input("Wybierz opcję z menu: "))


