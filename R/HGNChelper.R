#!/usr/bin/env Rscript 

args <- commandArgs( trailingOnly=TRUE )

f <- arrow::read_feather(    
        glue::glue('projects/{args[1]}/featherFiles/genes.feather')
    )

# df of updated nomenclature
f <- HGNChelper::checkGeneSymbols(
        f,
            unmapped.as.na=FALSE,
                species='human'
        )

feather::write_feather(
    f,
        glue::glue('projects/{args[1]}/featherFiles/genes.feather')
    )


