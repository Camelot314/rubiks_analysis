with open("extracted_tsv/WCA_export_Results.tsv") as myfile:
    head = [next(myfile) for x in range(50)]

for line in head:
    print(line)