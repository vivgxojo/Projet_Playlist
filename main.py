# main.py : programme principal de la playlist de party

# TODO 0 : corriger les erreurs de syntaxe dans le fichier playlist

# TODO 1 : importer le module playlist
import playlist as pl

# TODO 2 : créer le dictionnaire vide ma_playlist
#          et les listes titres et durees (5 éléments chacune)
ma_playlist: dict = {}
titres: list = [
    "Super Idol",
    "Red sun in the sky",
    "Moskau",
    "The red army is the strongest",
    "Gdzie jest biały węgorz (Zejście)"
]

durees: list = [
    123,
    231,
    912,
    102,
    412
]

# TODO 3 : avec une boucle for et range(len(titres)),
#          ajouter chaque chanson à ma_playlist
for i, _ in enumerate(titres):
    ma_playlist[titres[i]] = durees[i]


# TODO 4 : afficher chaque chanson avec sa durée formatée
#          (ex. : Nuit blanche - 3:05)

_ = [
   print(f"{titres[i]} - {pl.formater_duree(durees[i])}") for i in range(len(titres))
]


# TODO 5 : afficher la durée totale de la playlist, formatée
print()
print(pl.formater_duree(pl.duree_totale(ma_playlist)))

# TODO 6 : afficher la chanson la plus longue
print()
print(pl.chanson_la_plus_longue(ma_playlist))


# TODO 7 : demander une durée maximale en secondes (input, converti en int),
#          puis afficher la liste des chansons plus courtes que cette durée
while True:
    try:
        _input = int(input('Durée maximale: '))
        _ = [
            print(f"{titre} - {pl.formater_duree(ma_playlist[titre])}") for titre in pl.chansons_courtes(ma_playlist, _input)
        ]
        print()
        break
    except:
        pass


# TODO 8 : demander le titre d'une chanson à retirer
#          - si elle est absente : afficher un message
#          - sinon : la retirer et réafficher la playlist
titre_a_retirer = input("Chanson à enlever: ")
if titre_a_retirer in ma_playlist:
    del ma_playlist[titre_a_retirer]
    _ = [
        print(f"{titre} - {pl.formater_duree(ma_playlist[titre])}") for titre in ma_playlist
    ]
else:
    print("Mauvais")

# TODO 9 : tester votre programme, corriger les erreurs d'exécutions et de logique
#          incluant celles dans le module.

# TODO 10 : tester avec des valeurs incorrectes, exemple un titre qui n'existe pas,
#           une durée en str, et ajouter la gestion d'exceptions, incluant dans le module.
