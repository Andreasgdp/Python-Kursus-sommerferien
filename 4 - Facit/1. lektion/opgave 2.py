import math
import matplotlib
import os
import sys

help(math)

print('\n\n')

help(matplotlib)

print('\n\n')

help(os)

print('\n\n')

help(sys)

print('\n\n')


tekst_streng = 'Dette er en tekst streng'
print(f'\n\n\nDette er, hvad man kan gøre med en tekst streng: \n{dir(tekst_streng)}')

tal = 1
print(f'\n\n\nDette er, hvad man kan gøre med et tal: \n{dir(tal)}')

kommatal = 2.3
print(f'\n\n\nDette er, hvad man kan gøre med et kommatal: \n{dir(kommatal)}')

liste = [1, 2, 3, 4, 5]
print(f'\n\n\nDette er, hvad man kan gøre med en liste: \n{dir(liste)}')

ordbog = {
  'menneske': 'jord',
  'papegøje': 'luft',
  'haj': 'vand'
}
print(f'\n\n\nDette er, hvad man kan gøre med en ordbog: \n{dir(ordbog)}')


# Praktisk senarie:
print('\n\n\nPraktisk senarie:')
min_streng = 'Dette er en streng, jeg skal bruge til et eller andet'

type(min_streng)
# >>> str

help(str)

# >>> Betyder, at det bliver kørt i terminalen. Normalt i et program vil man printe værdien med print() for at finde værdien, som i dette tilfælde er str.