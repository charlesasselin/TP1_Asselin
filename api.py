import requests

url_base = 'https://python.gel.ulaval.ca/quoridor/api'

def lister_parties(idul):



    rep = requests.get(f'{url_base}/lister/', params={'idul': idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
        return rep['parties']
    else:
        raise RuntimeError(f"Le GET sur {url_base + 'lister'} a produit le code d'erreur {rep.status_code}.")

def initialiser_partie(idul):
    rep = requests.post(f'{url_base}/initialiser/', data={'idul': idul})
    dico = rep.json()
    if dico.get(['message']):
        raise RuntimeError(f"Le GET sur {url_base + 'initialiser'} a produit le code d'erreur {rep.status_code}.")
    else:
        return dico['id'], dico['état']

def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(f'{url_base}/jouer/')
    dico = rep.json()
    if dico.get(['gagnant']):
        raise StopIteration(f'Le gagnant est {dico["gagnant"]}')
    elif dico.get(['message']):
        raise RuntimeError(f"Le GET sur {url_base + 'jouer'} a produit le code d'erreur {rep.status_code}.")
    else:
        return dico['état']