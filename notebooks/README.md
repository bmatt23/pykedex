The descriptions for the notebooks are as follows: 
1. `pokedex_scrape.ipynb` is where I scraped the initial [Pokédex data](https://pokemondb.net/).
1. `get_images.ipynb` is where I used [bing-image-downloader](https://pypi.org/project/bing-image-downloader/) to get images of the Pokémon
3. `Get_pokemon_captions.ipynb` is where I used the [image-to-text package](https://github.com/salesforce/BLIP) to generate text for the Pokémon images previously scraped (make sure to clean the images first to make sure they're all correct!)
4. `generate_pokedex variations.ipynb` is where I used the [nlpaug](https://pypi.org/project/nlpaug/0.0.5/) library to augment the previous data. This file was also used to augment the data from the Pokémon Wiki below
5. `Pokémodel.ipynb` is where all the [model](https://huggingface.co/docs/transformers/model_doc/bert) creation was done. 
6. `scrape_pokewiki.ipynb` is where the [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page) validation data was scraped and processed
7. `final_validation.ipynb` is where the validation testing and EDA occurred
