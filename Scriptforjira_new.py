import csv
import sys

sys.tracebacklimit = 0

# SpiraPlan export parser
if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError(f'*** Invalid Syntax ***\nUsage:\n\t\t{sys.argv[0]} <input-csv> <output-csv>')

    inputCSV = sys.argv[1]
    outputCSV = sys.argv[2]

    with open(inputCSV, 'r') as fh:
        rd = csv.DictReader(fh, delimiter=',')
        mergedRows = []
        i = 0
        for row in rd:
            if i == 0:
                header = list(row.keys())

            if row[header[0]] != '':
                print(f"... processing: {header[0]}{row[header[0]]}")
                for key, val in row.items():
                    row[key] = str(row[key]).replace(',', ';')
                mergedRows.append(row)
                i += 1
            else:
                for key, val in row.items():
                    if val != '':
                        mergedRows[i-1][key] = str(mergedRows[i-1][key]) + '"___"'
                        mergedRows[i-1][key] = str(mergedRows[i-1][key]) + str(val).replace(',', ';')
        print(f"... processed {i} issues")

        # write results to file
        fw = open(outputCSV, 'w')
        writer = csv.DictWriter(fw, header)
        for row in mergedRows:
            writer.writerow(row)
        fw.close()
