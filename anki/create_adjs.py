#!/usr/bin/env python3
"""
Polish Adjective -> Anki Active Recall Generator

Input columns:
Thematic Group
English Translation
Polish Adjective
Feminine Singular Form
Neuter Singular Form

Output:
Anki CSV with active recall cards.

Generated cards:
- English -> masculine adjective
- English -> feminine adjective
- English -> neuter adjective
- Masculine -> feminine transformation
- Masculine -> neuter transformation
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
    english = row.get("English Translation", "").strip().lower()

    masculine = row.get("Polish Adjective", "").strip()
    feminine = row.get("Feminine Singular Form", "").strip()
    neuter = row.get("Neuter Singular Form", "").strip()


    if not english or not masculine:
        return cards


    tag = (
        f"adjective "
        f"active_recall "
        f"theme::{theme.replace(' ', '_')}"
    )
    # Translate
    cards.append(
        make_card(
            f"Translate: (masc) \n\n{masculine}",
            (
                f"{english}"
            ),
            tag + " paradigm"
        )
    )

    # Full paradigm recall
    cards.append(
        make_card(
            f"Give all forms:\n\n{english}",
            (
                f"Masculine: {masculine}\n"
                f"Feminine: {feminine}\n"
                f"Neuter: {neuter}"
            ),
            tag + " paradigm"
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

convert("anki/source/adjs.csv", "anki/output/anki_adjs.csv")