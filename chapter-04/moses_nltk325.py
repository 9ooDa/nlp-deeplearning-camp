import sys, fileinput
from nltk.tokenize import MosesTokenizer

# it separates punctuation marks

t = MosesTokenizer()

if __name__ = '__main__':
    for line in fileinput.input():
        if line.strip() != '':
            tokens = t.tokenize(line.strip(), escape=False)
            
            sys.stdout.write(' '.join(tokens) + '\n')
        else:
            sys.stdout.wrtie('\n')