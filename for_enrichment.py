from gprofiler import gprofiler
import pandas as pd
import subprocess as sb


def gprofiler_enrich(genes, organism='hsapiens'):

    try:
        if data := genes.iloc[:, 0].to_list():
            return gprofiler(query=data, organism=organism)

    except ValueError: print('genes is NoneType; ensure csv is being read')


def get_sem_sim(name, enrichment, orgdb='org.Hs.eg.db', ont='BP', method='Rel', threshold=0.7):

    try:
        enrichment = enrichment[enrichment['domain'] == ont].reset_index(drop=True, inplace=True)
    except:
        print('no indices detected; check your gprofiler data is loaded properly')

    enrichment.to_feather(f'projects/{name}/featherFiles/gprofiler_{ont}.feather')

    # data is sent to bioconductor for computation
    sb.call(['R/RRVGO.R', name, orgdb,
             ont, method, str(threshold)])

