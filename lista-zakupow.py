print("Zadanie 1")
lista_zakupow={
    "Piekarnia":['Chleb','Pączek','Bułki'],
    "Warzywniak":['Marchew','Seler','Rukola']
}
print("Lista zakupów")
for key in lista_zakupow:
    if key=="Piekarnia":
        print(f"Idę do Piekarnia, kupuję tu następujące rzeczy: {(lista_zakupow['Piekarnia'])}")
    elif key=="Warzywniak":
        print(f"Idę do Warzywniak, kupuję tu następujące rzeczy: {lista_zakupow['Warzywniak']}")
lista_zakupow_upper = {key.upper(): [ele.upper() for ele in lista_zakupow[key] ] for key in lista_zakupow }
print(f"oto słownik ze sklepami i towarami pisanymi wielką literą: {lista_zakupow_upper}")
for value in lista_zakupow.values():
    print(f"W sumie muszę kupić {len(value)} produktów.")
#nie potrafię wyciągnąć ilości produktów do kupienia w jedną linię ( czyli żeby było ich 6)
lista_zakupow.update({"Piekarnia":['Bagietka','Chleb','Pączek','Bułki']})
print(lista_zakupow)
lista_zakupow.update({"Warzywniak":['Sałata','Marchew','Seler','Rukola']})
print(lista_zakupow)