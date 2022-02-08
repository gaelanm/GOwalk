#   Script by Gaelan Melanson
#
#   Creates a Genes() object that holds a
#   list of interesting genes as well as methods
#   for functional enrichment analysis
#

import pandas as pd
import subprocess
import os
import utl

class Genes:
    def __init__(self, name):
        """
        :param name: user-defined project name
        :param self.genes: holds CSV of genes
        :param self.enrich: holds EA performed using gprofiler2 in R
        """
        self.name = name
        self.genes = None
        self.enrich = None

    def setGenes(self, path):
        """
        Reads user gene list into a Genes() object
        :param path: full path to csv
        :return: self.gene attribute
        """
        self.genes = utl.Genes(path)

        self.genes.to_feather(
            f'projects/{self.name}/featherFiles/genes.feather'
        )

    def getHGNC(self):
        """
        Data cleaning to remove erroneous gene names
        :return: updates self.gene with HGNC-approved symbols
        """
        utl.HGNC(
            self.genes,
                self.name
        )

        self.genes = pd.read_feather(
            f'projects/{self.name}/featherFiles/genes.feather'
        )

    def getEA(self):
        """
        Performs EA using gprofiler2 in R
        :return: enrichment analysis of self.genes
        """

        subprocess.call(
            ['R/clusterProfiler.R',
                self.name]
        )

        self.enrich = pd.read_csv(
            f'projects/{self.name}/data/gProfiler.csv'
        )

    def setEA(self, path):
        """
        Used to read previous EA file into self.enrich
        :param path: full path to csv
        :return: read EA into self.enrich
        """
        self.enrich = pd.read_csv(path, header=True)


file = str(input('Full path to gene list: '))
name = str(input('Project name: '))
z = Genes(name)

#   create parent and children directories
if not os.path.exists(f'projects/{name}/featherFiles/'):
    os.makedirs(f'projects/{name}/featherFiles/')
if not os.path.exists(f'projects/{name}/data'):
    os.makedirs(f'projects/{name}/data')





