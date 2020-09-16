mport sys
import fileinput
import csv
import pandas as pd
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("-f","--fnumber", default='1')
args = parser.parse_args()


output={}
for each_line_of_text in fileinput.input('Homo_sapiens.GRCh37.75.gtf'):
       
    if len(re.findall('#',each_line_of_text))>0:
        continue
        
    line = each_line_of_text.split("\t")
    s = next(csv.reader([line[8]], delimiter=' '))

    temp = {s[i]:s[i+1] for i in range(0,len(s),2)}
    temp_id = temp['gene_id'].strip(';')
    temp_name = temp['gene_name'].strip(';')
    output[temp_id] = temp_name

fileinput.close()

expression_file = args.file
file_in = pd.read_csv(expression_file)

def checking(str_in):
    try:
        return output[str(str_in).split('.')[0]]
    except:
        return 'unknown'

f_number = int(args.fnumber)
file_in.iloc[:,f_number-1] = file_in.iloc[:,f_number-1].apply(lambda x: checking(x))    

print(file_in)
