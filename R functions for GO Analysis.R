library(topGO)
library(org.Ag.eg.db)
library(rrvgo)

# Reads in the mapping of the genes to the GO TERMS, used in the GO_Analysis function as g2go
geneID2GO <- readMappings("FILE")

# Labels the specified genes in file "x" from the gene universe "geneNames" and stores them in a factor
make_GO <- function(x, geneNames){
  genes <- read.table(x, header = F)
  genes <- genes$V1
  gl <- factor(as.integer(geneNames %in% genes))
  names(gl) <- geneNames
  return(gl)
}

#QOL function to quickly edit names in rrvgo
capFirst <- function(s) {
    paste(toupper(substring(s, 1, 1)), substring(s, 2), sep = "")
}

#Function to run GO analysis using the perviously generated factor and the GO term mapping

GO_Analysis <- function(genes, g2go){
  GO_data <- new("topGOdata", 
                 ontology = "BP", 
                 allGenes = genes,
                 annot = annFUN.gene2GO,
                 gene2GO = g2go,
                 nodeSize = 5)
  
  allGO = usedGO(object = GO_data)
  result_ks.elim <- runTest(GO_data, statistic = "ks", algorithm = "elim")
  result_ks <- runTest(GO_data, statistic = "ks", algorithm = "classic")
  result_fisher <- runTest(GO_data, statistic = "fisher", algorithm = "classic")
  
  allRes <- GenTable(GO_data,
                             classicFisher = result_fisher, 
                             classicKS = result_ks, 
                             elimKS = result_ks.elim,
                             orderBy = "classicFisher",
                             ranksOf = "classicFisher",
                             topNodes = 3500)
  return(allRes)
}

# Reduces terms from the GO Analysis so that they can be made into treemaps
termReducer <- function(allRes){
  allRes$classicFisher <- gsub("<", "", allRes$classicFisher)
  allRes$classicFisher <- as.numeric(allRes$classicFisher)
  sig_Go<- subset(allRes, classicFisher < 0.05)
  simMatrix<- calculateSimMatrix(sig_Go$GO.ID, orgdb = "org.Ag.eg.db", ont = "BP", method = "Rel")
  scores <- setNames(-log10(sig_Go$classicFisher), sig_Go$GO.ID)
  reducedTerms <- reduceSimMatrix(simMatrix, scores, threshold = 0.95, orgdb = "org.Ag.eg.db")
}
