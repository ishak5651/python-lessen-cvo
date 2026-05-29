Naam = input("Wat is je Naam?")
Leeftijd_tekst = input("Wat is je leeftijd")
Leeftijd = int(Leeftijd_tekst)
Volgend_jaar = Leeftijd + 1
print(f"Hallo{Naam}! Volgend jaar ben je {Volgend_jaar} jaar oud")
print(Naam.upper())

print(Naam.lower())  
print(Naam.strip())  
print(Naam.replace("oude", "nieuwe"))  
print(len(Naam))