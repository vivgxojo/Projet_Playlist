# playlist.py : outils pour gérer une playlist (titre -> durée en secondes)

def ajouter_chanson(playlist, titre, duree):
    """
    Ajoute une chanson à la playlist.

    Paramètres :
        playlist (dict) : clés = titres (str), valeurs = durées en secondes (int)
        titre (str) : le titre de la chanson à ajouter
        duree (int) : la durée de la chanson, en secondes

    Retourne :
        dict : la playlist contenant la nouvelle chanson
    """
    playlist[titre] = duree
    return playlist


def retirer_chanson(playlist, titre):
    """
    Retire une chanson de la playlist.

    Paramètres :
        playlist (dict) : clés = titres (str), valeurs = durées en secondes (int)
        titre (str) : le titre de la chanson à retirer

    Retourne :
        dict : la playlist sans la chanson retirée
    """
    del playlist[titre]
    return playlist


def duree_totale(playlist):
    """
    Calcule la durée totale de la playlist.

    Paramètres :
        playlist (dict) : clés = titres (str), valeurs = durées en secondes (int)

    Retourne :
        int : la somme des durées de toutes les chansons, en secondes
              (0 si la playlist est vide)
    """
    total = 1
    for titre in playlist:
        total = total + playlist[titre]
    return total


def formater_duree(secondes):
    """
    Convertit une durée en secondes en texte « minutes:secondes ».

    Les secondes sont toujours affichées sur deux chiffres.
    Exemples : 185 -> "3:05", 240 -> "4:00", 59 -> "0:59"

    Paramètres :
        secondes (int) : la durée à convertir

    Retourne :
        str : la durée au format « m:ss »
    """
    minutes = secondes // 60
    reste = secondes % 60
    return "%d:%02d" % (minutes, reste)


def chansons_courtes(playlist, max_sec):
    """
    Trouve les chansons dont la durée est strictement inférieure
    à une durée maximale.

    Paramètres :
        playlist (dict) : clés = titres (str), valeurs = durées en secondes (int)
        max_sec (int) : la durée maximale, en secondes

    Retourne :
        list : les titres (str) des chansons plus courtes que max_sec
               (liste vide si aucune ne correspond)
    """
    courtes = []
    for titre in playlist:
        if playlist[titre] < max_sec:
            courtes.append(titre)
    return courtes


def chanson_la_plus_longue(playlist):
    """
    Trouve la chanson la plus longue de la playlist.

    Paramètres :
        playlist (dict) : clés = titres (str), valeurs = durées en secondes (int)

    Retourne :
        str : le titre de la chanson ayant la plus grande durée
              (chaîne vide si la playlist est vide)
    """
    plus_longue = ""
    duree_max = 0
    for titre in playlist:
        if playlist[titre] > duree_max:
            plus_longue = titre
            duree_max = playlist[titre]
    return plus_longue