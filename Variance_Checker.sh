line=$1
chrm=$(echo "$line" | cut -f 1 -d "_")
pos=$(echo "$line" | cut -f 2)
alt=$(echo "$line" | cut -f 5)
present=$(echo "$line" | cut -f 6-26)

python3 Variants.py cricket_genes/Unique/${chrm}.fa $pos $alt $chrm "$present"


