import csv

def update_aliases(alias_map, dest):
    #replace all redundant labels
    for obj in dest:
        if obj in alias_map:
            obj = alias_map[obj]

    return (alias_map, dest)

#function to import register machine csv
def import_program(filename):

    #key: label, value: (source, [dest1, dest2])
    instr_dict = {}

    #key: duplicate label, value: label to use 
    alias_map = {}

    #open csv
    with open(filename, 'r') as prog:
        reader = csv.reader(prog)

        for row in reader:

            label = row[0] #L0
            src = row[1] #R1
            dest = row[2:] #[L1, L2] or [HALT], or [L4]

            #replace duplicate labels
            (alias_map, dest) = update_aliases(alias_map, dest)

            pair = (src, dest)

            #find key matching pair
            val = [key for key, instr in instr_dict.items() if instr == pair]

            if val:
                #if exists - add to alias map
                alias_map[label] = val[0]
            else:
                #add src-dest pair to dictionary
                instr_dict[label] = pair

    return instr_dict



def main():
    print(import_program("example.csv"))

if __name__ == "__main__":
    main()