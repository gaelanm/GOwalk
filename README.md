# **Nexus-EA**
A simple tool to enhance the quality of life for researchers studying interesting gene lists. 

## What?
Nexus-EA is a container that provides easy access to various bioinformatics tools and visualizations for functional enrichment analysis in a single session.

## Why?

> Whereas reductionism has yielded splendid results in science, there is an important sense in which it is artificial, and in this sense false. By starting from wholes and moving ‘down’ into parts, one is moving in the opposite direction from the way matters arise.
*Ursula Goodenough*, [*The Sacred Emergence of Nature*](https://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1066&context=bio_facpubs)

Experimental models of gene products typically assume some degree of independence from all other gene products. This confounds our interpretation of experimental data by not considering a fundamental attribute of genes: membership to functionally related sets that orchestrate complex biological behaviour. In essence, phenotypes are (mostly) not the product of a single gene but instead **emerge from the complex interactions between evolutionarily determined set members**.

Functional enrichment analysis is a powerful computational tool that leverages our entire molecular knowledge to provide important insight into the system-level implication of an experimentally-derived gene list. This project is to provide an easy interface for researchers to explore thier data without having to manage their inputs, outputs, or organization.

***Nexus-EA provides some cross-compatibility with R's bioconductor***
This work is heavily influenced by tools such as GoSemSim, RRVGO, and g:Profiler.

## How?
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
