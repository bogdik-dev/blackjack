import random
nominal = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Валет", "Дама", "Король", "Туз"]
masti = ["♠", "♥", "♦", "♣"]
koloda = []

for i in nominal:
    for i2 in masti:
        koloda.append(str(i) + i2)
ochki = {
    "Валет": 2,
    "Дама": 3,
    "Король": 4
}

def rashet(ruka):
    summa = 0
    tuzov = 0
    for karta in ruka:
        bes_masti = karta.replace("♠", "").replace("♥", "").replace("♦", "").replace("♣", "")

        if bes_masti == "Туз":
            summa += 11
            tuzov += 1
        elif bes_masti in ochki:
            summa += ochki[bes_masti]
        else:
            summa += int(bes_masti)

    while summa > 21 and tuzov > 0:
        summa -= 10
        tuzov -= 1
    return summa

def razdacha(koloda):
    ruka = []
    ruka.append(koloda.pop())
    ruka.append(koloda.pop())
    return ruka

def igra():
    random.shuffle(koloda)
    ruka_igroka = razdacha(koloda)
    ruka_dilera = razdacha(koloda)
    print(f"Твои карты: {ruka_igroka} — {rashet(ruka_igroka)} очков")
    print(f"Карта дилера: {ruka_dilera[0]}")

    while True:
        if rashet(ruka_igroka) > 21:
            print("💀 Перебор!")
            break
        vibor = input("Взять карту? (да/нет): ").strip().lower()
        if vibor == "да":
            ruka_igroka.append(koloda.pop())
            print(f"Твои карты: {ruka_igroka} — {rashet(ruka_igroka)} очков")
        else:
            break

    if rashet(ruka_igroka) <= 21:
        print(f"\nКарты дилера: {ruka_dilera} — {rashet(ruka_dilera)} очков")
        while rashet(ruka_dilera) < 17:
            ruka_dilera.append(koloda.pop())
            print(f"Дилер взял: {ruka_dilera} — {rashet(ruka_dilera)} очков")

    ochki_igroka = rashet(ruka_igroka)
    ochki_dilera = rashet(ruka_dilera)

    print("\n=== РЕЗУЛЬТАТ ===")
    if ochki_igroka > 21:
        print("❌ Ты проиграл (перебор)")
    elif ochki_dilera > 21:
        print("✅ Дилер перебрал! Ты выиграл!")
    elif ochki_igroka > ochki_dilera:
        print("🎉 Ты выиграл!")
    elif ochki_igroka < ochki_dilera:
        print("❌ Дилер выиграл")
    else:
        print("🤝 Ничья")

igra()