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

class UtilitEA:

    def __init__(self, file, name):
        """
        :param self.name: user-defined project name
        :param self.file: gene list path
        :param self.genes: holds gene list
        :param self.GO: GO terms
        :param self.ont: BP, MF, or CC
        :param self.orgdb: org.Hs.eg.db
        :param self.threshold: semantic similarity cut-off
        :param self.method: semsim algorithm
        """
        self.name = name
        self.file = file
        self.genes = self.readGenes()
        self.GO = None
        self.ont = None
        self.orgdb = None
        self.threshold = 0
        self.method = None

    def readGenes(self):
        """
        Imports user's gene list
        """
        geneList = pd.read_csv(self.file, header=0)

        # feather format for passing data to Rscripts
        geneList.to_feather(
            f'projects/{self.name}/featherFiles/genes.feather'
        )

        return geneList

    def EA(self):
        """
        Performs EA using gprofiler2
        """
        subprocess.call(
            ['R/gProfilerEA.R',
             self.name]
        )

    def SR(self, orgdb, ont, method, threshold):
        """
        Performs semantic similarity and parent term reduction.
        """
        f = pd.read_feather(f'projects/{self.name}/data/gProfiler.feather')

        self.GO = f[f['source'] == f'GO:{self.ont}'].reset_index()
        self.GO.to_feather(
            f'projects/{self.name}/featherFiles/GO{self.ont}.feather'
        )

        subprocess.call(
            ['R/RRVGO.R',
             self.name,
             orgdb,
             ont,
             method,
             str(threshold)
             ]
        )

    def check(self, this):
        """
        Pseudo-methods for quick pre-processing
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
name = str(input('Project name: '))
obj = UtilitEA(file, name)

#   automatic directories
if not os.path.exists(f'projects/{name}/featherFiles/'):
    os.makedirs(f'projects/{name}/featherFiles/')
if not os.path.exists(f'projects/{name}/data'):
    os.makedirs(f'projects/{name}/data')

obj.EA()
obj.SR('org.Hs.eg.db', 'BP', 'Rel', 0.7)
