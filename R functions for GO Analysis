make_GO <- function(x, geneNames){
  genes <- read.table(x, header = F)
  genes <- genes$V1
  gl <- factor(as.integer(geneNames %in% genes))
  names(gl) <- geneNames
  return(gl)
}

capFirst <- function(s) {
    paste(toupper(substring(s, 1, 1)), substring(s, 2), sep = "")
}

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

termReducer <- function(allRes){
  allRes$classicFisher <- gsub("<", "", allRes$classicFisher)
  allRes$classicFisher <- as.numeric(allRes$classicFisher)
  sig_Go<- subset(allRes, classicFisher < 0.05)
  simMatrix<- calculateSimMatrix(sig_Go$GO.ID, orgdb = "org.Ag.eg.db", ont = "BP", method = "Rel")
  scores <- setNames(-log10(sig_Go$classicFisher), sig_Go$GO.ID)
  reducedTerms <- reduceSimMatrix(simMatrix, scores, threshold = 0.95, orgdb = "org.Ag.eg.db")
}
