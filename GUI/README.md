The GUI was built with PyQt, and features a text-input. Below are the images a user would see before and after submitting text into the GUI.

1. The folder `XCF_files` contains files that are editable with Gimp that are featured in the GUI.
1. The folder `GUI_images` contains the images for the GUI itself (Ash, the borders, etc.)
1. The folder `PokéPNGs` contains images of all the Pokémon that are used in the GUI.
1. The file `pykedex.ui` is the GUI that I made for this. It can be edited with QTDesigner if desired
1. The file `pykedex.py` is the file that will be ran to get the model going. For now, the default model in there is the final model, `pokemodel_stopwords_1`, but one can change it by downloading another model from the `models` directory if they so choose.
1. The directory `pokemodel_stopwords_1` is included in here so one can zip up this folder and run it on their own computer.

If you want to run this locally, make sure that the following Python libraries:
1. PyQt5
2. Pandas
3. Torch
4. Datasets
5. Transformers
6. NLTK


<img width="856" alt="pre_click" src="https://user-images.githubusercontent.com/94126661/233749124-db343557-d64e-4364-80c3-db028384bc4b.png">

<img width="938" alt="pykedex_example" src="https://user-images.githubusercontent.com/94126661/233749099-f83b09a2-72ee-4ac5-b143-bd3bfeb57d9b.png">
