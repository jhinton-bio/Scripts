from Bio import SeqIO
import os
import sys


file = sys.argv[1]
pos = int(sys.argv[2])
alt = str(sys.argv[3])
gene = sys.argv[4]
present = str(sys.argv[5])

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



seq = SeqIO.read(file, "fasta")

#print(seq)

if pos % 3 != 0:
    codon_num = (pos // 3) + 1

else:
    codon_num = pos // 3

print(seq.id)
print(f"Printing codon",codon_num)
print(seq.seq[((codon_num*3)-3):((codon_num*3))])

ref = str(seq.seq[((codon_num*3)-3):((codon_num*3))])

if pos % 3 == 0:
    print(genetic_code.get(ref))
    print("------")
    alt_codon = ref[:2] + alt
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))

elif pos % 3 == 1:
    print(genetic_code.get(ref))
    print("------")
    alt_codon =  alt + ref[1:3]
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))

elif pos % 3 == 2:
    print(genetic_code.get(ref))
    print("------")
    alt_codon = ref[:1] + alt + ref[2:]
    #print(alt)
    print(alt_codon)
    print(genetic_code.get(alt_codon))


if genetic_code.get(alt_codon) == genetic_code.get(ref):
    mtype = "Synonymous"
    print("Synonymous")

elif genetic_code.get(alt_codon) != genetic_code.get(ref):
    mtype = "Non_Synonymous"
    print("Non-Synonymous")

line = f"{gene}\t{seq.id}\t{ref}\t{genetic_code.get(ref)}\t{alt_codon}\t{genetic_code.get(alt_codon)}\t{mtype}\t{present}\n"

outfile = open("SNP_Variants.tsv", "a")
if os.path.getsize("SNP_Variants.tsv") == 0:
        outfile.write("Gene\tAcc. Num.\tReference Codon\tReference Protein\tAlternate Codon\tAlternate Protein\tMutation Type\tKD1\tKD10\tKD11\tKD12\tKD13\tKD14\tKD15\tKD16\tKD17\tKD18\tKD19\tKD2\tKD20\tKD3\tKD4\tKD5\tKD6\tKD7\tKD8\tKD9\n")

print(line)
outfile.write(line)

outfile.close()
