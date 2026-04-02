# Read in line from file
line=$1

# First column is chromosome info
chrm=$(echo "$line" | cut -f 1 -d "_")

# Second column is position
pos=$(echo "$line" | cut -f 2)

# Fifth column is alternative nucleotide
alt=$(echo "$line" | cut -f 5)

# Columns 6-26 are whether they are present in a sample, may need to change if using different number of samples
present=$(echo "$line" | cut -f 6-26)

# Use BioPython to compile and identify types of mutations
python3 Variants.py cricket_genes/Unique/${chrm}.fa $pos $alt $chrm "$present"


