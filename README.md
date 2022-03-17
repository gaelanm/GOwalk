# **UtilitEA for functional enrichment analysis**

## What is this?
A simple tool to enhance the quality of life for researchers studying interesting gene lists. UtilitEA provides easy access to various bioinformatics and visualizations libraries for functional enrichment analysis.

## Why make it?

> Whereas reductionism has yielded splendid results in science, there is an important sense in which it is artificial, and in this sense false. By starting from wholes and moving ‘down’ into parts, one is moving in the opposite direction from the way matters arise.
*Ursula Goodenough*, [*The Sacred Emergence of Nature*](https://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1066&context=bio_facpubs)

***Access to higher dimensional insights:*** machine-readable ontologies are used to identify interesting patterns and associations among your genes.

***UtilitEA provides some cross-compatibility with R's bioconductor:*** This work is heavily influenced by tools such as GoSemSim, RRVGO, and g:Profiler.

## How do I use it?
### 1. Initialize Enrichment() object with a project name and gene list
```
from enrich import *

name = 'project_name'
file = 'path_to_genes.csv'

data = Enrichment(name, file)   # automatically creates project directory
```
### 2. Navigating your genes
Once the object is initialized, you can view various attributes such as:
```
data.name   # project name
data.genes  # straight forward
data.pairwise   # PPIs from STRINGdb
data.network    # networkx representation
data.sub_network    # dict of spectral clusters as cluster:gene sublist pairs

```
### 3. Performing enrichment analysis
```
data.get_gprofiler()    # stores enrichment data from gprofiler as data.enrichment
data.get_semantics()    # returns a similarity matrix (sem_sim) and semantically reduced df (sem_red)
data.sem_sim
data.sem_red
```
### 4. Visualizing the data
In progress

### Dependencies

## Future attributes to be added
- Notebook format
- Shell compatibility
- ~Semantic similarity analysis~
- ~Semantic reduction~
- Class with visualization methods
- Save states for easy re-loading
- More species
