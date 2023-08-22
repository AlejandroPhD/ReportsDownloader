import requests
import os
import shutil

list_months = [
    "ENERO",
    "FEBRERO",
    "MARZO",
    "ABRIL",
    "MAYO",
    "JUNIO",
    "AGOSTO",
    "SEPTIEMBRE",
    "OCTUBRE",
    "NOVIEMBRE",
    "DICIEMBRE",
]

# Remove the existing 'reportes' folder and its contents
if os.path.exists("reportes"):
    shutil.rmtree("reportes")

# Recreate the 'reportes' folder
os.mkdir("reportes")

for month in list_months:
    url = f"https://www.asfi.gob.bo/images/VALORES/Boletines/2022/Boletin_{month}-2022_VF.xlsx"
    r = requests.get(url, allow_redirects=True)
    if r.ok:
        open(f"reportes/{month.lower()}-2022.xlsx", "wb").write(r.content)
