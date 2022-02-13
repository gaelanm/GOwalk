#   Script by Gaelan Melanson
#
#   Creates a Genes() object that holds a
#   list of interesting genes as well as methods
#   for functional enrichment analysis
#

import pandas as pd
import subprocess
import os
import utiliti
from enrich import enrichment


class UtilitEA(enrichment):

    def __init__(self, file):
        """
        :param name: user-defined project name
        :param self.genes: holds CSV of genes
        :param self.enrich: holds EA performed using gprofiler2 in R
        """
        self.name = None
        self.file = file
        self.genes = self.readGenes()


    def readGenes(self):
        """
        Reads user gene list into a Genes() object
        :param path: full path to csv
        :return: self.gene attribute
        """
        geneList = pd.read_csv(self.file, header=0)

        # feather format for passing data to Rscripts
        geneList.to_feather(
            f'projects/{self.name}/featherFiles/genes.feather'
        )

        return geneList

    def check(self, this):
        """
        Pseudo-methods for quick pre-processing
        :return: updates self.gene with HGNC-approved symbols
        """
        if this == 'HGNC':
            utiliti.HGNC(
                self.genes,
                    self.name
            )

            self.genes = pd.read_feather(
                f'projects/{self.name}/featherFiles/genes.feather'
            )


file = str(input('Full path to gene list: '))
proj = str(input('Project name: '))

#   empty object
z = UtilitEA(file)
z.name = proj

#   automatic directories
if not os.path.exists(f'projects/{proj}/featherFiles/'):
    os.makedirs(f'projects/{proj}/featherFiles/')
if not os.path.exists(f'projects/{proj}/data'):
    os.makedirs(f'projects/{proj}/data')

#   test
z.readGenes()
z.getEA(z.name)
z.getGO(z.name, 'BP', 'org.Hs.eg.db', 'Rel', 0.7)





