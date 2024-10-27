import datetime


def wyswietl_zadanie():
    plik = "nowy.txt"
    with open(plik, "r", encoding="UTF-8") as dane:
        dane = dane.readlines()
        for wers in dane:
            wers = wers.strip().split(",")  # dzieli na elementy
            print(wers)
    print("oto zapisane zadania")


import datetime


def dodaj_zadanie():
    plik = "nowy.txt"
    lista = []

    nazwa = input("Podaj nazwę zadania: ")

    # Walidacja daty
    while True:
        data = input("Podaj datę (format: YYYY-MM-DD lub 'brak' dla braku daty): ")
        if data.lower() == "brak":
            data = "brak"
            break
        else:
            try:
                # Sprawdzenie, czy data jest w przyszłości
                if data >= datetime.datetime.now().strftime("%Y-%m-%d"):
                    data = datetime.datetime.strptime(data, "%Y-%m-%d").strftime(
                        "%Y-%m-%d"
                    )
                    break
                else:
                    print(
                        "Wprowadzona data nie może być wcześniejsza niż obecna. Spróbuj jeszcze raz."
                    )
            except ValueError:
                print(
                    "Data jest zapisana w niepoprawnym formacie. Spróbuj jeszcze raz (format: YYYY-MM-DD)."
                )

    # Walidacja czasu
    while True:
        czas = input("Podaj czas (format: HH:MM lub 'brak' dla braku czasu): ")
        if czas.lower() == "brak":
            czas = "brak"
            break
        else:
            try:
                czas = datetime.datetime.strptime(czas, "%H:%M").strftime("%H:%M")
                break
            except ValueError:
                print(
                    "Czas jest zapisany w niepoprawnym formacie. Spróbuj jeszcze raz (format: HH:MM)."
                )

    opis = input("Podaj opis: ")

    # Walidacja priorytetu
    while True:
        priorytet = input("Podaj priorytet (NI, WY, NO): ").upper()
        if priorytet in ["WY", "NO", "NI"]:
            break
        else:
            print("Zły priorytet. Wybierz spośród 'WY', 'NO', 'NI'.")

    # Walidacja stopnia wykonania
    while True:
        try:
            stopień = int(input("Podaj stopień wykonania zadania (0-100): "))
            if 0 <= stopień <= 100:
                break
            else:
                print("Stopień wykonania musi być pomiędzy 0 a 100.")
        except ValueError:
            print("Stopień wykonania musi być liczbą całkowitą.")

    kategoria = input("Podaj kategorię: ")

    utworzono_data = datetime.datetime.now().strftime("%Y-%m-%d")
    utworzono_czas = datetime.datetime.now().strftime("%H:%M")
    modyfikacja_data = utworzono_data
    modyfikacja_czas = utworzono_czas

    lista.append(
        f"{nazwa},{data},{czas},{opis},{priorytet},{stopień},{kategoria},{utworzono_data},{utworzono_czas},{modyfikacja_data},{modyfikacja_czas}"
    )
    linia = ",".join(lista)

    with open(plik, "a", encoding="UTF-8") as op:
        op.write(linia + "\n")

    print("Pomyślnie dodano nowe zadanie.")


import datetime


import datetime


def usun_zadanie():
    plik = "nowy.txt"

    # Wczytaj istniejące zadania
    with open(plik, "r", encoding="UTF-8") as f_in:
        lines = f_in.readlines()

    # Flaga do sprawdzenia, czy zadanie zostało usunięte
    task_found = False

    while True:
        # Pobierz datę od użytkownika
        delete_date = input(
            "Podaj datę utworzenia zadania, które chcesz usunąć (format: YYYY-MM-DD): "
        )
        try:
            delete_date = datetime.datetime.strptime(delete_date, "%Y-%m-%d").strftime(
                "%Y-%m-%d"
            )
            break
        except ValueError:
            print(
                "Data jest zapisana w niepoprawnym formacie. Spróbuj jeszcze raz (format: YYYY-MM-DD)."
            )

    while True:
        delate_time = input(
            "Podaj czas utworzenia zadania, które chcesz usunąć (format: HH:MM): "
        )
        try:
            delate_time = datetime.datetime.strptime(delate_time, "%H:%M").strftime(
                "%H:%M"
            )
            break
        except ValueError:
            print(
                "Czas jest zapisany w niepoprawnym formacie. Spróbuj jeszcze raz (format: HH:MM)."
            )

    delate_name = input("Podaj nazwę zadania, które chcesz usunąć: ")

    # Iteruj przez linie w pliku i zapisz je do nowej listy, jeśli nie są zadaniem do usunięcia
    new_lines = []
    for line in lines:
        (
            nazwa,
            data,
            czas,
            opis,
            priorytet,
            stopień,
            kategoria,
            utworzono_data,
            utworzono_czas,
            modyfikacja_data,
            modyfikacja_czas,
        ) = line.strip().split(",")

        # Konwertuj czas do obiektu datetime
        utworzono_data = datetime.datetime.strptime(
            utworzono_data, "%Y-%m-%d"
        ).strftime("%Y-%m-%d")
        utworzono_czas = datetime.datetime.strptime(utworzono_czas, "%H:%M").strftime(
            "%H:%M"
        )

        # Sprawdź, czy linia odpowiada zadaniu do usunięcia
        if (
            utworzono_data == delete_date
            and utworzono_czas == delate_time
            and nazwa == delate_name
        ):
            task_found = True  # Zaznacz, że znaleziono zadanie do usunięcia
            continue  # Pomijamy dodawanie tej linii do nowej listy
        else:
            new_lines.append(line)  # Zachowujemy linię, jeśli nie jest do usunięcia

    # Zapisz nowe linie do pliku
    with open(plik, "w", encoding="UTF-8") as fs:
        for line in new_lines:
            fs.write(line)

    if task_found:
        print("Pomyślnie usunięto zadanie.")
    else:
        print("Nie znaleziono zadania o podanej dacie, czasie i nazwie.")


def nowy_priorytet():
    plik = "nowy.txt"
    name = input("Podaj nazwę zadania, które chcesz zmodyfikować: ")
    while True:
        try:
            date = input("Podaj datę utworzenia zadania (w formacie rrrr-mm-dd): ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            date = date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")
    while True:
        try:
            time = input("Podaj czas utworzenia zadania (w formacie hh:mm): ")
            time = datetime.datetime.strptime(time, "%H:%M")
            time = time.strftime("%H:%M")
            break
        except ValueError:
            print("czas jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")
    while True:
        try:
            priority = input("Podaj nowy priorytet zadania (WY, NO, NI): ")
            if priority == "WY" or priority == "NO" or priority == "NI":
                break
            else:
                print("niepoprawny priorytet, wybierz(WY, NO, NI")
        except:
            print("wybierz priorytet spośród WY, NO, NI")

    with open(plik, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    # iterujemy po liniach
    for i, line in enumerate(lines):
        # dzielimy linię na poszczególne pola
        miejsce = line.split(",")
        # bierzemy nazwę zadania
        task_name = miejsce[0]
        task_date = miejsce[7]
        task_time = miejsce[8]

        # Jeśli nazwa zadania pasuje do szukanego, to zmiają się dane zadania
        if task_name == name and task_date == date and task_time == time:
            miejsce[4] = priority
            # bierzemy aktualną datę i godzinę jako datę aktualizacji zadania
            now = datetime.datetime.now()
            miejsce[9] = now.strftime("%Y-%m-%d")
            miejsce[10] = now.strftime("%H:%M")
            miejsce[10] = miejsce[10] + "\n"

            new_line = ",".join(miejsce)
            # Zastępujemy stary wpis nowym
            lines[i] = new_line
    with open(plik, "w", encoding="UTF-8") as f:
        f.writelines(lines)
    print("poprawnie zmieniono prorytet zadania")


def nowa_data_czas():
    plik = "nowy.txt"
    name = input("Podaj nazwę zadania, które chcesz zmodyfikować: ")
    while True:
        try:
            date = input("Podaj datę utworzenia zadania (w formacie rrrr-mm-dd): ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            date = date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")
    while True:
        try:
            time = input("Podaj czas utworzenia zadania (w formacie hh:mm): ")
            time = datetime.datetime.strptime(time, "%H:%M")
            time = time.strftime("%H:%M")
            break
        except ValueError:
            print("czas jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")

    while True:
        try:
            new_date = input(
                "Podaj nową datę realizacji zadania (w formacie rrrr-mm-dd): "
            )
            new_date = datetime.datetime.strptime(new_date, "%Y-%m-%d")
            new_date = new_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")
    while True:
        try:
            new_time = input("Podaj nowy czas realizacji zadania (w formacie hh:mm): ")
            new_time = datetime.datetime.strptime(new_time, "%H:%M")
            new_time = new_time.strftime("%H:%M")
            break
        except ValueError:
            print("czas jest zapisany w niepoprawnym formacie. sprobuj jeszcze raz")

    with open(plik, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):

        miejsce = line.split(",")
        task_name = miejsce[0]
        task_date = miejsce[7]
        task_time = miejsce[8]

        if task_name == name and task_date == date and task_time == time:
            miejsce[1] = new_date
            miejsce[2] = new_time
            now = datetime.datetime.now()
            miejsce[9] = now.strftime("%Y-%m-%d")
            miejsce[10] = now.strftime("%H:%M")
            miejsce[10] = miejsce[10] + "\n"
            new_line = ",".join(miejsce)

            lines[i] = new_line
    with open(plik, "w", encoding="UTF-8") as f:
        f.writelines(lines)
    print("poprawnie zmieniono date i czas realizacji")


def nowy_stopien():
    plik = "nowy.txt"
    name = input("Podaj nazwę zadania, które chcesz zmodyfikować: ")
    while True:
        try:
            date = input("Podaj datę utworzenia zadania (w formacie rrrr-mm-dd): ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            date = date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Data jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")
    while True:
        try:
            time = input("Podaj czas utworzenia zadania (w formacie hh:mm): ")
            time = datetime.datetime.strptime(time, "%H:%M")
            time = time.strftime("%H:%M")
            break
        except ValueError:
            print("czas jest zapisana w niepoprawnym formacie. sprobuj jeszcze raz")

    while True:
        try:
            stopień = input("Podaj nowy stopień realizacji zadania (0-100): ")
            stopień = int(stopień)
            if 0 <= stopień <= 100:
                break
            else:
                print("Stopień wykonania musi być pomiędzy 0 a 100.")
        except ValueError:
            print("Stopień wykonania musi być liczbą całkowitą.")

    with open(plik, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    stopień = str(stopień)
    for i, line in enumerate(lines):
        miejsce = line.split(",")
        task_name = miejsce[0]
        task_date = miejsce[7]
        task_time = miejsce[8]

        if task_name == name and task_date == date and task_time == time:
            miejsce[5] = stopień

            now = datetime.datetime.now()
            miejsce[9] = now.strftime("%Y-%m-%d")
            miejsce[10] = now.strftime("%H:%M")
            miejsce[10] = miejsce[10] + "\n"

            # Robimy nową linię z nowymi danymi
            new_line = ",".join(miejsce)
            # Zastępujemy stary wpis nowym
            lines[i] = new_line

    with open(plik, "w") as f:
        f.writelines(lines)
    print("poprawnie zmieniono stopień realizacji")


def sortowanie_data_czas_utworzenia_rosnąco():
    plik = "nowy.txt"
    tasks = []
    with open(plik, "r", encoding="UTF-8") as f:
        fs = f.readlines()
        for task in fs:
            tasks.append(task)
    lista1 = []
    for task in tasks:
        task = task.strip().split(",")
        lista1.append(task)

    lista1.sort(key=lambda x: (x[7], x[8]))
    lista2 = []
    for tas in lista1:
        result = ",".join(tas)
        lista2.append(result)

    with open(plik, "w", encoding="UTF-8") as file:
        for task in lista2:
            file.write(f"{task}\n")
    print("poprawnie posortowano wydarzenia")


def sortowanie_data_czas_utworzenia_malejąco():
    plik = "nowy.txt"
    tasks = []
    with open(plik, "r", encoding="UTF-8") as f:
        fs = f.readlines()
        for task in fs:
            tasks.append(task)
    lista1 = []

    for task in tasks:
        task = task.strip().split(",")
        lista1.append(task)

    lista1.sort(key=lambda x: (x[7], x[8]), reverse=True)

    lista2 = []
    for tas in lista1:
        result = ",".join(tas)
        lista2.append(result)

    with open(plik, "w", encoding="UTF-8") as file:
        for task in lista2:
            file.write(f"{task}\n")
    print("poprawnie posortowano wydarzenia")


def sortowanie_data_czas_aktualizacji_rosnąco():
    plik = "nowy.txt"
    tasks = []
    with open(plik, "r", encoding="UTF-8") as f:
        fs = f.readlines()
        for task in fs:
            tasks.append(task)

    lista1 = []

    for task in tasks:
        task = task.strip().split(",")
        lista1.append(task)

    lista1.sort(key=lambda x: (x[9], x[10]))

    lista2 = []
    for tas in lista1:
        result = ",".join(tas)
        lista2.append(result)

    with open(plik, "w", encoding="UTF-8") as file:
        for task in lista2:
            file.write(f"{task}\n")
    print("poprawnie posortowano wydarzenia")


def sortowanie_data_czas_aktualizacji_malejąco():
    plik = "nowy.txt"
    tasks = []
    with open(plik, "r", encoding="UTF-8") as f:
        fs = f.readlines()
        for task in fs:
            tasks.append(task)
    lista1 = []

    for task in tasks:
        task = task.strip().split(",")
        lista1.append(task)

    lista1.sort(key=lambda x: (x[9], x[10]), reverse=True)

    lista2 = []
    for tas in lista1:
        result = ",".join(tas)
        lista2.append(result)

    with open(plik, "w", encoding="UTF-8") as file:
        for task in lista2:
            file.write(f"{task}\n")
    print("poprawnie posortowano wydarzenia")
