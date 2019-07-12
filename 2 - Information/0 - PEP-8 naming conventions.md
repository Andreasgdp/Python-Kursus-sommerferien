# Skriv brugervenlig kode med PEP-8 naming conventions

## 1 - Hvad er PEP 8?
- PEP står for: `Python Enhancement Proposal`
- PEP 8 er et set retningslinjer for Python
  - Anvendt af mange
  - https://www.python.org/dev/peps/pep-0008/


## 2 - Hvorfor i alverden vil man dog følge disse regner?
- Letlæselig kode
  - Mest for én selv, men også for andre programmører, som læser koden
- Brugervenlig kode
  - At følge disse regler er en anden måde at dokumentere éns kode
  - Det gør det også lettere for programmører (skriver man f.eks. koden til et bibliotek er det vigtig, at koden følger de regler, som de fleste kender til)

---
## 3 - De vigtigste naming conventions

### 3.1 - `normale_variabler`
- Navne på variabler skal altid være skrevet med små bogstaver (lowercase), hvor ord separeres med underscore

```python
en_otg_lærer = 'Søren Præstegård'
```

### 3.2 - `KONSTANTER`
I Python kan alle variabler bliver ændret, derfor eksisterer rigtige konstanter ikke. Dog kan man indikere, at en variabel burde blive behandlet, som om det var en konstant.

- Navne på konstanter skal skrives kun med store bogstaver (uppercase), hvor ordene separeres med underscore

```python
ROBOT_1_IP = '10.130.58.11'
```

### 3.3 - `funktion_navne()`
- Navne på funktioner og klasse-metoder (`@classmethod`) skal altid være skrevet med små bogstaver (lowercase), hvor ord separeres med underscore

```python
import random

OTG_LÆRERE = [
  'Søren Præstegård',
  'Jeppe Munk',
  'Dorthe Klausen'
]


def random_otg_lærer():

  return random.choice(OTG_LÆRERE)


print(random_otg_lærer())
```
`>>> Jeppe Munk`

### 3.4 - `KlasseNavne`
- Klasse navne skal for hvert ord starte med stort bogstav (CamelCase)

```python
class OtgLærer:
  def __init__(selv, navn):

    selv.navn = navn
  
  def __str__(self):
    
    return self.name


annette_bertelsen = OtgLærer(navn='Annette Bertelsen')
print(annette_bertelsen)
```
`>>> Annette Bertelsen`

### 3.5 - `FactoryFunctionNames()`
Factory funktioner er egne funktioner (ikke i en klasse), som returnerer objekter. Derfor, for brugere af koden (dette er igen mest til, hvis man laver biblioteker), agerer funktionerne som klasse definitioner.

- For at understrege denne egenskab af Factory funktioner skal disse funktioners navne opskrives på samme måde som klasser. Funktionernes navne skal for hvert ord starte med stort bogstav (CamelCase).

```python
def AntonVestergaard():
  
  return OtgLærer(name='Anton Vestergaard')


anton_vestergaard = AntonVestergaard()
print(anton_vestergaard)
```
`>>> Anton Vestergaard`

### 3.6 - `modstridende_navne_`
- Hvis et navn allerede er taget af python (det kunne være `list` eller `in`), skal der tilføjes en underscore som suffix

```python
list_ = ['Dette', 'er', 'en', 'liste']
```
