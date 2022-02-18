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
### 1. Initialize UtilitEA() object with gene list
```
name = 'project_name'
file = 'path_to_genes.csv'

GO = UtilitEA(file, name)   # creates project and stores gene list in self.genes
```
### 2. Automatic project directory created
```
if not os.path.exists(f'projects/{name}/featherFiles/'):
    os.makedirs(f'projects/{name}/featherFiles/')
if not os.path.exists(f'projects/{name}/data'):
    os.makedirs(f'projects/{name}/data')
```
### 3. Perform enrichment analysis
```
GO.EA() # automatic EA
GO.SR(GO.name, ont='BP', orgdb='org.Hs.eg.db', method='Rel', threshold=0.7)
```
- Semantic similarity and reduced GO terms are saved as CSVs for visualization
### Dependencies
- PyArrow
- feather (R)

## Future attributes to be added
- Shell compatibility
- ~Semantic similarity analysis~
- ~Semantic reduction~
- Class with visualization methods
- Save states for easy re-loading
- More species
