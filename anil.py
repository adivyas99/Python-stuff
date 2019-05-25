import pandas as pd
filenames = ["W1.xlsx", "W2.xlsx", "W3.xlsx"]  

# enter any number of file names in quotes to join the files
# and yes the names must be seprated by commas as shown

print("Number of Files- ", len(filenames))
for f in filenames:
    df = pd.read_excel(f) 
    df['Name'] = str(f)
    df.to_excel(f, header = True)


combined_csv = pd.concat( pd.read_excel(i) for i in filenames)
combined_csv.to_excel("final.xlsx", header=False, index=False)


'''
cd desktop   // go to dektop
cd anil     // in desktop there is a folder

python anil.py  // running the python file to combine
'''

