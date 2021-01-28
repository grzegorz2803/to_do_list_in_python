class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[34m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

tasks = []
def read_from_file():
    try: 
        file = open("tasks.txt")
        for line in file:
            tasks.append(line.strip())
    except:
        print(f"{bcolors.WARNING} Bark zadań  do wyświetlenia. Dodaj nowe zadania{bcolors.ENDC}")

def show_tasks():
    index = 0
    for task in tasks:
        print(task + " - [" + str(index) + "]")
        index += 1

def add_task():
    user_task = input("Podaj treść zadania: ")
    tasks.append(user_task)
    print(f"{bcolors.OKGREEN}Zadanie zostało dodane{bcolors.ENDC}")
    print()

def remove_task():
    show_tasks()
    print()
    user_choice_index_task = int(input("Poadaj numer zadania które chcesz usunąć: "))
    remove_user_task = tasks.pop(user_choice_index_task)
    print(f"{bcolors.OKBLUE}" + remove_user_task + f" zostało usunięte{bcolors.ENDC}")
    print()

def show_error():
     print(f"{bcolors.FAIL}Błędna pozycja w menu{bcolors.ENDC}")
     print()

def show_menu():
    print("1. Wyświtl wszytkie zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")
    print()
    user_choice = int(input("Wybierz opcję z menu: "))
    print()
    return user_choice

def save_tasks_to_file():
    file = open("tasks.txt", "w+")
    for task in tasks:
        file.write(task + "\n")
    file.close()

print()
print("Witamy w aplikacji To Do List")
print()
read_from_file()
print()
while True:
    print()
    user_choice = show_menu()
    if user_choice == 1:
        show_tasks()
        print()
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        remove_task()
    elif user_choice == 4:
        save_tasks_to_file()
        break
    else:
       show_error()


