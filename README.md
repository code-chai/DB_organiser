# Hello! 
`DB_organiser` is a script that helps with the database preparation stage of the EvoMining workflow. 
It takes fna and faa files downloaded from NCBI Genbank accessions, standardises their naming and moves them about, the `.faa` files straight to the GenomeDB folder, and the `.fna` files to an intermediate folder that MyRAST can be run on to provide standard annotations.

NB: As I am currently learning how to use EvoMining, I may have certain misconceptions about the input for the GenomeDB: using genome accessions instead of contigs/groups of contigs specified in the paper. If whole genome accessions cannot be used, I will fork and rework `DB_organiser`. 

> Evomining: https://github.com/nselem/evomining
> Original Paper: Cruz-Morales, P., Kopp, J.F., Martínez-Guerrero, C., Yáñez-Guerra, L.A., Selem-Mojica, N., Ramos-Aboites, H., Feldmann, J. and Barona-Gómez, F., 2016. Phylogenomic Analysis of Natural Products Biosynthetic Gene Clusters Allows Discovery of Arseno-Organic Metabolites in Model Streptomycetes. *Genome Biology and Evolution* [Online], 8(6), pp.1906–1916. Available from: https://doi.org/10.1093/gbe/evw125
