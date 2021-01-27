user_choice = -1
tasks = []
tasks.append("Pierwsze zadanie")
tasks.append("Drugie zadanie")
tasks.append("Trzecie  zadanie")
tasks.append("Czwarte zadanie")

def show_tasks():
    index = 0
    for task in tasks:
        print(task + " - [" + str(index) + "]")
        index += 1

def add_task():
    user_task = input("Podaj treść zadania: ")
    tasks.append(user_task)

def remove_task():
    show_tasks()
    user_choice_index_task = int(input("Poadaj numer zadania które chcesz usunąć: "))
    tasks.pop(user_choice_index_task)
print()
print("Witamy w aplikacji To Do List")
print()
while user_choice != 4:
    if user_choice == 1:
        show_tasks()
        print()
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        remove_task()
    else:
        print("Błędna pozycja w menu")

    print("1. Wyświtl wszytkie zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")
    print()
    user_choice = int(input("Wybierz opcję z menu: "))
    print()


