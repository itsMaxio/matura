file = open("Dane_2212\mecz.txt", 'r').read()
test = "ABABABAB"

print("zadanie 1")
kto_wygral = ''
wynik = 0
for mecz in file.strip():
    if kto_wygral == '':
        kto_wygral = mecz
    if mecz != kto_wygral:
        wynik += 1
        kto_wygral = mecz
        
print(wynik)


print("zadanie 2")

wynikA = 0
wynikB = 0
ostatniSet = ''

for mecz in file.strip():
    if mecz == 'A':
        wynikA += 1
    else:
        wynikB += 1
    if wynikA >= 1000 or wynikB >= 1000:
        if wynikA - wynikB >= 3 or wynikB - wynikA >= 3:
            ostatniSet = mecz
            break
       
print(ostatniSet, str(wynikA)+":"+str(wynikB))


print("zadanie 3")

passa = ''
licznik = 0
najPassa = ''
seriaPass = 0
kto_wygral = ''

test = "BBBBBBBBBBAABBAAAAAAAAAAABA"

for mecz in file.strip():
    if kto_wygral == '':
        kto_wygral = mecz
    if mecz == kto_wygral:
        passa += mecz
    else:
        if len(najPassa) < len(passa):
            najPassa = passa
        kto_wygral = mecz
        passa = '' + mecz
        licznik = 1
    if len(passa) >= 10 and licznik == 1:
         seriaPass += 1
         licznik = 0
print(seriaPass, najPassa[0], len(najPassa))