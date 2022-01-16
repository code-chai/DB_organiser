import os 
import re

# Place yourself in the directory with your Genbank (GCA) genome data folders.
if os.path.exists("../GenomeDB") == False:
    os.mkdir("../GenomeDB") 

pattern = "(^GCA).*(fna$)"
woutboth = 0 # will count the no. folders without both files we need. 
# denom can just be len(os.listdir())

for item in os.listdir():
    suffix = item.removeprefix("GCA_") 
    print(suffix)
    # .removeprefix() method is available in python 3.9+.
    os.chdir(item)
    print(f"Now in {os.getcwd()}. \n Files: {os.listdir()}")
    the_whey = "./protein.faa"
    destination = f"../../GenomeDB/{suffix}.faa"

    if os.path.exists(the_whey) and (re.search(pattern,file) for file in os.listdir()):
        goodtogo = 1
    else:
        goodtogo = 0
    
    try:  
        if goodtogo == 1:
        # If the dataset includes both a protein.faa file and genome.fna file,
            os.rename(the_whey, destination)
            print(f"Moving {the_whey} to {destination}")
        else:
            woutboth += 1
            # Why do some ncbi genome datasets come with a sequence report and not a sequence anyway?
        os.chdir("..")
    except PermissionError:
        print("su-do you think you are? (Get permission)")
    except OSError:
        print("Not sure about that one, chief. (OSError)")

print(f"GenomeDB: \n {os.listdir('../GenomeDB')}")

if os.path.exists("../RASTthis") == False:
    os.mkdir("../RASTthis") # the dir where we'll run MyRAST on. 

if goodtogo == 1:
    for item in os.listdir():
        suffix = item.removeprefix("GCA_")
        os.chdir(item)
        for file in os.listdir():
            if re.search(pattern, file): 
                os.rename(f"./{file}",f"../../RASTthis/{suffix}.fna")
        os.chdir("..")

print(f"RASTthis: \n {os.listdir('../RASTthis')}")

useful = woutboth/len(os.listdir())
print("In this directory, %f datasets had both files we wanted.") %useful
