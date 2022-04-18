# Graphical Minsky Machines

Made to support the learning of the 50003 Models of Computation Course at Imperial College London: https://www.imperial.ac.uk/computing/current-students/courses/50003/

## Usage:
  - make setup: installs dependendies
  - make run csv=CSVFILE: runs the program on the specfied CSV file, and opens the resulting PDF in the default browser
  - make clean: removes files outputted from the program


## CSV File Setup:

The repository contains an example file on how an input should be formatted before being passed into the program. The headings are as follows, where DEST_LABEL_1 and DEST_LABEL_2 are optional:

<code>LABEL_NUMBER, REGISTER, DEST_LABEL_1, DEST_LABEL_2</code>

The information about add or subtract instructions is ignored, and implicitly inferred in the program.


## Output File:

The result of the program is stored as a PDF in the program directory and automatically opened. The diagram is read as follows:
  - Circle: Register
  - Triangle Arrow: Add Instruction
  - Diamond Arrow: Subtract Instruction

![image](https://user-images.githubusercontent.com/80212345/163876197-93697235-40e5-4129-902f-49fc8071c1cb.png)

