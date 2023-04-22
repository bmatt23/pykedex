#!/usr/bin/env python
# coding: utf-8
# %%
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QPlainTextEdit
from PyQt5.QtWidgets import QDialog, QMessageBox, QRadioButton, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
import PyQt5.QtCore
from PyQt5 import uic
import pandas as pd
import torch
from datasets import ClassLabel
from transformers import BertTokenizer
from transformers import BertForSequenceClassification
import sys
import warnings
import nltk
from nltk.corpus import stopwords
warnings.filterwarnings('ignore')

# get normal dataframe
df = pd.read_csv('big_pokedex_scrape.csv').drop(columns = ['Unnamed: 0'])
stop_words = stopwords.words('english')

# create tokenizer from pretrained bert
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# establish int to pokemon relationship
class_converter = ClassLabel(num_classes = 1008, names = list(df.Pokemon.unique()))

# establish model
# model1 = model.from_pretrained("pokemodel_stopwords_1")

model = BertForSequenceClassification.from_pretrained(
    "pokemodel_stopwords_1",from_tf=False)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        #load the ui file
        uic.loadUi("pykedex.ui", self)
        self.setWindowTitle("Welcome to Pykédex!")
        

        
        
        # define our widgets
        
        # first our ashes
        self.ash_posttext = self.findChild(QLabel, "ash_posttext")
        self.ash_posttext.setHidden(True)
        self.ash_pretext = self.findChild(QLabel, "ash_pretext")
        self.ash_text = self.findChild(QLabel, "ash_text")
        self.i_choose_you = self.findChild(QLabel, "i_choose_you")
        self.i_choose_you.setHidden(True)

        # our first place stuff
        self.first_pokemon = self.findChild(QLabel, "first_pokemon")
        self.first_border = self.findChild(QLabel, "first_pokemon_border")
        self.first_place_name = self.findChild(QLabel, "first_place_name")
        self.first_num = self.findChild(QLabel, "first_num")

        # our second place stuff
        self.second_pokemon = self.findChild(QLabel, "second_pokemon")
        self.second_border = self.findChild(QLabel, "second_pokemon_border")
        self.second_place_name = self.findChild(QLabel, "second_place_name")
        self.second_num = self.findChild(QLabel, "second_num")

        # our third place stuff
        self.third_pokemon = self.findChild(QLabel, "third_pokemon")
        self.third_border = self.findChild(QLabel, "third_pokemon_border")
        self.third_place_name = self.findChild(QLabel, "third_place_name")
        self.third_num = self.findChild(QLabel, "third_num")

        # logo
        self.logo = self.findChild(QLabel, "logo")

        # set text prompt
        self.text_input = self.findChild(QPlainTextEdit, "text_input")
        self.text_input.setPlaceholderText('Insert Pokémon Description Here...')

        # predict pokemon button
        self.predict_pokemon_button = self.findChild(QPushButton, "predict_pokemon")
        
        
        # self.deal_button = self.findChild(QPushButton, "deal_new")
        # self.next_button = self.findChild(QPushButton, "next_hand")
        # self.bet_button = self.findChild(QPushButton, "bet_button")

        
        
        # self.bet_size = self.findChild(QLineEdit, "betsize")
        # # self.bet_size.setPlaceholderText('Type in Bet Here')
        

        
        
        
        # #click buttons
        # self.deal_button.clicked.connect(self.deal)
        # self.next_button.clicked.connect(self.next_)
        # self.bet_button.clicked.connect(self.bet)
        
        self.predict_pokemon_button.clicked.connect(self.predict_pokemon_)
        
        
        #show the app
        self.show()
        
    # def get_png(self, card):
    #     suits_dict = {'♠': 'spades', '♥': 'hearts', '♦': 'diamonds', '♣': 'clubs' }    
    #     nums_dict =  {2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
    #                   7: 7, 8: 8, 9: 9, 10: 10, 'J': 'jack', 
    #                   'Q': 'queen', 'K': 'king', 'A': 'ace'}
        
    #     return '{}_of_{}.png'.format(nums_dict[card[0]], suits_dict[card[1]])
    
    # code for predicting pokemon
    def predict_pokemon_(self, desc, model = model, filter_stopwords = True):


        desc = self.text_input.toPlainText()
        
        for descriptor in ['Pokémon', 'Pokemon', 'pokemon','pokémon']:
            if descriptor in desc:
                desc = desc.replace(descriptor,'')
        if filter_stopwords:
            desc = ' '.join([word for word in desc.split() if word not in (stop_words)])

        
        pred_inputs = tokenizer(desc, return_tensors="pt")
    
        with torch.no_grad():

            logits = model(**pred_inputs).logits


            predicted_class_id = logits.argmax().item()
            second_class_id = torch.topk(logits.flatten(), 3).indices[1]
            third_class_id = torch.topk(logits.flatten(), 3).indices[2]

            first_pokemon = class_converter.int2str(predicted_class_id)
            second_pokemon = class_converter.int2str(second_class_id.item())
            third_pokemon = class_converter.int2str(third_class_id.item())

        self.first_pokemon.setPixmap(QPixmap(f'PokéPNGs/{first_pokemon}.png'))
        self.second_pokemon.setPixmap(QPixmap(f'PokéPNGs/{second_pokemon}.png'))
        self.third_pokemon.setPixmap(QPixmap(f'PokéPNGs/{third_pokemon}.png'))

        self.ash_posttext.setHidden(False)
        self.ash_pretext.setHidden(True)
        self.ash_text.setHidden(True)
        self.i_choose_you.setHidden(False)

        self.first_place_name.setText(first_pokemon)
        self.second_place_name.setText(second_pokemon)
        self.third_place_name.setText(third_pokemon)


        
        
# UI.evaluate_seven = evaluate_seven   
# UI.face_dealer = face_dealer
# UI.best_hand_against_dealer = best_hand_against_dealer
# UI.get_payouts = get_payouts
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


