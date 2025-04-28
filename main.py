import sys
import math
from datetime import datetime

def log(section, message):
    """Zapíše logovací zprávu do souboru log.txt."""
    with open("log.txt", "a", encoding="utf-8") as log_file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{date}] [{section}] {message}\n")

def read_float(name):
    """Načte číselnou hodnotu od uživatele."""
    while True:
        value = input(f"Zadej {name} (nebo 'k' pro konec): ").strip().lower()
        if value == 'k':
            log("Program Exit", "Uživatel ukončil program.")
            print("Uživatel ukončil program.")
            sys.exit(0)
        value = value.replace(",", ".")
        try:
            result = float(value)
            log("Input", f"Uživatel zadal {name}: {result}")
            return result
        except ValueError:
            log("Error", f"Hodnota '{value}' zadaná pro '{name}' není platné číslo.")
            print(f"Chyba: Hodnota '{value}' zadaná pro '{name}' není platné číslo.")

def calculate_m2(m1, M1, M2, p1, p2):
    """Vypočítá hodnotu m2."""
    result = (m1 / M1) * M2 * (p2 / p1)
    log("Calculation", f"Vypočítáno m2: {result}")
    return result

def print_result(m2):
    """Vypíše výsledek výpočtu."""
    log("Output", f"Výsledek m2: {m2:.2f} (na dvě desetinná místa), {m2:.4f} (na čtyři desetinná místa)")
    print(f"m2 je: {m2:.2f} na dvě desetinná místa")
    print(f"m2 je: {m2:.4f} na čtyři desetinná místa")

def get_common_values():
    """Načte společné hodnoty M1, M2, p1, p2."""
    M1 = read_float("M1")
    M2 = read_float("M2")
    p1 = read_float("p1")
    p2 = read_float("p2")
    return M1, M2, p1, p2

while True:
    print("1. Reaktant")
    print("2. Kapalný produkt")
    print("3. Roztok")
    print("4. Magnetické číslo")
    print("5. Stavová rovnice pro výpočet tlaku")
    print("0. Konec")

    choice = input("Zadej volbu: ")

    if choice == "1":
        M1, M2, p1, p2 = get_common_values()
        m1 = read_float("m1")

    elif choice == "2":
        M1, M2, p1, p2 = get_common_values()
        v1 = read_float("v1")
        ro1 = read_float("ro1")
        m1 = v1 * ro1

    elif choice == "3":
        M1, M2, p1, p2 = get_common_values()
        v_solution = read_float("v_roz")
        w1 = read_float("w1")
        ro1 = read_float("ro1")
        v1 = v_solution * w1
        m1 = v1 * ro1

    elif choice == "4":
        n = read_float("n")
        m = math.sqrt((n * (n + 2)))
        log("Calculation", f"Vypočítáno magnetické číslo: {m}")
        print_result(m)
        continue

    elif choice == "5":
        r = 8.314
        v = read_float("V")
        t = read_float("T")
        n = read_float("n")
        p = (n * r * t) / v
        log("Calculation", f"Vypočítán tlak: {p}")
        print_result(p)
        continue

    elif choice == "0":
        log("Program Exit", "Program byl ukončen uživatelem.")
        print("Ukončuji program.")
        break

    else:
        log("Error", f"Neplatná volba: {choice}")
        print("Neplatná volba, zkus znovu.")
        continue

    if None in (m1, M1, M2, p1, p2):
        log("Error", "Zadávání hodnot se nezdařilo. Některé hodnoty jsou neplatné.")
        print("Zadávání se nezdařilo. Oprav chyby a zkus to znovu.")
    else:
        m2 = calculate_m2(m1, M1, M2, p1, p2)
        print_result(m2)
