import os

g = open("dane/data.txt","r",encoding="utf-8")
print(g.read())
print("+"*70)
g.close()

print(g.closed)

with open("dane/data.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)
print("+"*70)

print(f.closed)

with open("dane/data.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

print(f.closed)

print("+"*70 + "Zapis do pliku ++++")

with open("dane/dataoutput.txt","w",encoding="utf-8") as f:
    f.write("Nowy wiersz do pliku")

with open("dane/dataoutput.txt","a",encoding="utf-8") as f:
    f.write("\nDodaj nowy wiersz do pliku -> wersja append")


if os.path.exists("dane/dataoutputs.txt"):
    print("Plik istnieje")
else:
    print("Plik nie istnieje")


with open("dane/dataoutput.txt","r",encoding="utf-8") as f:
    print(f.read(5))
    f.seek(0)
    print(f.read(5))
