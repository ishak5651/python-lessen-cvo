getal1_tekst = input("Voer het eerste getal in:")
getal2_tekst = input("Voer het tweede getal in:")

getal1 = int(getal1_tekst)
getal2 = int(getal2_tekst)

som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2
deling = getal1 / getal2

print(f"som: {som}")
print(f"verschil: {verschil}")
print(f"product: {product}")
print(f"deling: {deling}")
#OEF C DEEL 2
if getal1 % 2 == 0:
    print("Het eerste getal is: even")
else:
    print("Het eerste getal is: oneven")
kwadraat = getal1 ** 2
print(f"kwadraat van eerste getal: {kwadraat}")