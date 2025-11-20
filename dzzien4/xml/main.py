from xml.etree.ElementTree import Element,SubElement
from prettyfy import pretty

top = Element("autokomis")

#pierwszy samochód
sam1 = SubElement(top,'samochod')

id = SubElement(sam1,"id")
id.text = "sam1"

marka = SubElement(sam1,"marka")
marka.text = "subaru"

model= SubElement(sam1,"model")
model.text = "impreza"

rok = SubElement(sam1,"rok")
rok.text = "2000"

poj = SubElement(sam1,"pojemnosc")
poj.text = "2.0"

cena = SubElement(sam1,"cena")
cena.text = "58900"

wyp_dod = SubElement(sam1,'wypo_dodatkowe')

kolor = SubElement(wyp_dod,"kolor")
kolor.text = "czarna perła"

klima = SubElement(wyp_dod,"klimatyzacja")
klima.text = "REDR5342345"

#drugi samochód

sam2 = SubElement(top,'samochod')

id = SubElement(sam2,"id")
id.text = "sam2"

marka = SubElement(sam2,"marka")
marka.text = "subaru"

model= SubElement(sam2,"model")
model.text = "outback"

rok = SubElement(sam2,"rok")
rok.text = "2019"

poj = SubElement(sam2,"pojemnosc")
poj.text = "2.4"

cena = SubElement(sam2,"cena")
cena.text = "114700"

wyp_dod = SubElement(sam2,'wypo_dodatkowe')

kolor = SubElement(wyp_dod,"kolor")
kolor.text = "czerwony metallic"

klima = SubElement(wyp_dod,"klimatyzacja")
klima.text = "REDR98675"

podu = SubElement(wyp_dod,"poduszki")
podu.text = "4"

print(top)
print(pretty(top))

with open("subaru.xml","a",encoding="utf-8") as f:
    f.write(pretty(top))
