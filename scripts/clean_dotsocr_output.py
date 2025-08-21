import sys, json, re
from pathlib import Path




def cleanJsonfile(jsonfile):
    with open(jsonfile) as fh:
        data = json.load(fh)
        #print(data)
        txt = data[0]["text"]

    txt = re.sub("[¹²³⁴⁵⁶⁷]", "", txt)

    txt = re.sub("[”“]", '"', txt)
        
    txt = re.sub(r"\[[^]]+\]", "", txt)

    txt = re.sub(r"\*\*", "", txt)

    txt = re.sub(r"\s+", " ", txt)

    txt = re.sub(r"([.?!]) ", r"\1\n", txt)


    
    return txt

if __name__ == "__main__":
    jsonfiles = sys.argv[1:]
    for jsonfile in jsonfiles:

        print(jsonfile)
        
        txt = cleanJsonfile(jsonfile)

        textfile = Path(jsonfile).with_suffix(".txt")
        with open(textfile, "w") as fh:
            fh.write(txt)


