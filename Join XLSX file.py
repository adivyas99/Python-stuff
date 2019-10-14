# importing the libraries
import pandas as pd

# Taking file names
filenames = ["W1.xlsx", "W2.xlsx", "W3.xlsx"]  

# enter any number of file names in quotes to join the files
# and yes the names must be seprated by commas as shown

## Printing the files-
print("Number of Files- ", len(filenames))

## Taking all files through a loop
for f in filenames:
    df = pd.read_excel(f) 
    df['Name'] = str(f)
    df.to_excel(f, header = True)

#combining the file
combined_csv = pd.concat( pd.read_excel(i) for i in filenames)

## making an excel file
combined_csv.to_excel("final.xlsx", header=False, index=False)


'''
cd desktop   // go to dektop
cd anil     // in desktop there is a folder

python anil.py  // running the python file to combine
'''

