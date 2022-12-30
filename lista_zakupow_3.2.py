slownik = {
    "piekarnia" : ["chleb", "bułki", "pączek"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

print("Lista zakupów:")

suma_zakupow = 0

for i in slownik:
    suma_zakupow += len(slownik.items())
    print(f"Idę do {i.capitalize()}, kupuję tu następujące rzeczy: {', '.join([a.title() for a in slownik.items()])}")

print(f"W sumie kupiłem {suma_zakupow} rzeczy.")