slownik = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów:")

suma_zakupow = 0

for i in slownik:
    suma_zakupow += len(slownik[i])
    print(f"Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {', '.join([a.title() for a in slownik[i]])}")

#tutaj powinien znajdowac się dodatkowy commit numer 1
print(f"W sumie kupiłem {suma_zakupow} rzeczy.")