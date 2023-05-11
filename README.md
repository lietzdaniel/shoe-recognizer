# shoe-recognizer

## Summary
Identifies the model of a shoe in a given image. Scrapes websites for databases of shoes and search engines for images of them. After categorizing the data, a Machine Learning model is trained on it. The model can be played around with in the dashboard below. This repository does all the Data Scraping and model training.


## [Dashboard](https://lietzdaniel-streamlit-shoe-recognizer-frontendstreamlit-bvk8g6.streamlit.app)

![Test](https://camo.githubusercontent.com/19f935f1367a85be4b193798d0737b83d8167725f87920f955a1c3ba63da44fa/68747470733a2f2f692e696d6775722e636f6d2f76495659554d762e676966)


## Table of Contents


## Motivation

As a sneaker enthusiast, it sometimes happens that you stumble upon a sneaker that you have never seen and you don't know the model of. My idea was to, in the end, provide an easily accessible dashboard where you can find out the name of any shoe that you want.

## Design Document & Pipeline

Before starting any programming, I wrote down my thoughts of how I was going to approach this in a Design Document. This defined a clear goal for me, and I thought about technologies I could use. ![designdoc](https://i.imgur.com/kfe3MW2.png)

To make it easier for me to follow, I also created a flow chart visualizing the steps that had to be done. ![flowchart](https://i.imgur.com/xwe1jUb.png)

Eventhough I didn't do everything exactly as stated in the plans, setting up a flowchart and design document helped a lot in the development of the project. I didn't only have the final goal in mind, but always knew what my next sub-goal is and what I need to do in order to advance with the development.

## Creating a shoe database

The first step that had to be done is deciding on what shoes the model should be able to recognize. My first idea was to just to find every possible shoe model, including every possible color and variant it released with, and write it into a `.csv` database. After doing some research, I found a Sneaker Database in the Website [Sole Collector](https://solecollector.com/sd/sole-search-sneaker-database/). It had sneakers from nine of the most popular footwear brands (`[Nike, Adidas, New Balance, Asics, Converse, Vans, Jordan, Puma, Reebok]`), every model these brands released, and every variant of these models ever released. Using the backend API of this website, I scraped every entry in the database and saved it locally. The amount of shoes was over 4000. These were a lot of entries, and I decided to go a step back and ignore the different variants, only differentiating between models, reducing the amount of sneakers in my database to roughly 1200.
![shoedb](https://i.imgur.com/R0y7lmu.png)
## Image Scraping

After gathering the models of shoes, I had to collect images of them in preperation for the training of my Machine Learning model. 

### Amount and kind of images

Before starting to download images, I had to decide on how many images I want per Sneaker. I decided for 50 per Sneaker for my first run. In addition, I created another database `popularShoes.csv`, where I handpicked the most popular shoes out of my list in order to download double the amount of pictures to them, in order to have a higher likelyhood of estimating popular sneakers. These numbers were later increased to 200 images for normal and 1000 for popular sneakers. 

In addition, to prevent downloading to many stock pictures done in a photo studio, I wanted to not only search for the shoe name as it was listed in the database, but instead append `vinted` `ebay` and `used` to the search query in order to get more variance in my training images.

### Websites used
 Similarly to the creation of the database, I had planned to use multiple websites as the sources for the images. First of all, I tried [Pinterest](https://www.pinterest.com/) with the `pin-scrape` library. This didn't provide enough images per call of the function, so I quickly switched to `bing-search-scraper`, hoping I would have more luck with a proper search engine like [Bing](https://www.bing.com/?toWww=1&redig=6BD5868229A5487EAE0708E5AA0E020D). This proved to supply better results, but I noticed that the search querys with `ebay` in them still only provided stock images, so I needed to search for another alternative. The best solution I found for this was `jmd_imagescraper`, using [Duck Duck Go](https://duckduckgo.com/?va=b&t=hchttps://duckduckgo.com/?va=b&t=hc) as a search engine. Using these libraries, images were downloaded very quickly and with good coherence to the search queries.
![foldergif](https://i.imgur.com/9iOmtcQ.gif)




## Machine Learning

After the data was ready, a machine learning model could be built upon it. Before trying it with the huge amount of pictures I collected, I chose four models specifically in order to attempt a smaller scale model. I took some pictures of my shoes to try this model out with in order to see if it is working. After that was successful, I incorporated every of my downloaded folders into the training. 

### Different Training Runs
The first training run was done with 50 images per normal and 100 images per popular shoe. The metrics used were only accuracy, and 10 epochs were done. After playing around with the model for a bit, the accuracy wasn't quite to my satisfaction. I first added an `EarlyStoppingCallback` in order to stop the training earlier if it doesn't improve by `delta = 0.1` in one epoch for quicker training. For improvement of the model, I added `Precision(average='macro')` as a metric. Due to the different amounts of images for some shoes, the `macro` keyword was mandatory here. The model looked like it was getting better, but it still had troubles, especially if the images were rotated, like this: ![af1](https://i.imgur.com/NM52TTg.png)

To fix this, I increased the threshhold for possible rotation during the training to 90 degrees with `aug_transforms(max_rotate=90.0)`. Also, I increased the image amount to 200 for normal shoes, and 1000 for popular shoes. In the end, the accuracy for rotated image has improved, but the accuracy for non rotated has 

# Connection to frontend
The code for the frontend can be found [here](https://github.com/lietzdaniel/streamlit-shoe-recognizer). The model that was trained on is uploaded in the repo. The model is loaded in the StreamLit app, and  `predict()` is invoked on the image uploaded, with the results being printed on the dashboard. 

# Final thoughts and further ideas
All in all, while the most recent model can identify some sneakers in some positions okay-ish, the sheer amount of sneakers in the world make it hard to train a machine learning model accurately identifying them. The rarer a colorway or a model of a shoe is, the harder it is to find many distinct pictures of it in order to properly train a Machine Learning model on it. That said, there are some optimizations and approaches that still can be tried out in order to more accurately predict the sneaker:

- Reduce the model amount by uniting similar models (e.g `UltraBoost 2019` and `UltraBoost 2020`)
- Train the model with rotation with a smaller probability for that rotation occuring
- Changing Hyperparameters like `batch_size` or other modification with the augments of the data
- Gather a significant additional amount of images for the shoes from various sources
- Providing the frontend with multiple models to choose from
- Create a Test Set with 5% of the Data to more easily validate the model

