#import spacy as sp
import polars as pl
import tqdm as tq
import requests as req
import openpyxl as op
import morfeusz2 as mo
import requests
import json

from outdated.translateWord import translate

def find_top_n_words(num):
    df = pl.read_excel("subtlexWordsByFreq")
    df.columns = ["word", "freq"]
    return df

df = pl.read_excel("subtlexWordsByFreq.xlsx", columns=["spelling","dom.pos","dom.pos.freq"])
df = df.rename({"spelling": "word", "dom.pos":"word_type", "dom.pos.freq":"word_freq"})
df.remove(pl.col("word_freq") < 1000)

df.write_excel("dict.xlsx", worksheet="Dictionary")

translations = []

for row in df.iter_rows():
    if len(translations) // 100 == len(translations) / 100:
        print("")
        print("We've translated: "+ str(len(translations)) + " words!")
        print("")
    translations.append(translate(row[0]))

new_col = pl.Series("translation", translations)
df.insert_column(3, new_col)

print(df)
df.write_excel("dict.xlsx", worksheet="Dictionary")