# **UtilitEA for functional enrichment analysis**

## What is this?
A simple tool to enhance the quality of life for researchers studying interesting gene lists. UtilitEA provides easy access to various bioinformatics and visualizations libraries for functional enrichment analysis.

## Why make it?

> Whereas reductionism has yielded splendid results in science, there is an important sense in which it is artificial, and in this sense false. By starting from wholes and moving ‘down’ into parts, one is moving in the opposite direction from the way matters arise.
*Ursula Goodenough*, [*The Sacred Emergence of Nature*](https://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1066&context=bio_facpubs)

***Access to higher dimensional insights:*** machine-readable ontologies are used to identify interesting patterns and associations among your genes.

***UtilitEA provides some cross-compatibility with R's bioconductor:*** This work is heavily influenced by tools such as GoSemSim, RRVGO, and g:Profiler.

***I write the code so you don't have to.***

## How do I use it?
### 1. Initialize Genes() object
```
genes = Genes('project name')
```
### 2. Get genes
```
genes.setGenes('path/to/genes.csv')
```
### 3. Analyze
Currently, this software provides:
```
Genes().getHGNC()     # update self.genes with approved gene nomenclature
Genes().getEA()       # performs and stores EA in self.enrich
Genes().setEA()       # read stored EA CSV into self.enrich 
```
### Dependencies
- PyArrow
- feather (R)

## Future attributes to be added
- Shell compatibility
- Semantic similarity analysis
- Semantic reduction
- Class with visualization methods
- Save states for easy re-loading
- More species
