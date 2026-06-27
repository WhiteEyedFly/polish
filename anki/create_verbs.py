#!/usr/bin/env python3
"""
Polish Verb Conjugation -> Anki Active Recall Generator

Input columns:
English
Verb
Conjugation group
Ja
Ty
On/ona/ono
My
Wy
Oni/one
Case

Output:
Anki CSV with active recall cards.

The cards test production:
- English meaning + subject -> Polish conjugation
- Polish infinitive + subject -> Polish conjugation
- Full paradigm recall
"""

import csv
import sys
import random


SUBJECTS = [
    ("Ja", "I"),
    ("Ty", "You"),
    ("On/ona/ono", "He/she/it"),
    ("My", "We"),
    ("Wy", "You (plural)"),
    ("Oni/one", "They"),
]


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

    english = row.get("English", "").strip()
    verb = row.get("Verb", "").strip()
    group = row.get("Conjugation group", "").strip()
    ja = row.get("Ja", "").strip()
    ty = row.get("Ty", "").strip()
    on = row.get("On/ona/ono", "").strip()
    my = row.get("My", "").strip()
    wy = row.get("Wy", "").strip()
    oni =row.get("Oni/one", "").strip()
    case = row.get("Case", "").strip()

    if not english or not verb:
        return cards

    tag = f"verb active_recall {group}"

    # Full paradigm recall
    full_prompt = (
        f"Translate {verb}\n"
        "Conjugate it in the present tense:\n\n"
        "Ja:\n"
        "Ty:\n"
        "On/ona/ono:\n"
        "My:\n"
        "Wy:\n"
        "Oni/one:"
    )

    full_answer = (
        f"{english}:: "
        f"Ja: {ja}, "
        f"Ty: {ty}, "
        f"On/ona/ono: {on}, "
        f"My: {my}, "
        f"Wy: {wy}, "
        f"Oni/one: {oni}"
    )

    cards.append(
        make_card(
            full_prompt,
            full_answer,
            tag + " full_paradigm"
        )
    )

    # Grammar recall
    """
    if case:
        cards.append(
            make_card(
                f"{verb}: what case does this verb require?",
                case,
                tag + " grammar"
            )
        )
    """
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


convert("anki/source/verbs.csv", "anki/output/anki_verbs.csv")
