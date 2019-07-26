# åben filen ved brug af en kontekst manager
with open('opgave3.txt', 'w') as f:
  # Skriv noget tekst i filen
  f.write('Dette er noget tekst')

# åben filen ved brug af en kontekst manager
with open('opgave3.txt', 'r') as f:
  # Læs filen
  fil = f.read()

# Print indholdet af filen
print(fil)