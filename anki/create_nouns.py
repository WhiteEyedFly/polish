#!/usr/bin/env python3
"""
Polish Noun -> Anki Active Recall Generator

Input columns:
Thematic Group
English Translation
Polish Noun
Gender Category

Output:
Anki CSV with active recall cards.
"""

import csv
import random


def detect_delimiter(filename):
    with open(filename, encoding="utf-8-sig") as f:
        sample = f.read(2000)
    return "\t" if "\t" in sample else ","


def make_card(front, back, tags):
    return {"Front": front, "Back": back, "Tags": tags}


def get_article(gender):
    gender = gender.lower()

    if "feminine" in gender:
        return "ta"
    if "neuter" in gender:
        return "to"
    if "masculine" in gender:
        return "ten"

    return ""


def generate_cards(row):
    cards = []

    theme = row.get("Thematic Group", "").strip()
    english = row.get("English Translation", "").strip()
    noun = row.get("Polish Noun", "").strip()
    gender = row.get("Gender Category", "").strip()
    article = get_article(gender)

    if not english or not noun:
        return cards

    tag = f"noun active_recall {theme} {gender}"

    cards.append(make_card(noun, english, tag))

    cards.append(make_card(
        f"Translate: This {english}",
        f"{article} {noun}",
        tag + " recognition"
    ))

    return cards


def convert(input_file, output_file):
    delimiter = detect_delimiter(input_file)
    cards = []

    with open(input_file, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=delimiter)

        for row in reader:
            cards.extend(generate_cards(row))

    random.shuffle(cards)

    with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Front", "Back", "Tags"]
        )
        writer.writeheader()
        writer.writerows(cards)

    print(f"Generated {len(cards)} active recall Anki cards")


convert("anki/source/nouns.csv", "anki/output/anki_nouns.csv")
