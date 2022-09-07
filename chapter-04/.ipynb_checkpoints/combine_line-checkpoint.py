import sys, fileinput
from nltk.tokenize import sent_tokenize

if __name__ == "__main__":
    buf = []

    for line in fileinput.input(): # we are able to get the data of the file line by line by using this method
        if line.strip() != "": # line.strip() devides a sentenceif line is not empty
            buf += [line.strip()] # add each line to the list (same as .append() but you can add multiple elements at once with += operator)
            sentences = sent_tokenize(" ".join(buf)) # .join(list) combines the elements in the list into a string; " " goes in between
                                                     # sentences = list

            if len(sentences) > 1: # 3 sentences => len(sentences) = 3
                buf = sentences[1:] # update buf -> exclude the first sentence

                sys.stdout.write(sentences[0] + '\n') # write the first sentence in sentences list

    sys.stdout.write(" ".join(buf) + "\n") # last sentnece could not be included since len(sentences) = 1 
                                           # so, write it separately outside of the loop
