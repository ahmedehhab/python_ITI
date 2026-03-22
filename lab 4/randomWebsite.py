import random
import webbrowser

websites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.github.com",
]

chosen_site = random.choice(websites)

webbrowser.open(chosen_site)