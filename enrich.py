import pandas as pd
from for_genes import *
from for_enrichment import *
import networkx as nx
from sklearn.cluster import SpectralClustering
from gprofiler import gprofiler
import os


class GeneList:
    """
    Object allows a user to perform various data contextualizations to a csv of genes

    genes df: list of genes
    pairwise df: gene interactions using STRINGdb API
    network Networkx obj: nodes, edges, weights
    sub_networks dict: keys are cluster labels, values are subsets of genes
    """

    def __init__(self, name, f='test.csv'):
        self.name = name

        if not os.path.exists(f'projects/{name}/featherFiles/'):
            os.makedirs(f'projects/{name}/featherFiles/')

        self.genes = pd.read_csv(f)
        self.pairwise = stringdb_pairwise(self.genes)
        self.network = self.get_network()
        self.sub_networks = self.get_subnet()

    def get_network(self):

        return nx.from_pandas_edgelist(self.pairwise, source='preferredName_A',
                                       target='preferredName_B', edge_attr='score')

    def get_subnet(self, n_clusters=10, affinity='precomputed', assign_labels='discretize'):
        """
        Discretizes gene list into n sub-networks using spectral clustering

        n_clusters int: # of discrete sub networks
        """

        # create instance for clustering
        sc = SpectralClustering(n_clusters=n_clusters, affinity=affinity,
                                assign_labels=assign_labels)

        # pair-wise weighted adjacency matrix
        adjacency = neighbourhood_adjacency(self.pairwise)

        clusters = pd.Series(sc.fit_predict(adjacency), index=adjacency.index)

        # dict with clusters k and gene list subset values
        res = dict()
        for cluster, gene in zip(clusters, clusters.index):
            res.setdefault(str(cluster), [])
            res[str(cluster)].append(gene)

        return res


class Enrichment(GeneList):
    """
    Performs various analyses on GeneList objects

    enrichment df: functional enrichment data using gprofiler API
    sem_sim df: semantic similarity matrix
    sem_red df: semantic reduction of enrichment

    """
    def __init__(self, name, f='test.csv'):
        GeneList.__init__(self, name, f)
        self.enrichment = None
        self.sem_sim = None
        self.sem_red = None

    def get_gprofiler(self, organism='hsapiens'):
        try:
            if data := self.genes.iloc[:, 0].to_list():
                self.enrichment = gprofiler(query=data, organism=organism)

        except ValueError:
            print('genes variable is empty; ensure you are reading the proper file')

    def get_semantics(self, orgdb='org.Hs.eg.db', ont='BP', method='Rel', threshold=0.7):
        try:
            self.enrichment = self.enrichment[
                self.enrichment['domain'] == ont
            ].reset_index(drop=True, inplace=True)

        except ValueError:
            print('no indices detected; check your gprofiler data is loaded properly')

        self.enrichment.to_feather(f'projects/{self.name}/featherFiles/gprofiler_{ont}.feather')

        # data is sent to bioconductor for computation
        sb.call(['R/RRVGO.R', self.name, orgdb,
                 ont, method, str(threshold)])

        self.sem_sim = pd.read_csv(
            f'projects/{self.name}/featherFiles/simMatrix{ont}_th{str(threshold * 100)}.feather')

        self.sem_red = pd.read_csv(
            f'projects/{self.name}/featherFiles/simReduced{ont}_th{str(threshold * 100)}.feather')






