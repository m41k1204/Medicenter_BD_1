import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = []
            for cell in row:
                # Remove commas from the cell
                clean_cell = cell.replace(',', '')
                new_row.append(clean_cell)
            writer.writerow(new_row)

# Example usage
input_csv = 'insumos_medicos_mil.csv'
output_csv = 'prueba.csv'
clean_csv(input_csv, output_csv)
