from ast import Str
import csv

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
            #(alias_map, dest) = some magic to update aliases
            #update_aliases(alias_map, dest)

            if (src, dest) in instr_dict.values:

                #get key from value - todo! find nicer way to do this
                for l, i in instr_dict.items():
                    if i == (src, dest):
                        #add alias in map
                        alias_map[label] = l

            else:
                #add label-instr pair to dictionary
                instr_dict[label] = (src, dest)

    return instr_dict


def __main__():
    