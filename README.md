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
geneset = UtilitEA('test.csv')
geneset.name = 'test'
```
### 2. Automatic project directory created
```
if not os.path.exists(f'projects/{proj}/featherFiles/'):
    os.makedirs(f'projects/{proj}/featherFiles/')
if not os.path.exists(f'projects/{proj}/data'):
    os.makedirs(f'projects/{proj}/data')
```
### 3. Analyze
```
geneset.getEA(geneset.name)
geneset.getGO(geneset.name, ont='BP', orgdb='org.Hs.eg.db', method='Rel', threshold=0.7)
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
