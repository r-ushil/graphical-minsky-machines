import csv
import graphviz
import sys

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

def graph_gen(instr_dict):

    dot = graphviz.Digraph()

    for (label, (src, dest)) in instr_dict.items():

        dot.node(label, src)

        # todo!() - replace with match-case when upgrading to python 3.10
        if len(dest) == 0:
            print("Adding no edges for HALT")
        elif len(dest) == 1:
            dot.edge(label, dest[0], arrowhead="normal")
        elif len(dest) == 2:
            dot.edge(label, dest[0], arrowhead="normal")
            dot.edge(label, dest[1], arrowhead="diamond") #needs to be double arrow
        else:
            print("ERROR IN CSV INPUT!")
            exit()

    print(dot.source)

    dot.render("output", view=False)     


def main():
    csv_path = sys.argv[1]
    graph_gen(import_program(csv_path))


if __name__ == "__main__":
    main()