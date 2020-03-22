import requests

url_base = 'https://python.gel.ulaval.ca/quoridor/api'


def lister_parties(idul):
    rep = requests.get(f'{url_base}/lister/', params={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
        return rep['parties']
    raise RuntimeError(f"Le GET sur {url_base + 'lister'} a produit le code d'erreur {rep.status_code}.")


id_partie = None
def initialiser_partie(idul):
    rep = requests.post(f'{url_base}/initialiser/', data={'idul': idul})
    dico = rep.json()
    if "message" in dico:
        print(dico["message"])
    if rep.status_code != 200:
        raise RuntimeError(f"Le GET sur {url_base + 'initialiser'} a produit le code d'erreur {rep.status_code}.")
    return dico

def jouer_coup(id_partie, type_coup, position):
    rep = requests.post(f'{url_base}/jouer/')
    dico = rep.json()
    if dico.post('gagnant'):
        raise StopIteration(f'Le gagnant est {dico["gagnant"]}')
    if dico.post('message'):
        return dico['message']
    return dico['état']

# Cette section est pour tester l'état des fonction
print(initialiser_partie('chass38'))