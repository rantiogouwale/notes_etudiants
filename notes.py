etudiants = []

def ajouter_etudiants(nom,note):
etudiants.append({"nom":nom,"note":note})
print(f"Etudiant {nom} ajouté avec la note}."}

def calculer_moyenne():
if not etudiants:
print("Aucun etudiant enregistre.")
return 0
total = sum(e['note'] for e in etudiants)
moyenne= total / len(etudiants)
print(f"Moyenne de la classe : {moyenne:.2f}")
return moyenne
