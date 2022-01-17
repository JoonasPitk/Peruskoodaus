class Henkilo:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def laske_syntymavuosi(self):
        return 2022 - self.ika

jaska = Henkilo('Jaakko Saariluoma', 50)
minna = Henkilo('Minna', 60)
taina = {'nimi': 'Taina', 'ika': 55}

print(jaska.nimi)
print(jaska.ika)

print(minna.nimi)
print(minna.ika)

print(taina['nimi'])
print(taina['ika'])

print('Jaska on syntynyt vuonna', jaska.laske_syntymavuosi())
