from modules.Biudzetas import Biudzetas
from enum import Enum

mano_biudzetas = Biudzetas()

class Veiksmas(Enum):
    IVESTI_PAJAMAS = 1
    IVESTI_ISLAIDOS = 2
    GAUTI_BALANSA = 3
    GAUTI_ATASKAITA = 4
    ISEITI = 0

def ivesti_pajamas():
    print("Įveskite pajamas: ")
    suma = int(input("Suma: "))
    siuntejas = input("Siuntėjas: ")
    papildoma_informacija = input("Papildoma informacija: ")
    mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
    print("Pajamos įvestos sėkmingai!")

def ivesti_islaidas():
    print("Įveskite išlaidas: ")
    suma = int(input("Suma: "))
    atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
    isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
    mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
    print("Išlaidos įvestos sėkmingai!")

def gauti_balansa():
    print(f"Sąskaitos balansas: {mano_biudzetas.gauti_biudzeto_balansa()}")

def gauti_ataskaita():
    mano_biudzetas.gauti_ataskaita()

def atlikti_veiksma(ivestas_veiksmas: Veiksmas):
    if ivestas_veiksmas == Veiksmas.IVESTI_PAJAMAS:
        ivesti_pajamas()
    elif ivestas_veiksmas == Veiksmas.IVESTI_ISLAIDOS:
        ivesti_islaidas()
    elif ivestas_veiksmas == Veiksmas.GAUTI_BALANSA:
        gauti_balansa()
    elif ivestas_veiksmas == Veiksmas.GAUTI_ATASKAITA:
        gauti_ataskaita()
    elif ivestas_veiksmas == Veiksmas.ISEITI:
        return

# Įvedimas ir funkcijos kvietimas:
for veiksmas in Veiksmas:
    print(f"{veiksmas.value} - {veiksmas.name}")

ivesta = int(input("Pasirinkite veiksmą: "))
atlikti_veiksma(Veiksmas(ivesta))
