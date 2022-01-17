class etunimiSukunimi:
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

joonas = etunimiSukunimi('Joonas', 'Pitkänen')
lasse = etunimiSukunimi('Lasse', 'Lehtinen')

print(joonas.etunimi, joonas.sukunimi)

print(lasse.etunimi, lasse.sukunimi)
