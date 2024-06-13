PrvaValuta=input("unesi valutu ")
DrugaValuta=input("unesi valutu ")
Kolicina=int(input("Kolicina "))
dinueur=0.0085
eurudin=117.08
dinuusd=0.00923
usdudin=108.0193
euruusd=1.0806
usdueur=0.92541
if(PrvaValuta=="din" and DrugaValuta=="eur"):
    resenje=Kolicina * dinueur
elif(PrvaValuta=="eur" and DrugaValuta=="din"):
    resenje=Kolicina * eurudin

if(PrvaValuta=="usd" and DrugaValuta=="din"):
    resenje=Kolicina * usdudin
elif(PrvaValuta=="din" and DrugaValuta=="usd"):
    resenje=Kolicina * dinuusd

if(PrvaValuta=="usd" and DrugaValuta=="eur"):
    resenje=Kolicina * usdueur
elif(PrvaValuta=="eur" and DrugaValuta=="usd"):
    resenje=Kolicina * euruusd

print(resenje)
