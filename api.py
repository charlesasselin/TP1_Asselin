import requests

def lister_parties(idul):

    url_base = 'https://python.gel.ulaval.ca/quoridor/api'

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
        raise RuntimeError(f"Le GET sur {url_base + 'lister'} a produit le code d'erreur {rep.status_code}.")
    else:
        return dico['id'], dico['état']