import sys
import csv

def main():
    if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif sys.argv[1][-4:] != ".csv":
        print("Not a CSV file")
        sys.exit(1)
    try:
        with open(sys.argv[1], 'r') as input:
            sizes = []
            bigger = []
            temp = csv.DictReader(input)
            csv_reader = list(temp)
            for header in temp.fieldnames:
                biggest = len(header)
                bigger.append(True)
                for line in csv_reader:
                    if len(line[header]) > biggest + 1:
                        biggest = len(line[header])
                        bigger[-1] = False
                sizes.append(biggest)

            normal_row = ""
            for i, j in zip(sizes, bigger):
                if j == True:
                    normal_row += ("+" + (i + 4)*"-")
                else:
                    normal_row += ("+" + (i + 3)*"-")
            normal_row += ("+")


            print (normal_row)
            counter = 0
            print("|", end = "")
            for element in temp.fieldnames:
                if bigger[counter]:
                    print(f" {element}" + (sizes[counter] - (len(element)) + 3) * " " + "|", end = "")
                else:
                    print(f" {element}" + (sizes[counter] - (len(element)) + 2) * " " + "|", end = "")
                counter += 1
            print("")
            print(normal_row.replace('-', '='))

            for row in csv_reader:
                counter = 0

                print("|", end = "")
                for element in row:
                    if bigger[counter]:
                        print(f" {row[element]}" + (sizes[counter] - (len(row[element])) + 3) * " " + "|", end = "")
                    else:
                        print(f" {row[element]}" + (sizes[counter] - (len(row[element])) + 2) * " " + "|", end = "")
                    counter += 1
                print("")
                print (normal_row)


    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

main()
