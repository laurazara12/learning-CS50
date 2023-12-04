import csv
import sys

def process_csv(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            rows = []
            for row in reader:
                name = row[0].strip('"')
                last_name, first_name = name.split(', ', 1)
                house = row[1]
                rows.append([first_name, last_name, house])

        with open(output_file, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(['first', 'last', 'house'])
            writer.writerows(rows)

        print(f"Processing completed. Output written to {output_file}")

    except FileNotFoundError:
        print(f"Could not read {input_file}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Invalid number of command-line arguments")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.csv') or not output_file.endswith('.csv'):
        print("Please provide CSV files as input and output")
        sys.exit(1)

    process_csv(input_file, output_file)

if __name__ == "__main__":
    main()
