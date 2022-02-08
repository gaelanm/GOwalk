import subprocess
import pandas as pd
import numpy as np


def HGNC(genes, name):
    """
    Useful to ensure gene nomenclature is up-to-date
    :param genes: gene list
    :param name: project name
    :return: update genes with HGNC approved gene symbols
    """
    #   write genes to feather
    genes.to_feather(
        f'projects/{name}/featherFiles/genes.feather'
    )

    #   perform check
    subprocess.call(
        ['R/HGNChelper.R',
            name
         ]
    )

    #   read the HGNC output
    genes = pd.read_feather(
        f'projects/{name}/featherFiles/genes.feather'
    )

    #   re-formatting pyarrow behavior
    genes = genes['Suggested.Symbol'][0].split(' ')

    delete = ['\"', ',', '(', ')', 'c']
    for element in range(len(genes)):
        for _ in delete:
            genes[element] = genes[element].replace(_, '')

    genes = pd.DataFrame(genes, columns=['Genes'])

    #   feather is updated with approved genes
    genes.to_feather(
        f'projects/{name}/featherFiles/genes.feather')

    return