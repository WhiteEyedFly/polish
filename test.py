# AI GENERATED

import tkinter as tk
from tkinter import ttk, messagebox
import random

# ==========================================
# MASTER B1 VOCABULARY ECOSYSTEM DATABASES
# ==========================================

VERB_DB = [
    {"eng": "Love", "pl": "kochać", "grp": "C1", "case": "accusative", "conj": {"ja": "kocham", "ty": "kochasz", "on/ona/ono": "kocha", "my": "kochamy", "wy": "kochacie", "oni/one": "kochają"}},
    {"eng": "Know person", "pl": "znać", "grp": "C1", "case": "accusative", "conj": {"ja": "znam", "ty": "znasz", "on/ona/ono": "zna", "my": "znamy", "wy": "znacie", "oni/one": "znają"}},
    {"eng": "Know fact", "pl": "wiedzieć", "grp": "irregular", "case": "accusative", "conj": {"ja": "wiem", "ty": "wiesz", "on/ona/ono": "wie", "my": "wiemy", "wy": "wiecie", "oni/one": "wiedzą"}},
    {"eng": "Do / make", "pl": "robić", "grp": "C3", "case": "accusative", "conj": {"ja": "robię", "ty": "robisz", "on/ona/ono": "robi", "my": "robimy", "wy": "robicie", "oni/one": "robią"}},
    {"eng": "Learn / study", "pl": "uczyć się", "grp": "C3", "case": "genitive", "conj": {"ja": "uczę się", "ty": "uczysz się", "on/ona/ono": "uczy się", "my": "uczymy się", "wy": "uczycie się", "oni/one": "uczą się"}},
    {"eng": "Write", "pl": "pisać", "grp": "C4", "case": "accusative", "conj": {"ja": "piszę", "ty": "piszesz", "on/ona/ono": "pisze", "my": "piszemy", "wy": "piszecie", "oni/one": "piszą"}},
    {"eng": "Be", "pl": "być", "grp": "irregular", "case": "instrumental", "conj": {"ja": "jestem", "ty": "jesteś", "on/ona/ono": "jest", "my": "jesteśmy", "wy": "jesteście", "oni/one": "są"}},
    {"eng": "Have", "pl": "mieć", "grp": "C2", "case": "accusative", "conj": {"ja": "mam", "ty": "masz", "on/ona/ono": "ma", "my": "mamy", "wy": "macie", "oni/one": "mają"}},
    {"eng": "Drive into", "pl": "wjechać", "grp": "C4", "case": "instrumental", "conj": {"ja": "wjadę", "ty": "wjedziesz", "on/ona/ono": "wjedzie", "my": "wjedziemy", "wy": "wjedziecie", "oni/one": "wjadą"}},
    {"eng": "It is necessary / must", "pl": "trzeba", "grp": "impersonal", "case": "infinitive", "conj": {"impersonal": "trzeba"}}
]

NOUN_DB = [
    {"grp": "Places", "eng": "School", "pl": "szkoła", "gen": "Feminine", "end": "Hard consonant (-a)"},
    {"grp": "Countries", "eng": "Germany", "pl": "Niemcy", "gen": "Masculine Inanimate", "end": "Plural-only noun"},
    {"grp": "Family members", "eng": "Father", "pl": "ojciec", "gen": "Masculine Personal", "end": "Drops 'e' and changes c to j (ojca)"},
    {"grp": "Days", "eng": "Monday", "pl": "poniedziałek", "gen": "Masculine Inanimate", "end": "Drops 'e' (poniedziałku)"},
    {"grp": "Months", "eng": "January", "pl": "styczeń", "gen": "Masculine Inanimate", "end": "Soft consonant (drops 'e': stycznia)"},
    {"grp": "Foods", "eng": "Apple", "pl": "jabłko", "gen": "Neuter", "end": "Velar consonant (-ko)"}
]

ADJ_ADV_DB = [
    {"grp": "Descriptions & Sizes", "eng": "Big / large", "pl_adj": "duży", "pl_adv": "dobrze", "stem": "Hard stem"},
    {"grp": "Descriptions & Sizes", "eng": "Tall / high", "pl_adj": "wysoki", "pl_adv": "wysoko", "stem": "Velar stem (-ki)"},
    {"grp": "Opinions & Feelings", "eng": "Good", "pl_adj": "dobry", "pl_adv": "dobrze", "stem": "Hard stem"},
    {"grp": "Daily Life & State", "eng": "Cheap", "pl_adj": "tani", "pl_adv": "tanio", "stem": "Soft stem (-ni)"}
]

STRUCTURAL_DB = [
    {"type": "Preposition", "eng": "To / into", "pl": "do", "rule": "genitive"},
    {"type": "Preposition", "eng": "Between", "pl": "między", "rule": "instrumental"},
    {"type": "Conjunction", "eng": "Because", "pl": "ponieważ", "rule": "Always requires a comma before it"},
    {"type": "Conjunction", "eng": "Although / even though", "pl": "mimo że", "rule": "Introduces a counter-premise"}
]

# ==========================================
# APP ENGINE CORE GRAPHICAL INTERFACE
# ==========================================

class PolishB1MasterSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("Polish B1 Language Engine Suite")
        self.root.geometry("720x560")
        
        # Fixed Scoring Dictionary Trackers
        self.scores_correct = {"verb": 0, "noun": 0, "adj": 0, "struct": 0}
        self.scores_total = {"verb": 0, "noun": 0, "adj": 0, "struct": 0}
        
        # Tabbed Layout Framework
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.build_verb_tab()
        self.build_noun_tab()
        self.build_adj_adv_tab()
        self.build_structural_tab()
        self.build_generation_tab()
        
    def create_score_row(self, frame):
        lbl = tk.Label(frame, text="Score: 0/0", font=("Arial", 11, "bold"), fg="#444")
        lbl.pack(anchor="ne", padx=15, pady=5)
        return lbl

    # ------------------------------------------
    # VERB VERIFICATION ENGINE
    # ------------------------------------------
    def build_verb_tab(self):
        self.v_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.v_frame, text="Verbs Matrix")
        
        self.v_score_lbl = self.create_score_row(self.v_frame)
        
        tk.Label(self.v_frame, text="Translate English Focus Verb:", font=("Arial", 11)).pack(pady=2)
        self.v_target_lbl = tk.Label(self.v_frame, text="", font=("Arial", 15, "bold", "italic"), fg="#1a73e8")
        self.v_target_lbl.pack(pady=4)
        
        tk.Label(self.v_frame, text="Infinitive Target (lowercase):").pack()
        self.v_inf_ent = ttk.Entry(self.v_frame, font=("Arial", 11), width=35)
        self.v_inf_ent.pack(pady=2)
        
        tk.Label(self.v_frame, text="Conjugation Group Code (C1, C2, C3, C4, irregular, impersonal):").pack()
        self.v_grp_ent = ttk.Entry(self.v_frame, font=("Arial", 11), width=35)
        self.v_grp_ent.pack(pady=2)
        
        self.v_subj_lbl = tk.Label(self.v_frame, text="Conjugation Target:", font=("Arial", 10, "bold"))
        self.v_subj_lbl.pack(pady=4)
        self.v_conj_ent = ttk.Entry(self.v_frame, font=("Arial", 11), width=35)
        self.v_conj_ent.pack(pady=2)
        
        ttk.Button(self.v_frame, text="Verify Verb Parameters", command=self.eval_verb).pack(pady=15)
        self.next_verb()

    def next_verb(self):
        self.v_inf_ent.delete(0, tk.END); self.v_grp_ent.delete(0, tk.END); self.v_conj_ent.delete(0, tk.END)
        self.cur_v = random.choice(VERB_DB)
        self.v_target_lbl.config(text=self.cur_v["eng"])
        self.cur_v_subj = random.choice(list(self.cur_v["conj"].keys()))
        self.v_subj_lbl.config(text=f"Conjugate Entry for Form: '{self.cur_v_subj}'")

    def eval_verb(self):
        inf, grp, conj = self.v_inf_ent.get().strip().lower(), self.v_grp_ent.get().strip(), self.v_conj_ent.get().strip().lower()
        if inf == self.cur_v["pl"].lower() and grp == self.cur_v["grp"] and conj == self.cur_v["conj"][self.cur_v_subj].lower():
            messagebox.showinfo("Matrix Match", "Flawless validation across all paradigm segments!")
            self.scores_correct["verb"] += 1
        else:
            messagebox.showerror("Fault Injected", f"Verification Rejected!\n\nExpected: {self.cur_v['pl']} [{self.cur_v['grp']}]\nForm '{self.cur_v_subj}': {self.cur_v['conj'][self.cur_v_subj]}")
        self.scores_total["verb"] += 1
        self.v_score_lbl.config(text=f"Score: {self.scores_correct['verb']}/{self.scores_total['verb']}")
        self.next_verb()

    # ------------------------------------------
    # NOUN VERIFICATION ENGINE
    # ------------------------------------------
    def build_noun_tab(self):
        self.n_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.n_frame, text="Thematic Nouns")
        
        self.n_score_lbl = self.create_score_row(self.n_frame)
        self.n_grp_lbl = tk.Label(self.n_frame, text="Thematic Domain Group: ", font=("Arial", 10, "italic"))
        self.n_grp_lbl.pack()
        
        self.n_target_lbl = tk.Label(self.n_frame, text="", font=("Arial", 15, "bold"), fg="#e67e22")
        self.n_target_lbl.pack(pady=5)
        
        tk.Label(self.n_frame, text="Polish Translation Noun (lowercase):").pack()
        self.n_trans_ent = ttk.Entry(self.n_frame, font=("Arial", 11), width=35)
        self.n_trans_ent.pack(pady=2)
        
        tk.Label(self.n_frame, text="Gender Category Allocation (e.g. Feminine, Neuter, Masculine Personal):").pack()
        self.n_gen_ent = ttk.Entry(self.n_frame, font=("Arial", 11), width=35)
        self.n_gen_ent.pack(pady=2)
        
        ttk.Button(self.n_frame, text="Verify Noun Identity", command=self.eval_noun).pack(pady=20)
        self.next_noun()

    def next_noun(self):
        self.n_trans_ent.delete(0, tk.END); self.n_gen_ent.delete(0, tk.END)
        self.cur_n = random.choice(NOUN_DB)
        self.n_grp_lbl.config(text=f"Thematic Domain Group: [ {self.cur_n['grp']} ]")
        self.n_target_lbl.config(text=self.cur_n["eng"])

    def eval_noun(self):
        pl, gen = self.n_trans_ent.get().strip().lower(), self.n_gen_ent.get().strip().lower()
        if pl == self.cur_n["pl"].lower() and gen == self.cur_n["gen"].lower():
            messagebox.showinfo("Lexical Match", "Declension profile variables validated.")
            self.scores_correct["noun"] += 1
        else:
            messagebox.showerror("Declension Error", f"Incorrect assignment!\n\nTarget Word: {self.cur_n['pl']}\nGender Category: {self.cur_n['gen']}\nStructural Model: {self.cur_n['end']}")
        self.scores_total["noun"] += 1
        self.n_score_lbl.config(text=f"Score: {self.scores_correct['noun']}/{self.scores_total['noun']}")
        self.next_noun()

    # ------------------------------------------
    # ADJECTIVE & ADVERB TARGET COUPLING
    # ------------------------------------------
    def build_adj_adv_tab(self):
        self.a_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.a_frame, text="Adjectives & Adverbs")
        
        self.a_score_lbl = self.create_score_row(self.a_frame)
        
        tk.Label(self.a_frame, text="Structural Modification Base Root:", font=("Arial", 11)).pack()
        self.a_target_lbl = tk.Label(self.a_frame, text="", font=("Arial", 15, "bold"), fg="#9b59b6")
        self.a_target_lbl.pack(pady=5)
        
        tk.Label(self.a_frame, text="Polish Adjective Form (Masculine Dictionary):").pack()
        self.a_adj_ent = ttk.Entry(self.a_frame, font=("Arial", 11), width=35)
        self.a_adj_ent.pack(pady=2)
        
        tk.Label(self.a_frame, text="Derived Polish Adverb Form:").pack()
        self.a_adv_ent = ttk.Entry(self.a_frame, font=("Arial", 11), width=35)
        self.a_adv_ent.pack(pady=2)
        
        ttk.Button(self.a_frame, text="Validate Derived Forms", command=self.eval_adj_adv).pack(pady=20)
        self.next_adj_adv()

    def next_adj_adv(self):
        self.a_adj_ent.delete(0, tk.END); self.a_adv_ent.delete(0, tk.END)
        self.cur_a = random.choice(ADJ_ADV_DB)
        self.a_target_lbl.config(text=self.cur_a["eng"])

    def eval_adj_adv(self):
        adj, adv = self.a_adj_ent.get().strip().lower(), self.a_adv_ent.get().strip().lower()
        if adj == self.cur_a["pl_adj"].lower() and adv == self.cur_a["pl_adv"].lower():
            messagebox.showinfo("Lexical Concord", "Adjective-Adverb transformation logic confirmed.")
            self.scores_correct["adj"] += 1
        else:
            messagebox.showerror("Morpheme Mismatch", f"Transformation Failure!\n\nAdjective: {self.cur_a['pl_adj']}\nAdverb: {self.cur_a['pl_adv']}\nStem Properties: {self.cur_a['stem']}")
        self.scores_total["adj"] += 1
        self.a_score_lbl.config(text=f"Score: {self.scores_correct['adj']}/{self.scores_total['adj']}")
        self.next_adj_adv()

    # ------------------------------------------
    # CONNECTORS & CASE-GOVERNMENT VERIFICATION
    # ------------------------------------------
    def build_structural_tab(self):
        self.s_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.s_frame, text="Structural Framework")
        
        self.s_score_lbl = self.create_score_row(self.s_frame)
        self.s_type_lbl = tk.Label(self.s_frame, text="Functional Variable Class: ", font=("Arial", 10, "italic"))
        self.s_type_lbl.pack()
        
        self.s_target_lbl = tk.Label(self.s_frame, text="", font=("Arial", 15, "bold"), fg="#16a085")
        self.s_target_lbl.pack(pady=5)
        
        tk.Label(self.s_frame, text="Polish Operator Translation:").pack()
        self.s_trans_ent = ttk.Entry(self.s_frame, font=("Arial", 11), width=35)
        self.s_trans_ent.pack(pady=2)
        
        tk.Label(self.s_frame, text="Governed Case / Structural Operational Rule:").pack()
        self.s_rule_ent = ttk.Entry(self.s_frame, font=("Arial", 11), width=35)
        self.s_rule_ent.pack(pady=2)
        
        ttk.Button(self.s_frame, text="Verify Operator Logic", command=self.eval_structural).pack(pady=20)
        self.next_structural()

    def next_structural(self):
        self.s_trans_ent.delete(0, tk.END); self.s_rule_ent.delete(0, tk.END)
        self.cur_s = random.choice(STRUCTURAL_DB)
        self.s_type_lbl.config(text=f"Functional Variable Class: [ {self.cur_s['type']} ]")
        self.s_target_lbl.config(text=self.cur_s["eng"])

    def eval_structural(self):
        pl, rule = self.s_trans_ent.get().strip().lower(), self.s_rule_ent.get().strip().lower()
        if pl == self.cur_s["pl"].lower() and rule == self.cur_s["rule"].lower():
            messagebox.showinfo("Syntactic Fit", "Operational grammar requirements successfully validated.")
            self.scores_correct["struct"] += 1
        else:
            messagebox.showerror("Syntactic Break", f"Incorrect system variables!\n\nTarget Form: {self.cur_s['pl']}\nAssigned Rule/Case: {self.cur_s['rule']}")
        self.scores_total["struct"] += 1
        self.s_score_lbl.config(text=f"Score: {self.scores_correct['struct']}/{self.scores_total['struct']}")
        self.next_structural()
    
    # ------------------
    # Sentence generator
    # ------------------
    
    def build_generation_tab(self):
        """Constructs the new 5th Tab for live grammar transformation puzzles."""
        self.g_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.g_frame, text="Sentence Lab")

        # Static Local Pools for the Generation Engine
        self.g_subjects = ["ja", "ty", "on", "ona", "my", "wy", "oni"]
        self.g_verbs = {
            "robić": {"eng": "to do / make", "case": "accusative", "conj": {"ja": "robię", "ty": "robisz", "on": "robi", "ona": "robi", "my": "robimy", "wy": "robicie", "oni": "robią"}},
            "pić": {"eng": "to drink", "case": "accusative", "conj": {"ja": "piję", "ty": "pijesz", "on": "pije", "ona": "pije", "my": "pijemy", "wy": "pijecie", "oni": "piją"}},
            "szukać": {"eng": "to look for", "case": "genitive", "conj": {"ja": "szukam", "ty": "szukasz", "on": "szuka", "ona": "szuka", "my": "szukamy", "wy": "szukają", "oni": "szukają"}},
            "potrzebować": {"eng": "to need", "case": "genitive", "conj": {"ja": "potrzebuję", "ty": "potrzebujesz", "on": "potrzebuje", "ona": "potrzebuje", "my": "potrzebujemy", "wy": "potrzebujecie", "oni": "potrzebują"}},
            "być": {"eng": "to be", "case": "instrumental", "conj": {"ja": "jestem", "ty": "jesteś", "on": "jest", "ona": "jest", "my": "jesteśmy", "wy": "jesteście", "oni": "są"}}
        }
        self.g_nouns = [
            {"eng": "coffee", "pl": "kawa", "gen": "Feminine"},
            {"eng": "book", "pl": "książka", "gen": "Feminine"},
            {"eng": "house", "pl": "dom", "gen": "Masculine Inanimate"},
            {"eng": "doctor", "pl": "lekarz", "gen": "Masculine Personal"},
            {"eng": "teacher", "pl": "nauczyciel", "gen": "Masculine Personal"}
        ]
        self.g_adjectives = [
            {"eng": "good", "masc": "dobry", "fem": "dobra", "neut": "dobre"},
            {"eng": "new", "masc": "nowy", "fem": "nowa", "neut": "nowe"},
            {"eng": "bad", "masc": "zły", "fem": "zła", "neut": "złe"}
        ]

        # UI Prompts
        tk.Label(self.g_frame, text="Translate and construct the target sentence structure:", font=("Arial", 11)).pack(pady=5)
        self.g_eng_prompt = tk.Label(self.g_frame, text="", font=("Arial", 13, "bold"), fg="#2c3e50")
        self.g_eng_prompt.pack(pady=5)

        self.g_hint_lbl = tk.Label(self.g_frame, text="", font=("Arial", 9, "italic"), fg="#7f8c8d")
        self.g_hint_lbl.pack(pady=2)

        # User Entry Field
        tk.Label(self.g_frame, text="Your Complete Polish Sentence (Include the full stop):").pack(pady=5)
        self.g_user_ent = ttk.Entry(self.g_frame, font=("Arial", 12), width=50)
        self.g_user_ent.pack(pady=2)

        # Trigger Controls
        ttk.Button(self.g_frame, text="Verify Full Sentence", command=self.eval_generated_sentence).pack(pady=15)
        self.next_generated_puzzle()

    def run_case_logic(self, noun_dict, adj_dict, case):
        """Internal text transformer mapping out case agreement rules."""
        gender = noun_dict["gen"]
        noun_base = noun_dict["pl"]
        adj_base = adj_dict["fem"] if gender == "Feminine" else adj_dict["masc"]
        
        if case == "accusative":
            if gender == "Feminine":
                return adj_base[:-1] + "ą", noun_base[:-1] + "ę"
            elif gender == "Masculine Inanimate":
                return adj_base, noun_base
            elif gender == "Masculine Personal":
                return adj_base[:-1] + "ego", noun_base + "a"
        elif case == "genitive":
            if gender == "Feminine":
                return adj_base[:-1] + "ej", noun_base[:-1] + "y"
            elif gender in ["Masculine Inanimate", "Masculine Personal"]:
                ending = "u" if noun_base == "dom" else "a"
                return adj_base[:-1] + "ego", noun_base + ending
        elif case == "instrumental":
            if gender == "Feminine":
                return adj_base[:-1] + "ą", noun_base[:-1] + "ą"
            elif gender in ["Masculine Inanimate", "Masculine Personal"]:
                adj_ending = "im" if adj_base[-2] in ["k", "g"] else "ym"
                return adj_base[:-1] + adj_ending, noun_base + "em"
        return adj_base, noun_base

    def next_generated_puzzle(self):
        self.g_user_ent.delete(0, tk.END)
        
        # Safely extract random components
        subj = random.choice(self.g_subjects)
        verb_key = random.choice(list(self.g_verbs.keys()))
        noun = random.choice(self.g_nouns)
        adj = random.choice(self.g_adjectives)
        
        verb_data = self.g_verbs[verb_key]
        case_needed = verb_data["case"]
        
        # Block illogical combinations from rendering
        if (verb_key == "być" and noun["gen"] == "Masculine Inanimate") or \
           (verb_key in ["pić", "szukać", "robić"] and noun["gen"] == "Masculine Personal") or \
           (verb_key == "pić" and noun["pl"] == "dom"):
            self.next_generated_puzzle()
            return

        # Precompute correct string properties
        conj_verb = verb_data["conj"][subj]
        trans_adj, trans_noun = self.run_case_logic(noun, adj, case_needed)
        
        self.target_sentence = f"{subj.capitalize()} {conj_verb} {trans_adj} {trans_noun}."
        english_prompt = f"{subj.capitalize()} {verb_data['eng']} a {adj['eng']} {noun['eng']}."
        hint_text = f"Grammar Rule: Verb '{verb_key}' demands noun phrase to be placed in the {case_needed.upper()} case."

        self.g_eng_prompt.config(text=english_prompt)
        self.g_hint_lbl.config(text=hint_text)

    def eval_generated_sentence(self):
        user_input = self.g_user_ent.get().strip()
        
        if user_input.lower() == self.target_sentence.lower():
            messagebox.showinfo("Syntax Perfect", f"Excellent! Syntactic and morphological integration match standard target forms perfectly.")
        else:
            messagebox.showerror("Syntax Error", f"Incorrect casing or word alignment detected!\n\nExpected:\n{self.target_sentence}\n\nYou Entered:\n{user_input}")
        
        self.next_generated_puzzle()

# ==========================================
# RUN ENGINE LOOP
# ==========================================
if __name__ == "__main__":
    app_root = tk.Tk()
    suite = PolishB1MasterSuite(app_root)
    app_root.mainloop()
