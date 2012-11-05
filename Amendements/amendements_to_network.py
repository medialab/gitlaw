import pprint
import re
network = [
["Source", "Target"],
]
debug=False

def integer_marking(string):
    try:
        int(string)
        return "integer"
    except :
        return string
nb_line_processed=0
nd_line=0
with open("description_amendement.txt") as amendements_original:
    with open("amendement_first_line.txt","w") as amendent_first_line_only:
        for line in amendements_original.readlines():
            nd_line+=1
            # get article title 
            if re.match("Article [0-9]+\t",line) :
                article,amendement=line.split("\t")
            else :
                article,amendement=(None,line,)
            # ponctuations
            amendement=amendement.lower().replace("\n", "").replace(","," ,").replace("."," .").replace(":"," :")
            amendement=re.sub(" +"," ",amendement)
            # split in words and encode integers
            amendement= [integer_marking(word).strip() for word in amendement.split(" ") if word != " "]
            words=(w for w in amendement)
            wordprecedent = words.next()
            if article :
                amendent_first_line_only.write("|".join(amendement)+"\n")
                if debug :
                    print line
                for word in words:
                    network.append([wordprecedent,word])
                    if wordprecedent==word=="integer" and debug:
                            print line
                    if debug :
                        print wordprecedent,word
                    wordprecedent = word
                nb_line_processed=nb_line_processed+1 
                    
            else :
                # skeep line to be processed later
                pass
if debug :
    pprint.pprint(network)

print "processed %s lines on %s "%(nb_line_processed,nd_line)

with open("network.csv", "w") as outputfile: 
    for link in network:
            outputfile.write('\t'.join(link)+"\n")

    #outputfile.write(",".join([word.encode("utf8") for link in network for node in link ])+"\n")
