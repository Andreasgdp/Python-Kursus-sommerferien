# definer liste
liste = [34, 5, 33, 245, 7, 144, 238, 3, 65847, 368, 46, 45, 547, 368, 6, 34258, 7, 18, 75, 247, 868, 5, 386, 3, 26, 26, 36, 2486, 45, 43, 643, 5, 43, 27, 42, 5, 23]


# løb igennem listen med index og tal
for index, tal in enumerate(liste, start = 1):
  # tjek om indekset er det samme som tallet
  if index == tal:
    # print tallet
    print(f'Tallet: {tal} har indekset: {index}')