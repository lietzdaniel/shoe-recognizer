import requests
from bs4 import BeautifulSoup
import json
import csv
baseURL = "https://solecollector.com"
dataBase = "/sd/sole-search-sneaker-database/"





brandIdDict = {"Nike": 117, "Adidas":130,"Reebok":242,"Puma":249,"Jordan":8,"Converse":62,"Vans":191,"New Balance": 177,"Asics":1}
with open("allShoes.csv","w") as csvFile:
    writer = csv.writer(csvFile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for name,id in brandIdDict.items():
        typeJson = requests.get(f"https://solecollector.com/api/sneaker-api/lines?brand_id={id}&get=1000").json()
        for shoeType in typeJson:
         
            shoeModel = shoeType["id"]
            modelJson = requests.get(f"https://solecollector.com/api/sneaker-api/models?line_id={shoeModel}&get=1000").json()
            for modelType in modelJson:
                writer.writerow([modelType["name"]])
                #colorWay = modelType["id"]
               # colorJson = requests.get(f"https://solecollector.com/api/sneaker-api/releases?asc=0&parent_id={colorWay}&get=1000").json()

               # for shoe in colorJson:
                  #  try:
                    #    writer.writerow([shoe["name"],shoe["style_code"]])
                   # except KeyError:
                   #     writer.writerow([shoe["name"],"n/a"])