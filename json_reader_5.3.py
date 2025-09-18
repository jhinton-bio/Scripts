import json
import os
import sys

#Finds the index based of input of accession number
def findIndex(name):
    i = 0
    found = False
    for n in y:
        if y[i]["accession"] == anum:
            found = True
            break
        else:
            i += 1
    if found == False:
        i = -1

    return i

filename = sys.argv[1]

#Opens json file
f = open(filename, "r")
x = f.read()

#Makes jsonfile into large nested list/dictionary
y = json.loads(x)

if isinstance(y, list):
    #File has multiple accession numbers (needs an index)
    print("Multiple Accession Numbers in File, please input desired number")

    #Accession number input
    anum = sys.argv[2]


    #Run above function to find index of correct number
    index = findIndex(anum)

    #Exits if index not found
    if index == -1:
        print("Accession not found")
        exit()

    #Print info
    if "biosample" in y[index]["assemblyInfo"]:
        print("Organism Name: ", y[index]["assemblyInfo"]["biosample"]["description"]["organism"]["organismName"])
    else:
        print("Org. Name")
    print("Accession Number: ", y[index]["accession"])
    print("Assembly Level: ", y[index]["assemblyInfo"]["assemblyLevel"])
    print("Bioproject Accession: ", y[index]["assemblyInfo"]["bioprojectAccession"])

    if "annotationInfo" in y[index]:
        print("Protein Coding Gene Count: ", y[index]["annotationInfo"]["stats"]["geneCounts"]["proteinCoding"])
        print("Gene Count: ", y[index]["annotationInfo"]["stats"]["geneCounts"]["total"])
    else:
        print("Missing Annotation Info")

    print()
    print("Assembly Stats")
    print("Contig L50: ", y[index]["assemblyStats"]["contigL50"])
    print("Contig N50: ", y[index]["assemblyStats"]["contigN50"])
    print("GC-Count: ", y[index]["assemblyStats"]["gcCount"])
    print("GC%: ", y[index]["assemblyStats"]["gcPercent"])
    print("Num. of Contigs: ", y[index]["assemblyStats"]["numberOfContigs"])
    print("Total Sequence Length: ", y[index]["assemblyStats"]["totalSequenceLength"])

    if "annotationInfo" in y[index]:
        if "busco" in y[index]["annotationInfo"]:
            print()
            print("Busco Stats")
            print("Complete %: ", y[index]["annotationInfo"]["busco"]["complete"])
            print("Duplicated %: ", y[index]["annotationInfo"]["busco"]["duplicated"])
            print("Fragmented %: ", y[index]["annotationInfo"]["busco"]["fragmented"])
            print("Missing %: ", y[index]["annotationInfo"]["busco"]["missing"])
            print("Single Copy %: ", y[index]["annotationInfo"]["busco"]["singleCopy"])
        else:
            print("Missing Busco Stats")
    else:
        print("Missing Annotation Info")
        
    #Create list for easier pasting to tsv
    infoList = []

    #Add info to list

    if "biosample" in y[index]["assemblyInfo"]:
        infoList.append(str(y[index]["assemblyInfo"]["biosample"]["description"]["organism"]["organismName"]))
    else:
        infoList.append("NA")
        
    infoList.append(str(y[index]["accession"]))
    infoList.append(str(y[index]["assemblyInfo"]["assemblyLevel"]))
    infoList.append(str(y[index]["assemblyInfo"]["bioprojectAccession"]))

    if "annotationInfo" in y[index]:
        infoList.append(str(y[index]["annotationInfo"]["stats"]["geneCounts"]["proteinCoding"]))
        infoList.append(str(y[index]["annotationInfo"]["stats"]["geneCounts"]["total"]))
    else:
        infoList.append("NA")
        infoList.append("NA")

    infoList.append(str(y[index]["assemblyStats"]["contigL50"]))
    infoList.append(str(y[index]["assemblyStats"]["contigN50"]))
    infoList.append(str(y[index]["assemblyStats"]["gcCount"]))
    infoList.append(str(y[index]["assemblyStats"]["gcPercent"]))
    infoList.append(str(y[index]["assemblyStats"]["numberOfContigs"]))
    infoList.append(str(y[index]["assemblyStats"]["totalSequenceLength"]))

    if "annotationInfo" in y[index]:
        if "busco" in y[index]["annotationInfo"]:
            infoList.append(str(y[index]["annotationInfo"]["busco"]["complete"]))
            infoList.append(str(y[index]["annotationInfo"]["busco"]["duplicated"]))
            infoList.append(str(y[index]["annotationInfo"]["busco"]["fragmented"]))
            infoList.append(str(y[index]["annotationInfo"]["busco"]["missing"]))
            infoList.append(str(y[index]["annotationInfo"]["busco"]["singleCopy"]))
        else:
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
    else:
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")
        
else:
    #For one accession number (no index needed)

    if "biosample" in y["assemblyInfo"]:
        print("Organism Name: ", y["assemblyInfo"]["biosample"]["description"]["organism"]["organismName"])
    else:
        print("Org. Name")
    print("Accession Number: ", y["accession"])
    print("Assembly Level: ", y["assemblyInfo"]["assemblyLevel"])
    print("Bioproject Accession: ", y["assemblyInfo"]["bioprojectAccession"])
    
    if "annotationInfo" in y:
        print("Protein Coding Gene Count: ", y["annotationInfo"]["stats"]["geneCounts"]["proteinCoding"])
        print("Gene Count: ", y["annotationInfo"]["stats"]["geneCounts"]["total"])
    else:
        print("Missing Annotation Info")


    print()
    print("Assembly Stats")
    print("Contig L50: ", y["assemblyStats"]["contigL50"])
    print("Contig N50: ", y["assemblyStats"]["contigN50"])
    print("GC-Count: ", y["assemblyStats"]["gcCount"])
    print("GC%: ", y["assemblyStats"]["gcPercent"])
    print("Num. of Contigs: ", y["assemblyStats"]["numberOfContigs"])
    print("Total Sequence Length: ", y["assemblyStats"]["totalSequenceLength"])

    if "annotationInfo" in y:
        if "busco" in y["annotationInfo"]:
            print()
            print("Busco Stats")
            print("Complete %: ", y["annotationInfo"]["busco"]["complete"])
            print("Duplicated %: ", y["annotationInfo"]["busco"]["duplicated"])
            print("Fragmented %: ", y["annotationInfo"]["busco"]["fragmented"])
            print("Missing %: ", y["annotationInfo"]["busco"]["missing"])
            print("Single Copy %: ", y["annotationInfo"]["busco"]["singleCopy"])
        else:
            print("Missing Busco Stats")
    else:
        print("Missing Annotation Info")

    infoList = []

    if "biosample" in y["assemblyInfo"]:
        infoList.append(str(y["assemblyInfo"]["biosample"]["description"]["organism"]["organismName"]))
    else:
        infoList.append("NA")
    
    infoList.append(str(y["accession"]))
    infoList.append(str(y["assemblyInfo"]["assemblyLevel"]))
    infoList.append(str(y["assemblyInfo"]["bioprojectAccession"]))

    if "annotationInfo" in y:
        infoList.append(str(y["annotationInfo"]["stats"]["geneCounts"]["proteinCoding"]))
        infoList.append(str(y["annotationInfo"]["stats"]["geneCounts"]["total"]))
    else:
        infoList.append("NA")
        infoList.append("NA")

    infoList.append(str(y["assemblyStats"]["contigL50"]))
    infoList.append(str(y["assemblyStats"]["contigN50"]))
    infoList.append(str(y["assemblyStats"]["gcCount"]))
    infoList.append(str(y["assemblyStats"]["gcPercent"]))
    infoList.append(str(y["assemblyStats"]["numberOfContigs"]))
    infoList.append(str(y["assemblyStats"]["totalSequenceLength"]))

    if "annotationInfo" in y:
        if "busco" in y["annotationInfo"]:
            infoList.append(str(y["annotationInfo"]["busco"]["complete"]))
            infoList.append(str(y["annotationInfo"]["busco"]["duplicated"]))
            infoList.append(str(y["annotationInfo"]["busco"]["fragmented"]))
            infoList.append(str(y["annotationInfo"]["busco"]["missing"]))
            infoList.append(str(y["annotationInfo"]["busco"]["singleCopy"]))
        else:
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
            infoList.append("NA")
    else:
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")
        infoList.append("NA")


#Format to tsv
line = "NA\t"
for i in infoList:
    line += i
    line += "\t"

line += "\n"

#Write to tsv file if needed
#append = input("Append to metadata file? (y/n)")

#temporary yes
append = "y"

if append == "y":
    outfile = open("metadata.tsv", "a")

    if os.path.getsize("metadata.tsv") == 0:
        outfile.write("Common Name\tSci. Name\tAcc. Num.\tAssembly\tBioproject Acc.\tProtein Coding Gene Count\tTotal Gene Count\tContig L50\tContig N50\tGC-Count\tGC%\tContig Num.\tTotal Seq. Length\tComplete%\tDuplicated%\tFragmented%\tMissing%\tSingleCopy%\n")
    
    outfile.write(line)

    outfile.close()

f.close()

