import os 
import re

# Place yourself in the directory with your Genbank (GCA) genome data folders.
genfile_regex = "(^GCA).*(fna$)"
woutboth = 0 # will count the no. folders without both files we need. 

def DB_organiser(pattern):
    global woutboth 
    if os.path.exists("../GenomeDB") == False:
        os.mkdir("../GenomeDB") 
    if os.path.exists("../RASTthis") == False:
        os.mkdir("../RASTthis") # the dir where we'll run MyRAST on. 

    for item in os.listdir():
        if item[0:3] == "GCA":
            suffix = item.removeprefix("GCA_") 
            # .removeprefix() method is available in python 3.9+.
            os.chdir(item)
            print(f"Now in {os.getcwd()}. \n Files: {os.listdir()}")

            the_whey = "./protein.faa"
            whey_dest = f"../../GenomeDB/{suffix}.faa"
            faa_present = os.path.exists(the_whey)
            for file in os.listdir():
                if re.search(pattern, file):
                    fna_present = True
                    the_jean = f"./{file}"
            jean_dest = f"../../RASTthis/{suffix}.fna"

            if faa_present and fna_present:
            # If the dataset includes both a protein.faa file and genome.fna file,
                os.rename(the_whey, whey_dest)
                print(f"Moving {the_whey} to {whey_dest}")
                os.rename(the_jean, jean_dest)
                print(f"Moving {the_jean} to {jean_dest}")
            else:
                woutboth += 1
            os.chdir("..")

    print(f"GenomeDB: \n {os.listdir('../GenomeDB')}") 
    print(f"RASTthis: \n {os.listdir('../RASTthis')}")
    

DB_organiser(genfile_regex)

useful = (round(1-(woutboth/len(os.listdir())),2))*100
print(f"In this directory, {useful}% of the datasets had both files we wanted.")

