import tkinter as tk
import random
import string
def generer():
    try:
        longueur = int(entree.get())
        caracteres = string.ascii_letters + string.digits + string.punctuation
        mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
        resultat.config(text=mot_de_passe)
    except:
        resultat.config(text="Entrée invalide")
def copier():
    mot = resultat.cget("text")
    if mot:
        fenetre.clipboard_clear()
        fenetre.clipboard_append(mot)
        copier_btn.config(text="Copié !", bg="lightgreen")
        fenetre.after(1500, lambda: copier_btn.config(text="Copier", bg="SystemButtonFace"))

fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")

tk.Label(fenetre, text="Longueur du mot de passe :").pack()
entree = tk.Entry(fenetre)
entree.pack()

tk.Button(fenetre, text="Générer", command=generer).pack(pady=5)

resultat = tk.Label(fenetre, text="", font=("Arial", 12, "bold"), fg="green")
resultat.pack(pady=10)

copier_btn = tk.Button(fenetre, text="Copier", command=copier)
copier_btn.pack()

fenetre.mainloop()
tk.Button(fenetre, text="Générer", command=generer).pack(pady=5)

resultat = tk.Label(fenetre, text="", font=("Arial", 12, "bold"), fg="green")
resultat.pack(pady=10)

fenetre.mainloop()