class Google:
  antal_produkter = 0 # antallet af produktet i starten
  rabatfaktor = 0.80 # 20% reduktion

  def __init__(self, produktnavn, produkttype, pris):
    self.produktnavn = produktnavn
    self.produkttype = produkttype
    self.support = f'{produkttype}@Google.com'
    self.pris = pris

    Google.antal_produkter += 1 # lægger 1 til antallet af produkter, hver gang et nyt produkt bliver lavet med __init__


  def produktinformation(self):
    return f'''
    Produktnavn: {self.produktnavn}
    produkttype: {self.produkttype}
    Kontakt support: {self.support}
    Produktpris: {self.pris} kr.
    '''


  def tilfør_rabat(self):
    self.pris = int(self.pris * self.rabatfaktor)

prod_1 = Google(produktnavn = 'Pixel', produkttype = 'Telefon', pris = 3000)

print(f'Antallet af Googles produkter: {Google.antal_produkter}')

print(f'\nDen generelle rabatfaktor på Googles produkter: {Google.rabatfaktor}')

print(f'\nPrisen for første produkt før rabat: {prod_1.pris}')

prod_1.tilfør_rabat()

print(f'Prisen for første produkt efter rabat: {prod_1.pris}')
