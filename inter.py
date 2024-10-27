print("program planner")
opcja = 1

while opcja != 5:
    print("wybierz opcje:")
    print("1. wypisz wydarzenia")
    print("2. dodaj wydarzenie")
    print("3. usuń wydarzenie")
    print("4. operacje")
    print("5. zakończ program")

    while True:
        try:
            opcja = int(input("wybierz opcje: "))
            if 1 <= opcja <= 5:
                break
            else:
                print("wybrano niepoprawną opcje")
        except ValueError:
            print("wybrano nieprawidłowe dane")

    if opcja == 1:
        from zlymodul import wyswietl_zadanie

        wyswietl_zadanie()

    elif opcja == 2:
        from zlymodul import dodaj_zadanie

        dodaj_zadanie()

    elif opcja == 3:
        from zlymodul import usun_zadanie

        usun_zadanie()

    elif opcja == 4:
        wybór = 1
        while wybór != 8:  # Poprawione do 8, bo mamy 8 opcji w operacjach
            print("Wybierz operacje:")
            print("1. zmień priorytet")
            print("2. zmień datę i czas realizacji")
            print("3. zmień godzinę realizacji")
            print(
                "4. Wyświetlanie zadań posortowanych wg daty i czasu utworzenia rosnąco"
            )
            print(
                "5. Wyświetlanie zadań posortowanych wg daty i czasu utworzenia malejąco"
            )
            print(
                "6. Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji rosnąco"
            )
            print(
                "7. Wyświetlanie zadań posortowanych wg daty i czasu aktualizacji malejąco"
            )
            print("8. powrót do menu głównego")

            while True:
                try:
                    wybór = int(input("wybierz opcje: "))
                    if 1 <= wybór <= 8:
                        break
                    else:
                        print("wybrano niepoprawną opcje")
                except ValueError:
                    print("wybrano nieprawidłowe dane")

            if wybór == 1:
                from zlymodul import nowy_priorytet

                nowy_priorytet()

            elif wybór == 2:
                from zlymodul import nowa_data_czas

                nowa_data_czas()

            elif wybór == 3:
                from zlymodul import nowy_stopien

                nowy_stopien()

            elif wybór == 4:
                from zlymodul import sortowanie_data_czas_utworzenia_rosnąco

                sortowanie_data_czas_utworzenia_rosnąco()

            elif wybór == 5:
                from zlymodul import sortowanie_data_czas_utworzenia_malejąco

                sortowanie_data_czas_utworzenia_malejąco()

            elif wybór == 6:
                from zlymodul import sortowanie_data_czas_aktualizacji_rosnąco

                sortowanie_data_czas_aktualizacji_rosnąco()

            elif wybór == 7:
                from zlymodul import sortowanie_data_czas_aktualizacji_malejąco

                sortowanie_data_czas_aktualizacji_malejąco()

            elif wybór == 8:
                print("wracamy do menu głównego")

    elif opcja == 5:
        print("zakończono program")
