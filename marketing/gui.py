# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from trends import get_google_trends
from twitter_trends import get_twitter_trends
from news import get_top_headlines
from utils import ensure_data_directory, save_to_csv
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image, ImageTk

class ContentIdeenGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Content-Ideen-Generator")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        # Fenstericon setzen
        # self.root.iconbitmap('assets/icon.ico')

        # API-Schlüssel hier einfügen
        self.twitter_api_key = 'TWITTER_API_KEY'
        self.twitter_api_secret_key = 'TWITTER_API_SECRET_KEY'
        self.twitter_access_token = 'TWITTER_ACCESS_TOKEN'
        self.twitter_access_token_secret = 'TWITTER_ACCESS_TOKEN_SECRET'
        self.news_api_key = 'NEWSAPI_KEY'

        self.ideas = []

        self.create_widgets()

    def create_widgets(self):
        # Logo hinzufügen
        # logo = Image.open('assets/logo.png')
        # logo = logo.resize((100, 100))
        # logo = ImageTk.PhotoImage(logo)
        # logo_label = tk.Label(self.root, image=logo)
        # logo_label.image = logo
        # logo_label.pack(pady=10)

        # Titel
        title_label = ttk.Label(self.root, text="Content-Ideen-Generator", font=("Helvetica", 18))
        title_label.pack(pady=10)

        # Eingabefeld für Keyword
        keyword_frame = ttk.Frame(self.root)
        keyword_frame.pack(pady=5)
        keyword_label = ttk.Label(keyword_frame, text="Keyword:")
        keyword_label.pack(side=tk.LEFT)
        self.keyword_entry = ttk.Entry(keyword_frame, width=50)
        self.keyword_entry.pack(side=tk.LEFT, padx=5)

        # Optionen
        options_frame = ttk.Frame(self.root)
        options_frame.pack(pady=5)
        self.google_var = tk.BooleanVar(value=True)
        self.twitter_var = tk.BooleanVar(value=True)
        self.news_var = tk.BooleanVar(value=True)

        google_check = ttk.Checkbutton(options_frame, text="Google Trends", variable=self.google_var)
        google_check.pack(side=tk.LEFT, padx=5)
        twitter_check = ttk.Checkbutton(options_frame, text="Twitter Trends", variable=self.twitter_var)
        twitter_check.pack(side=tk.LEFT, padx=5)
        news_check = ttk.Checkbutton(options_frame, text="News Headlines", variable=self.news_var)
        news_check.pack(side=tk.LEFT, padx=5)

        # Buttons
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=10)
        generate_button = ttk.Button(buttons_frame, text="Ideen generieren", command=self.generate_content_ideas)
        generate_button.pack(side=tk.LEFT, padx=5)
        save_button = ttk.Button(buttons_frame, text="Ergebnisse speichern", command=self.save_results)
        save_button.pack(side=tk.LEFT, padx=5)
        visualize_button = ttk.Button(buttons_frame, text="Visualisieren", command=self.visualize_data)
        visualize_button.pack(side=tk.LEFT, padx=5)

        # Ergebnisse anzeigen
        results_frame = ttk.Frame(self.root)
        results_frame.pack(pady=10)
        results_label = ttk.Label(results_frame, text="Ergebnisse:")
        results_label.pack(anchor=tk.W)
        self.results_text = tk.Text(results_frame, height=20, width=100)
        self.results_text.pack()

    def generate_content_ideas(self):
        keyword = self.keyword_entry.get().strip()
        if not keyword:
            messagebox.showwarning("Warnung", "Bitte geben Sie ein Keyword ein.")
            return

        self.results_text.delete(1.0, tk.END)
        self.ideas = []

        if self.google_var.get():
            self.results_text.insert(tk.END, "Google Trends:\n", 'header')
            gt_ideas = get_google_trends(keyword)
            for idea in gt_ideas:
                self.results_text.insert(tk.END, f"- {idea}\n")
            self.ideas.extend(gt_ideas)
            self.results_text.insert(tk.END, "\n")

        if self.twitter_var.get():
            self.results_text.insert(tk.END, "Twitter Trends:\n", 'header')
            tt_ideas = get_twitter_trends(
                self.twitter_api_key, self.twitter_api_secret_key,
                self.twitter_access_token, self.twitter_access_token_secret
            )
            for idea in tt_ideas:
                self.results_text.insert(tk.END, f"- {idea}\n")
            self.ideas.extend(tt_ideas)
            self.results_text.insert(tk.END, "\n")

        if self.news_var.get():
            self.results_text.insert(tk.END, "News Headlines:\n", 'header')
            news_ideas = get_top_headlines(self.news_api_key)
            for idea in news_ideas:
                self.results_text.insert(tk.END, f"- {idea}\n")
            self.ideas.extend(news_ideas)
            self.results_text.insert(tk.END, "\n")

        if not self.ideas:
            self.results_text.insert(tk.END, "Keine Ideen gefunden. Bitte versuchen Sie es mit anderen Einstellungen.\n")

    def save_results(self):
        if not self.ideas:
            messagebox.showwarning("Warnung", "Es gibt keine Ergebnisse zum Speichern.")
            return
        ensure_data_directory()
        save_to_csv(self.ideas)
        messagebox.showinfo("Erfolg", "Ergebnisse wurden erfolgreich gespeichert.")

    def visualize_data(self):
        if not self.ideas:
            messagebox.showwarning("Warnung", "Es gibt keine Daten zum Visualisieren.")
            return
        idea_counts = Counter(self.ideas)
        labels, values = zip(*idea_counts.items())
        plt.figure(figsize=(10, 5))
        plt.bar(labels, values, color='skyblue')
        plt.xticks(rotation=90)
        plt.title('Häufigkeit der Content-Ideen')
        plt.tight_layout()
        plt.show()