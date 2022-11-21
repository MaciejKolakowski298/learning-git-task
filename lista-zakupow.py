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