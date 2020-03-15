import argparse


def analyser_commande():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-h', '--help', help = 'show this message and exit'
    )

    parser.add_argument(
        '-l', '--lister', help= 'Lister les identifiants de vos 20 dernieres parties'
    )

    return parser.parse_args()