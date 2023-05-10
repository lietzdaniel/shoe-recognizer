from jmd_imagescraper.core import * 
from pathlib import Path
import csv

allFile= 'allShoes.csv'
popularFile = 'popularShoes.csv'

with open(popularFile, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        root = Path().cwd()/"images"
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] ,label="all" , max_results=100)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " ebay",label="all" , max_results=100)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " vinted",label="all" , max_results=100)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " used",label="all" , max_results=100)
        
with open(allFile, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        root = Path().cwd()/"images"
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] ,label="all" , max_results=20)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " ebay",label="all" , max_results=20)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " vinted",label="all" , max_results=20)
        duckduckgo_search(Path().cwd()/row[0],keywords= row[0] + " used",label="all" , max_results=20)
        
    