"""
Module provides basic methods for analyzing gene lists
"""
import requests
import pandas as pd

def stringdb_pairwise(genes, species='9606'):

    # requires taxonomy ID
    species = f'&species={species}'
    STRINGdb = 'https://string-db.org'
    method = '/api/tsv/network?identifiers='
    genes = '%0d'.join([gene for gene in genes.iloc[:, 0]])

    response = requests.get(''.join([STRINGdb, method, genes, species]))
    response = str(response.content)
    response = [line.split('\\t') for line in response.split('\\n')]
    response = pd.DataFrame(response[1:], columns=response[0])
    response.dropna(axis=0, how='any', inplace=True)
    response['score'] = response['score'].astype(float)

    return response


def neighbourhood_adjacency(pairwise):

    labels = list(
        set(
            list(pairwise['preferredName_B']) +
            list(pairwise['preferredName_A'])
        )
    )

    adjacency = pd.DataFrame(0, index=labels, columns=labels)

    # weighted adjacency matrix
    for geneA, geneB, score in zip(pairwise['preferredName_A'], pairwise['preferredName_B'],
                                   pairwise['score']):
        adjacency.loc[geneB, geneA] = score
        adjacency.loc[geneA, geneB] = score

    return adjacency

