def osszehasonlito(text01:str, text02:str) -> int:
    gyakori_betuk = ""
    for i in text01:
        if i in text02 and i not in gyakori_betuk:
            gyakori_betuk += i
    egyezik = len(gyakori_betuk)
    return egyezik