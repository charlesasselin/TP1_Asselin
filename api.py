"""Ce module et ses fonctions assure la connection avec le serveur de jeu"""
import requests

URL_BASE = 'https://python.gel.ulaval.ca/quoridor/api'


def lister_parties(idul):
    """Cette fonction permet de lister les dernières parties du joueur avec l'IDUL correspondant"""
    rep = requests.get(
        f'{URL_BASE}/lister/',
        params={
            'idul': idul
        }
    )
    if rep.status_code == 200:
        rep = rep.json()
        return rep['parties']
    raise RuntimeError(
        f"Le GET sur {URL_BASE + 'lister'} a produit le code d'erreur {rep.status_code}."
    )


def initialiser_partie(idul):
    """Cette fonction initialise la partie en lui donnant un id"""
    rep = requests.post(
        f'{URL_BASE}/initialiser/',
        data={
            'idul': idul
        }
    )
    dico = rep.json()
    if 'message' in dico:
        raise RuntimeError(dico['message'])
    return dico


def jouer_coup(id_partie, type_coup, position):
    """Cette fonction permet au joueur d'entrer son coup et de le transférer au serveur"""
    rep = requests.post(
        f'{URL_BASE}/jouer/',
        data={
            'id': id_partie,
            'type': type_coup,
            'pos': position
        }
    )
    dico = rep.json()
    if 'gagnant' in dico:
        raise StopIteration(f'Le gagnant est {dico["gagnant"]}')
    if 'message' in dico:
        raise RuntimeError(dico['message'])
    return dico['état']
