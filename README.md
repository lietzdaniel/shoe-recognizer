# shoe-recognizer
This repository contains the code for generating the models for [this](https://lietzdaniel-streamlit-shoe-recognizer-frontendstreamlit-bvk8g6.streamlit.app/) application. 

## Image Scraping
For Image Scraping, a database of shoes has to be created. This is done in `./ImageScraping/sneakerDatabase.py`. There, the API of [Sole Collector](https://solecollector.com) is used in order to collect models of shoes. The commented code in the project would allow for every colorway to be listed in the resulting `allShoes.csv`. But because of the increased difficulty to collect many distinct images, this model will be trained for models of shoes, not colorways. Using the library `jmd_imagescraper` to scrape DuckDuckGo, 80 images are downloaded for every shoe. Additionally, in a handpicked `popularShoes.csv` the most popular shoe models are listed, for which 400 images will be downloaded. These images consist of different querys used for the images in order to not only have stock images for the shoes.

## Machine Learning

In the Jupyter Notebook `./ml/ml.ipynb`, the model is trained for recognizing the shoes. For this, the `FastAI` libary is used, taking the `vision_learner()` with `resnet34` as a base. `fit_one_cycle()` is called on 10 epochs, and is stopped when no increase of 0.1 over 2 epochs happens. After the training, the learner can be saved and tested using images in the folder `./ml/images`.