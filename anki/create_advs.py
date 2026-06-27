#!/usr/bin/env python3
"""
Polish Adverb -> Anki Active Recall Generator

Input columns:
Thematic Group
English Translation
Polish Adverb
Base Adjective Origin

Output:
Anki CSV with active recall cards.

Generated cards:
- English -> Polish adverb
- Polish adverb -> English
- Adverb -> adjective origin
- Full relationship recall
"""


import csv
import random



def detect_delimiter(filename):

    with open(filename, encoding="utf-8-sig") as f:
        sample = f.read(2000)

    return "\t" if "\t" in sample else ","



def make_card(front, back, tags):

    return {
        "Front": front,
        "Back": back,
        "Tags": tags
    }



def generate_cards(row):

    cards = []
    theme = row.get("Thematic Group", "").strip()

    english = (
        row.get("English Translation", "")
        .strip()
        .lower()
    )

    adverb = (
        row.get("Polish Adverb", "")
        .strip()
    )

    if not english or not adverb:
        return cards

    tag = (
        f"adverb "
        f"active_recall "
        f"theme::{theme.replace(' ', '_')}"
    )

    # English -> Polish adverb

    cards.append(
        make_card(
            f"Translate: {english}",
            adverb,
            tag
        )
    )

    # Polish -> English recognition

    cards.append(
        make_card(
            f"Translate: {adverb}",
            english,
            tag + " recognition"
        )
    )


    return cards





def convert(input_file, output_file):

    delimiter = detect_delimiter(input_file)

    cards = []


    with open(input_file, encoding="utf-8-sig") as f:

        reader = csv.DictReader(
            f,
            delimiter=delimiter
        )


        for row in reader:

            cards.extend(
                generate_cards(row)
            )


    random.shuffle(cards)



    with open(
        output_file,
        "w",
        encoding="utf-8-sig",
        newline=""
    ) as f:


        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Front",
                "Back",
                "Tags"
            ]
        )

        writer.writeheader()
        writer.writerows(cards)



    print(
        f"Generated {len(cards)} active recall Anki cards"
    )

convert("anki/source/advs.csv", "anki/output/anki_advs.csv")