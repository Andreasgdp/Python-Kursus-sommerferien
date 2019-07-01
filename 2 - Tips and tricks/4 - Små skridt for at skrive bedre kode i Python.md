# Små skridt for at skrive bedre kode i Python

Når man lige er begyndt at lære Python, som vi i dette kursus er, så kan det være svært at gribe forskellige opgaver an, da man ikke har al viden omkring, hvordan programmeringssproget kan takle opgaven. Derfor har jeg herunder beskrevet nogle eksempler, som kan hjælpe med at takle forskellige opgaver.

---
## "Ternary conditionals"
Stop ikke blot ved overskriften, det er ikke så svært, som det lyder. Det er betyder direkte oversat betingelser delt i tre. Herunder er et eksempel på, hvordan en sådan betingelse kan bruges:

```python
betingelse = True

if betingelse:
  x = 1
else:
  x = 0

print(x)

>>> 1
```

Dette kan omskrives ved brug af `Ternary conditionals` for at forkorte, og på samme måde gøre det mere læsbart. Se herunder:

```python
betingelse = False

x = 1 if betingelse else 0

print(x)

>>> 0
```
Dette stykke kode gør nøjagtig det samme, som det øverste, men det er beskrevet på 1 linje i stedet for 4, og giver også mening for én, som ikke nødvendigvis er programmør (dette er, fordi vi er vandt til at læse tekstlinjer. Dette eksempel omformuleret til ren tekst ville være: "x er 1, hvis betingelsen er sand, ellers er x 0")

---

## Arbejde med store tal
Når man arbejdet med meget store tal, kan det være svært at se, hvor store tallene egentlig er; hvis der f.eks. står 100000000000, kan man ikke med det samme sige, hvad tallet er, men havde der stået 100.000.000.000, ville det have været meget lettere. Dette kan man også gøre i python, her gøres det blot med underscore. Se eksempel:

<!-- TODO Continue from here and finish this document -->
<!-- * Continue from here: https://youtu.be/C-gEQdGVXbk?t=188 -->
```python
num_1 = 100_000_000_000
num_2 = 100_000_000

total = num_1 + num_2

print(total)
```