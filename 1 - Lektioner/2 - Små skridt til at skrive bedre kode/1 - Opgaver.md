# Opgaverne til anden lektion
Heri findes opgaverne til anden lektion omhandlende brugen af forskellige elementer, som vil øge din viden inden for programmering, og samtidig gøre din kode mere læsbar.

---

## Opgave 1 - Brug af "Ternary conditionals"
I denne opgave skal du skrive et stykke kode, som skal printe `'Listen er for lang!'`, hvis en liste har mere end 5 elementer og printe `'Listen er lige, som den skal være'`, hvis ikke det er tilfældet. **Husk at bruge Ternary conditionals!**

---

## Opgave 2 - Omskrivning af store tal
I denne opgave skal du omskrive et stykke kode, så det bliver lettere at læse, både selve koden og i terminalen.
```python
stort_tal = 524643654
større_tal = 2161578538568

største_tal = stort_tal * større_tal

print(største_tal)
```

---

## Opgave 3 - Brug af en kontekst manager
I denne opgave skal du åbne filen `opgave3.txt` og skrive noget tekst i filen.

**Hint:**
For at indlede, at man gerne vil skrive i en fil skal man åbne den med `'w'`, som det andet parameter i `open(fil_navn.txt, 'w')`. For at skrive i filen skal man bruge `f.write('En eller anden form for tekst')`, såfremt, at man har navngivet variablen af sin fil, `f`.


---

## Opgave 4 - Brug af `enumerate()`
I denne opgave skal du finde det element i listen herunder, der har den samme værdi, som den placering det har i listen. Det første element i listen skal have placeringen `1`
```python
[34, 5, 33, 245, 7, 144, 238, 3, 65847, 368, 46, 45, 547, 368, 6, 34258, 7, 18, 75, 247, 868, 5, 386, 3, 26, 26, 36, 2486, 45, 43, 643, 5, 43, 27, 42, 5, 23]
```
---

## Opgave 5 - Brug af `zip()`
Herunder er tre lister med navne, heltenavne og universer, som nogle superhelte har. 

```python
navne = ['Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heltenavne = ['Superman', 'Deadpool', 'Batman']
universer = ['DC', 'Marvel', 'DC']
```

I denne opgave skal du løbe igennem alle listerne og for hver person sammenkæde informationerne på følgende måde:
`'Peter Parker er i al hemmelighed Spiderman og kommer fra Marvel-universet'`

---

## Opgave 6 - Udpakning af tupler
**Til dem, som har lyst**
I denne opgave skal du tage den første og den næstsidste værdi af tuplen herunder, og lægge dem sammen, samt finde ud af, hvor mange tal der er imellem de to værdier (hvis tuplen er `(1, 2, 3, 4)`, så er der 1 tal mellem det første og det næstsidste tal).
```python
(5,3,4,8,4,7,8,3)
```