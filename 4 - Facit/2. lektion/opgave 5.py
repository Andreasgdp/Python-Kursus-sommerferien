# opskriv liserne
navne = ['Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heltenavne = ['Superman', 'Deadpool', 'Batman']
universer = ['DC', 'Marvel', 'DC']

# løb igennem alle listerne med zip()
for navn, heltenavn, univers in zip(navne, heltenavne, universer):
  # print navn, heltenavn, univers
  print(f'{navn} er i al hemmelighed {heltenavn} og kommer fra {univers}-universet')