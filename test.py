fornavne = ['Jens', 'Flemming', 'Jan', 'Hans']
mellemnavne = ['Dragelund', 'Bamse', 'And', 'Gustav']
efternavne = ['Jensen', 'Flemmingsen', 'Jansen', 'Hansen']

for fornavn, mellemnavn, efternavn in zip(fornavne, mellemnavne, efternavne):
  print(f'{fornavn} har mellemnavnet {mellemnavn} & efternavnet {efternavn}')