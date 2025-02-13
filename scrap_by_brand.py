import re
import csv
from bs4 import BeautifulSoup
import requests
from time import sleep

car_brands = {
    "Ostatní značky": 28,
    "Volvo": 39,
    "Volkswagen": 36,
    "Toyota": 35,
    "Tesla": 55,
    "Škoda": 34,
    "Suzuki": 41,
    "Subaru": 33,
    "Smart": 49,
    "Seat": 38,
    "Saab": 42,
    "Rover": 45,
    "Rolls Royce": 59,
    "Renault": 32,
    "Praga": 54,
    "Porsche": 31,
    "Pontiac": 30,
    "Peugeot": 29,
    "Opel": 27,
    "Nissan": 26,
    "Motokára": 50,
    "Mitsubishi": 25,
    "Mini": 24,
    "MG": 23,
    "Mercedes-Benz": 22,
    "McLaren": 53,
    "Mazda": 21,
    "Maserati": 20,
    "Lotus": 19,
    "Lexus": 18,
    "Lancia": 46,
    "Lamborghini": 17,
    "KTM": 52,
    "Kia": 56,
    "Kaipan": 47,
    "Jaguar": 16,
    "Infiniti": 15,
    "Chrysler": 14,
    "Chevrolet": 13,
    "Hyundai": 12,
    "Honda": 11,
    "Formule": 37,
    "Ford": 10,
    "Fiat": 9,
    "Ferrari": 8,
    "Dodge": 7,
    "Cupra": 57,
    "Cobra": 51,
    "Citroën": 40,
    "Bugatti": 6,
    "BMW": 5,
    "Bentley": 4,
    "Audi": 3,
    "Aston Martin": 2,
    "Alpine": 61,
    "Alpina": 60,
    "Alfa Romeo": 1,
    "Abarth": 58
}

print(f"Zadejte značku vozidla")
raw_input = input()
desired_brand = car_brands[raw_input]
url = f"https://www.sportovnivozy.cz/znacka-{desired_brand}"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
tables = soup.find_all("table", class_="vypisDilo W100pc T100pc prechod1 zalamovaniTextu")

data = []
print("Načítám vozy...")
sleep(1.6)
for table in tables:
    try:
        car = table.find("strong").get_text(strip=True)

        #second row
        tr = table.find("tr")
        next_tr = tr.find_next("tr")

        year = next_tr.find("strong").get_text(strip=True)

        td_text = next_tr.find("td").get_text(" ", strip=True)

        mileage_match = re.search(r"(\d{1,3}(?:\s?\d{3})*)\s*Km", td_text)
        litres_match = re.search(r"(\d{1,2}\s?\d{3})\s*ccm", td_text)
        kw_match = re.search(r"(\d{1,3})\s*kW", td_text)

        mileage = mileage_match.group(1).replace(" ", "") + " Km" if mileage_match else "NA"
        litres = litres_match.group(1).replace(" ", "") + " ccm" if litres_match else "NA"  
        kw = kw_match.group(1) + " kW" if kw_match else "NA"
        print(car)
        print(year)
        print(mileage)
        print(litres)
        print(kw)
        # Uložení do seznamu
        #data.append([car, year, mileage, litres, kw])

    except Exception as e:
        print(f"Chyba při zpracování vozidla: {e}")

# Zápis do CSV souboru
# csv_filename = "auta.csv"
# with open(csv_filename, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
    
#     # Hlavička CSV
#     writer.writerow(["Model", "Rok", "Kilometry", "Objem motoru", "Výkon"])
    
#     # Data
#     writer.writerows(data)

# print(f"Data byla uložena do {csv_filename}")