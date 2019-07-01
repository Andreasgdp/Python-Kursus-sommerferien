# Hjælpeværktøjer i Python

I Python er der flere værktøjer, man kan bruge, til hurtigt at få en viden af det, man arbejder med.

---
## `help()`
I Python er der en indbygget funktion kaldet `help()`. Denne funktion bruges til at få en viden af indholdet af de biblioteker, man arbejder med. Hvis man f.eks. arbejder med `matplotlib`, `math` eller et andet bibliotek, kan det være meget svært altid at kunne huske, hvad for nogle funktioner, man kan bruge i de biblioteker. Ved brug af funktionen `help()` kan man få al dokumentationen for det pågældende bibliotek.

```python
import math

help(math)

'''
>>> Help on built-in module math:

    NAME
        math

    DESCRIPTION
        This module is always available.  It provides access to the
        mathematical functions defined by the C standard.

    FUNCTIONS
        acos(x, /)
            Return the arc cosine (measured in radians) of x.

  -- More --
'''
# ">>>" Betyder, at det udskrevet i terminalen. Normalt skriver man det 
# omvendt, så det er al den kode, som ikke vises fra terminalen, som 
# skal stå med ">>>", men her har jeg gjort det lettere for jer 
# deltagere at kopiere det for hurtigere at kunne lære med brugen af det
```

Man kan også bruge `help()` til at få dokumentation af ting som typer. Man kan altså finde typen af en variabel og derefter bruge ``help()` til at finde ud af, hvad man kan gøre med den variabel.

```python
min_streng = 'Dette er en streng, jeg skal bruge til et eller andet'

type(min_streng)
>>> <class 'str'>

help(str)
```

## `dir()`
`dir()` er på en måde den korte version af `help()`, da den returnerer de operationer, som kan blive lavet på et element i koden.

```python
min_streng = 'Jeg er en streng'
dir(min_streng)

>>> ['__add__', ..., 'upper', 'zfill']  # Forkortet for bedre læsbarhed
```
Elementerne returneret af `dir()` er alle de metoder (dvs. handlinger) som man kan anvende på elementer, f.eks.:
```python
min_streng.upper()
>>> 'JEG ER EN STRENG'
```