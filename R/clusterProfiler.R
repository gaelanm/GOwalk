#!/usr/bin/env Rscript 

args <- commandArgs( trailingOnly=TRUE )

f <- arrow::read_feather(
        glue::glue('projects/{args[1]}/featherFiles/genes.feather')
        ) 

# https://biit.cs.ut.ee/gprofiler/page/docs
res <- gprofiler2::gost(
    as.list(f),
        correction_method='gSCS',
            user_threshold=0.05,
                organism='hsapiens',
                    domain_scope='annotated')

# added to avoid parent as list error
res <- apply(res$result,
             2,
             as.character
             )

# saved as csv for long-term storage of results
write.csv(res, glue::glue('projects/{args[1]}/data/gProfiler.csv'))








