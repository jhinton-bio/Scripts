from Bio import SeqIO
import os
import sys

# Gather variables from command line
file = sys.argv[1]
pos = int(sys.argv[2])
alt = str(sys.argv[3])
gene = sys.argv[4]
present = str(sys.argv[5])

# Dictionary for codon to amino acids
genetic_code = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "AGT": "Ser", "AGC": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "STOP", "TAG": "STOP",
    "CAT": "His", "CAC": "His", "CAA": "Glu", "CAG": "Glu",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys", "TGA": "STOP", "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}


# Read in the sequence
seq = SeqIO.read(file, "fasta")

# Identify codon number
if pos % 3 != 0:
    codon_num = (pos // 3) + 1
else:
    codon_num = pos // 3

# Print ID, Codon #, and Codon to screen
print(seq.id)
print(f"Printing codon",codon_num)
print(seq.seq[((codon_num*3)-3):((codon_num*3))])

# Create Reference Codon
ref = str(seq.seq[((codon_num*3)-3):((codon_num*3))])

# Change to alt codon, 3rd position
if pos % 3 == 0:
    print(genetic_code.get(ref))
    print("------")
    alt_codon = ref[:2] + alt
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))

# Change to alt codon, 1st position
elif pos % 3 == 1:
    print(genetic_code.get(ref))
    print("------")
    alt_codon =  alt + ref[1:3]
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))

# Change to alt codon, 2nd position
elif pos % 3 == 2:
    print(genetic_code.get(ref))
    print("------")
    alt_codon = ref[:1] + alt + ref[2:]
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))

# Identify if Synonymous or Nonsynonymous
if genetic_code.get(alt_codon) == genetic_code.get(ref):
    mtype = "Synonymous"
    print("Synonymous")

elif genetic_code.get(alt_codon) != genetic_code.get(ref):
    mtype = "Non_Synonymous"
    print("Non-Synonymous")

# Gather data into a single line
line = f"{gene}\t{seq.id}\t{ref}\t{genetic_code.get(ref)}\t{alt_codon}\t{genetic_code.get(alt_codon)}\t{mtype}\t{present}\n"

# Make output file
outfile = open("SNP_Variants.tsv", "a")

# If output file is empty, print header
if os.path.getsize("SNP_Variants.tsv") == 0:
        outfile.write("Gene\tAcc. Num.\tReference Codon\tReference Protein\tAlternate Codon\tAlternate Protein\tMutation Type\tKD1\tKD10\tKD11\tKD12\tKD13\tKD14\tKD15\tKD16\tKD17\tKD18\tKD19\tKD2\tKD20\tKD3\tKD4\tKD5\tKD6\tKD7\tKD8\tKD9\n")

# Print variant information
print(line)

# Write to file
outfile.write(line)

# Close output file
outfile.close()
