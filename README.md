# TGRN510_Assignment4
In this week's assignment, I created a program `ensg2hugo.py` that takes comma-delimited file as an argument and column number as an input and print a file with Ensembl gene name has substituted to HUGO gene name.
## Installation & Usage
### Clone
First, you need to use `git clone` to clone this repository to your local machine: 
`$ git clone https://github.com/kayleyw/TRGN510_Assignment4.git`
### Download GTF annotation file
This program builds a dictionary from the `Homo_sapiens.GRCh37.75.gtf` release. Therefore, you need to download the files to the path of where the program is located. 

`$ curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz --output [path_of_where_program_located]/Homo_sapiens.GRCh37.75.gtf.gz`

### Usage 
In the repository you downloaded, there is a `.csv` for unit test. You can try it out to see if the program is working on your local machine. 

`$ ./ensg2hugo.py -f 2 expres.anal.csv`

In here we specify the program to substitute Ensembl gene names in column 2 of `expres.anal.csv` to HUGO gene name with the `-f 2` option. You can change the column number to work with your csv file with this option. If column number is not specify, the first column will be used. 

## Known issues
- Due to the GTF annotation release uses in this program, some of the Ensembl gene names may not be present in the dictionary. For genes that the program does not find a match for, `unknown` will be put in the gene name column instead.

## Contact
Kayley
manyeewo@usc.edu

