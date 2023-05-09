
from bing_image_downloader import downloader
import csv





filename = 'allShoes.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    i = 0
    for row in datareader:
        if i < 722:  
            i += 1
            continue
        downloader.download(row[0], limit=50,  output_dir='./bing' + row[0] + 'dataset', adult_filter_off=True, force_replace=False, timeout=30, verbose=False)

