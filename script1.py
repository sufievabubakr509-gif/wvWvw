import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

def resource_path(path):
    try:
        base_path = sys._MEIPASS   # exe ichidagi vaqtinchalik papka
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

# -------------------- TILLAR --------------------
LANG = "uz"

TEXT = {
    "uz": {
        "search": "Qidiruv",
        "disease": "KASALLIK",
        "support": "Support admin: +998 (94) 077 01 36",
        "herbs": "Giyohlar",
        "usage": "Qo‘llanishi",
        "points": "Hijama nuqtalari",
        "mode": "Kun / Tun"
    },
    "en": {
        "search": "Search",
        "disease": "DISEASE",
        "support": "Support admin: +998 (94) 077 01 36",
        "herbs": "Herbs",
        "usage": "Usage",
        "points": "Hijama points",
        "mode": "Day / Night"
    },
    "ru": {
        "search": "Поиск",
        "disease": "БОЛЕЗНЬ",
        "support": "Поддержка: +998 (94) 077 01 36",
        "herbs": "Травы",
        "usage": "Применение",
        "points": "Точки хиджамы",
        "mode": "День / Ночь"
    }
}

# -------------------- KASALLIK MA'LUMOTI --------------------
DISEASES = {
    "Bel og‘rig‘i": {"herbs": "Zanjabil, qora sedana", "usage": "Kuniga 2 mahal choy qilib ichiladi", "image": "body.png"},
    "Bosh og‘rig‘i": {"herbs": "Yalpiz, romashka", "usage": "Issiq damlama ichiladi", "image": "body.png"},
    "Gripp": {"herbs": "Zanjabil, Limon, Asal", "usage": "Choy sifatida ichiladi", "image": "flu.png"},
    "Tomoq og‘rig‘i": {"herbs": "Zanjabil, Asal", "usage": "Choy ichiladi", "image": "throat.png"},
    "Uyqusizlik": {"herbs": "Lavanda, Valeriana", "usage": "Damlamani ichiladi", "image": "sleep.png"},
    "Stress": {"herbs": "Lavanda, Yalpiz", "usage": "Aromaterapiya yoki choy ichiladi", "image": "stress.png"},
    "Qon bosimi yuqori": {"herbs": "Sarimsoq, Yalpiz", "usage": "Choy ichiladi", "image": "bp_high.png"},
    "Qon bosimi past": {"herbs": "Zanjabil, Qora sedana", "usage": "Choy ichiladi", "image": "bp_low.png"},
    "Teri allergiyasi": {"herbs": "Aloe vera, Yalpiz", "usage": "Shilti surtiladi", "image": "skin.png"},
    "Shishlar": {"herbs": "Romashka, Aloe vera", "usage": "Shilti surtiladi", "image": "swelling.png"},
}

# -------------------- OYNA --------------------
app = ctk.CTk()
app.title("Hijama Medical App")

# -------------------- SIDEBAR --------------------
sidebar = ctk.CTkFrame(app, width=250)
sidebar.pack(side="left", fill="y", padx=10, pady=10)

search = ctk.CTkEntry(sidebar, placeholder_text=TEXT[LANG]["search"])
search.pack(pady=10, fill="x")

buttons_frame = ctk.CTkScrollableFrame(sidebar)
buttons_frame.pack(fill="both", expand=True)

# -------------------- MAIN --------------------
main = ctk.CTkFrame(app)
main.pack(side="right", fill="both", expand=True, padx=10, pady=10)

title = ctk.CTkLabel(main, text="", font=("Arial", 22, "bold"))
title.pack(pady=10)

info = ctk.CTkTextbox(main, height=150)
info.pack(fill="x", padx=20)

img_label = ctk.CTkLabel(main, text="")
img_label.pack(pady=10)

support = ctk.CTkLabel(main, text=TEXT[LANG]["support"])
support.pack(side="bottom", pady=10)

# -------------------- FUNKSIYALAR --------------------
def toggle_mode():
    current = ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark" if current == "Light" else "light")

def show_disease(name):
    d = DISEASES[name]
    title.configure(text=name)

    info.delete("1.0", "end")
    info.insert("end",
        f"{TEXT[LANG]['herbs']}: {d['herbs']}\n\n"
        f"{TEXT[LANG]['usage']}: {d['usage']}\n\n"
        f"{TEXT[LANG]['points']}:"
    )

    img_path = resource_path(d["image"])
    if os.path.exists(img_path):
        img = Image.open(img_path).resize((250, 350))
        photo = ImageTk.PhotoImage(img)
        img_label.configure(image=photo)
        img_label.image = photo
    else:
        img_label.configure(image=None)
        img_label.image = None

# -------------------- QIDIRUV FUNKSIYASI --------------------
def filter_diseases(*args):
    query = search.get().lower()
    for widget in buttons_frame.winfo_children():
        if query in widget.cget("text").lower():
            widget.pack(pady=5, fill="x")  # ko'rsatish
        else:
            widget.pack_forget()           # yashirish

search.bind("<KeyRelease>", filter_diseases)

# -------------------- TUGMALAR --------------------
for d in DISEASES:
    btn = ctk.CTkButton(
        buttons_frame,
        text=d.upper(),
        fg_color="darkred",
        command=lambda x=d: show_disease(x)
    )
    btn.pack(pady=5, fill="x")

mode_btn = ctk.CTkButton(
    sidebar,
    text=TEXT[LANG]["mode"],
    command=toggle_mode
)
mode_btn.pack(pady=10)

app.mainloop()
