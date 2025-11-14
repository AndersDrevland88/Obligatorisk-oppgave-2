#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 20:38:59 2025

@author: andersdrevland
"""
# Arbeidskrav 2 oppgave 1

alder = int(input('Hvilket år er du født? '))
alder_i_2024 = 2024 - alder
print(f'Du blir {alder_i_2024} år i løpet av 2024.')

# Oppgave 2

#Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et
#program som tar inn antall elever fra konsollen ved

antall_elever = int(input('Skriv inn antall elever:' ))
pizza_per_elev = 0.25 * antall_elever
print(f'Antall pizza blir {pizza_per_elev}')
import math
tall = pizza_per_elev
rundet_opp = math.ceil(tall)
print(rundet_opp)  # Output blir heltall

# Oppgave 3
#Lag et program med en funksjon som regner om fra grader til radianer.
#Programmet skal starte med 
  
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180
print(f'Omregnet så er gradtallet {v_rad} radianer')

# Oppgave 4
#Opprett en dictionary som gitt under. Dictionaryen har ulike land som nøkkel (Keys)
#og gir info om hovedstaden i landet og antall innbyggere i mill. i hovedstaden.

Data = {
        "Norge": {"Hovedstad": "Oslo","innbyggere": 0.634},
        "England": {"Hovedstad": "London","innbyggere": 8.982},
        "Frankrike":{"Hovedstad": "Paris","innbyggere": 2.161},
        "Italia": {"Hovedstad": "Roma","innbyggere": 2.873}
        } 
land = input("Hvilket land vil du ha informasjon om hovedstaden:")

if land in Data:
    Hovedstad = Data[land]["Hovedstad"]
    innbyggere = Data[land]["innbyggere"]
    print(f"{Hovedstad} i {land} har {innbyggere} mill. innbyggere." )
else:    
    print("Landet finnes ikke i listen")

nytt_land = input("Skriv inn nytt land: ")
if nytt_land not in Data:
    hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")
    try:
        innbyggere = float(input(f"Hvor mange millioner innbyggere er det i {hovedstad}? ").replace(",", "."))
        # Her er riktig måte:
        Data[nytt_land] = {"hovedstad": hovedstad, "innbyggere": innbyggere}
        # Alternativ med update:
        # data.update({nytt_land: {'hovedstad': hovedstad, 'innbyggere': innbyggere}})
    except ValueError:
        print("Vennligst skriv inn innbyggertall som tall (eks: 1.5)")
else:
    print("Landet finnes allerede.")

print("Oppdatert ")
for land, info in Data.items():
    print(f"{land}: Hovedstad: {info["hovedstad"]}, Innbyggere: {info["innbyggere"]} mill.")



#Oppgave 5

import math

def trekant_halvsirkel(a, b):
    areal_trekant = (a * b) / 2
    radius_halvsirkel = b / 2
    areal_halvsirkel = (math.pi * radius_halvsirkel ** 2) / 2
    areal_total = areal_trekant + areal_halvsirkel

    buelengde_halvsirkel = math.pi * radius_halvsirkel
    omkrets = a + b + buelengde_halvsirkel

    return areal_total, omkrets

# Eksempelbruk (må være utenfor funksjonen, ikke innrykket!)
a = float(input("Skriv inn lengde a: "))
b = float(input("Skriv inn lengde b: "))

areal, omkrets = trekant_halvsirkel(a, b)
print(f"Areal: {areal:.2f}, Ytre omkrets: {omkrets:.2f}")


#OPppgave 6

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = -x^2 - 5')
plt.grid(True)
plt.show()

